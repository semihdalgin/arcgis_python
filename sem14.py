# ---------------------------------------------------------------------------
# create_semih_archydro.py
#
# Coded by :
# Semih DALGIN
# semihdalgin@gmail.com
#
# 
# Requires Arc10 and ArcHydro 2.0
#
#
# ---------------------------------------------------------------------------


# Import system modules
import arcpy, time, datetime, os, sys, string, csv, shutil
arcpy.ImportToolbox("c:\\program files (x86)\\arcgis\\desktop10.2\\ArcToolbox\\Toolboxes\\Arc Hydro Tools.tbx","archydrotools")


verbose = True
cleanup = True

arcpy.CheckOutExtension("Spatial")

try:
    # Script arguments
    arcpy.AddMessage ("\nValidating arguments..." )
    try: 

        # Make parameters array, and later write input parameter values to an output file
        parameters = []
        now = datetime.datetime.now()
        parameters.append("Date and Time: "+ now.strftime("%Y-%m-%d %H:%M"))
        
        # Folder where output files will be saved
        workspace = arcpy.GetParameterAsText(0)
        parameters.append("Workspace: " + workspace)
        
        # Digital Elevation Model raster
        DEM = arcpy.GetParameterAsText(1)
        parameters.append("DEM: " + DEM)
        
    except:
        arcpy.AddMessage("\nError in input arguments: " + arcpy.GetMessages(2))
        raise Exception

    # Check and create output folders

    try:
        arcpy.AddMessage("\nCreating output folders...")
        thefolders=["Intermediate", "Output"]
        for folder in thefolders:
            if not arcpy.Exists(workspace + folder):
                arcpy.CreateFolder_management(workspace, folder)
    except:
        arcpy.AddError("\nError creating output folders: " + arcpy.GetMessages(2))
        raise Exception

    # Output files
    
    try:
        arcpy.AddMessage("\nSetting script variables...")
        # Intermediate and output directories
        outputws = workspace + os.sep + "Output" + os.sep
        interws = workspace + os.sep + "Intermediate" + os.sep

        sshed_gdb_name = "ssheds" + "Suffix" + ".gdb"
        sshed_gdb = interws + sshed_gdb_name

        # ArcHydro does not allow shapefiles as input or output,
        # so do these in a geodatabase
        flow_dir = interws + "flow_dir"
        flow_acc = interws + "flow_acc"
        streams = interws + "streams"
        stream_link = interws + "stream_link"
        stream_sink_link = interws + "str_sink_link"
        catchment_grid = interws + "catch_grid"
        catchment_poly = sshed_gdb + os.sep + "catch_poly"
        drainage_line = sshed_gdb + os.sep + "drainage_line"
        adjoint_catchment = sshed_gdb + os.sep + "adj_catch"
        servicesheds_gdb = sshed_gdb + os.sep + "servicesheds" + Suffix
        serviceshed_points = sshed_gdb + os.sep + "ssheds_points"
        batchpoints = sshed_gdb + os.sep + "batchpoints"

        # Fields required in ArcHydro's batchpoint file
        name_field = "Name"
        descript_field = "Descript"
        batchdone_field = "BatchDone"
        snapon_field = "SnapOn"
        srctype_field = "SrcType"
        bp_field_dict = {name_field:['TEXT', '\" \"'], descript_field:['TEXT', '\" \"'], batchdone_field:['SHORT', '0'], \
                         snapon_field:['SHORT', '1'], srctype_field:['SHORT', '0']}
                
        # Output files
        streams_out = outputws + "streams_" + str(stream_threshold_numcells) + "_" + Suffix + ".tif"
        servicesheds = outputws + "servicesheds" + Suffix + ".shp"

    except:
        arcpy.AddError("\nError configuring local variables: " + arcpy.GetMessages(2))
        raise Exception


    # Check that DEM is projected

    try:
        arcpy.AddMessage("\nChecking DEM properties...")
        dem_spatref = arcpy.Describe(DEM).spatialReference
        if dem_spatref.Type <> "Projected":
            arcpy.AddError("Error: " + DEM + " must have a projected coordinate system for servicesheds to be calculated correctly.")
            raise Exception
    except:
        arcpy.AddError("\nError checking DEM properties: " + arcpy.GetMessages(2)) 
        raise Exception


    # Set the Geoprocessing environment

    try:
        # Make sure all temporary files go in the Intermediate folder
        arcpy.workspace = interws

        # Make sure the user has the necessary versions of ArcGIS and ArcHydro  
        install_info = arcpy.GetInstallInfo("desktop")      
        if (install_info["Version"] <> "10.0"):
            arcpy.AddError("Error: ArcGIS 10 and ArcHydro 2.0 are required to run this tool.")
            raise Exception

        toolboxList = arcpy.ListToolboxes("archydro")
        if "archydro" in toolboxList[0]:
            arcpy.AddMessage("\nArcHydro toolbox found")
            
        else:
            arcpy.AddError("\nError: Can't find ArcHydro in the ArcGIS toolbox list.  Please verify the ArcHydro installation.")
            raise Exception

        ArcHydroTools.SetTargetLocations("HydroConfig", "Layers", interws, sshed_gdb)
        
    except:
        arcpy.AddError("\nError setting geoprocessing environment: " + arcpy.GetMessages(2))
        raise Exception


    # Do all ArcHydro processes involved with making watersheds
    
    try:
            
        arcpy.AddMessage("\nFlow direction...")
        ArcHydroTools.FlowDirection(DEM, flow_dir)

        arcpy.AddMessage("\nFlow accumulation...")
        ArcHydroTools.FlowAccumulation(flow_dir, flow_acc)

        arcpy.AddMessage("\nStream definition...")
        ArcHydroTools.StreamDefinition(flow_acc, stream_threshold_numcells, streams, "")

        # Output the streams layer so users can compare with known streams
        arcpy.CopyRaster_management(streams, streams_out)
        arcpy.AddMessage("\n\tCreated streams output file:\n\t" + str(streams_out))

        arcpy.AddMessage("\nStream segmentation...")
        ArcHydroTools.StreamSegmentation(streams, flow_dir, stream_link, "", "")

        arcpy.AddMessage("\nCatchment grid delineation...")
        ArcHydroTools.CatchmentGridDelineation(flow_dir, stream_link, catchment_grid)

        arcpy.AddMessage("\nCatchment polygons...")
        ArcHydroTools.CatchmentPolyProcessing(catchment_grid, catchment_poly)

        arcpy.AddMessage("\nDrainage lines...")
        ArcHydroTools.DrainageLineProcessing(stream_link, flow_dir, drainage_line)

        arcpy.AddMessage("\nAdjoint catchments...")
        ArcHydroTools.AdjointCatchment(drainage_line, catchment_poly, adjoint_catchment)

        # Prepare user-input outlets to conform with ArcHydro's requirements
        # for batch points

        arcpy.AddMessage("\nPreparing batch points...")
        arcpy.CopyFeatures_management(outlets, batchpoints)

        for bp_field, field_info in bp_field_dict.iteritems():
            field_type = field_info[0]
            field_default = field_info[1]
            
            # Add fields if they do not exist in the input outlets file
            if (len(arcpy.ListFields(batchpoints, bp_field)) == 0):
                arcpy.AddField_management(batchpoints, bp_field, field_type)
                
            # Set field values
            # Name = blank (to start - will set to user input field)
            # Descript = blank (to start - will also set to user input field)
            # BatchDone = 0 (do need to process this point)
            # SnapOn = 1 (do snap point to closest stream)
            # SrcType = 0 (0 = outlet, 1 = inlet)
            arcpy.CalculateField_management(batchpoints, bp_field, field_default)

        # Populate Name, Descript fields with user-specified field values
        arcpy.AddMessage("\n\tUsing field \'" + str(outlets_id_field)+ "\' to assign serviceshed names")
        arcpy.CalculateField_management(batchpoints, name_field, "[" + outlets_id_field + "]")
        arcpy.CalculateField_management(batchpoints, descript_field, "[" + outlets_id_field + "]")

        arcpy.AddMessage("\nCreating servicesheds...")
        ArcHydroTools.BatchWatershedDelineation(batchpoints, flow_dir, streams, streams, \
                                                 catchment_poly, adjoint_catchment, "", \
                                                 servicesheds_gdb, serviceshed_points)

        arcpy.CopyFeatures_management(servicesheds_gdb, servicesheds)
            
        arcpy.AddMessage("\n\tCreated serviceshed output file:\n\t" + str(servicesheds))


    except:
        arcpy.AddError("\nError creating servicesheds:" + arcpy.GetMessages(2))
        raise Exception


    # Write input parameters to an output file for user reference
    try:
        arcpy.AddMessage("\nCreating parameter file...")
        parameters.append("Script location: " + os.path.dirname(sys.argv[0]) + "\\" + os.path.basename(sys.argv[0]))
        parafile = open(outputws + "\\Create_servicesheds" + now.strftime("%Y-%m-%d-%H-%M") + Suffix + ".txt", "w")
        parafile.writelines("CREATE SERVICESHEDS ARCHYDRO\n")
        parafile.writelines("____________________________\n\n")

        for para in parameters:
            parafile.writelines(para + "\n")
            parafile.writelines("\n")
        parafile.close()
    except:
        arcpy.AddError ("\nError creating parameter file: " + arcpy.GetMessages(2))
        raise Exception
    
        
##    # Clean up temporary files
##    arcpy.AddMessage("\nCleaning up temporary files...\n")
##    try:
##        arcpy.Delete_management(interws)
##    except:
##        arcpy.AddError("\nError cleaning up temporary files:  " + arcpy.GetMessages(2))
##        raise Exception


except:
    arcpy.AddError("\nError running script")  
    raise Exception
