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
		inter = workspace + os.sep + "Intermediate"

		#sshed_gdb_name = "data" + ".gdb"
		#sshed_gdb = interws +"data"+".gdb"
		
		if not arcpy.Exists(inter+"\\data.gdb"):
			arcpy.CreateFileGDB_management(inter,"data","CURRENT")
        

        # ArcHydro does not allow shapefiles as input or output,
        # so do these in a geodatabase
		ekonum=interws+"data.gb"
        flow_dir = interws + "flow_dir"
        flow_acc = interws + "flow_acc"
        streams = interws + "streams"
        stream_link = interws + "stream_link"
        stream_sink_link = interws + "str_sink_link"
        catchment_grid = interws + "catch_grid"
        catchment_poly = ekonum + os.sep + "catch_poly"
        drainage_line = ekonum + os.sep + "drainage_line"
        adjoint_catchment = ekonum + os.sep + "adj_catch"
        servicesheds_gdb = ekonum + os.sep + "servicesheds" + Suffix
        serviceshed_points = ekonum + os.sep + "ssheds_points"
        batchpoints = ekonum + os.sep + "batchpoints"

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

   
except:
    arcpy.AddError("\nError running script")  
    raise Exception
