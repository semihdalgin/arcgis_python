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
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]

arcpy.AddMessage("\nBaþlangýç Deðerleri Tamamlandý...")

try:
    # Script arguments
    arcpy.AddMessage ("\nValidating arguments..." )
    try: 

	arcpy.AddMessage("\nDevam Ediyor...")        
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
	stream_threshold_numcells = arcpy.GetParameterAsText(2)
        parameters.append("Stream threshold - number of cells: " + str(stream_threshold_numcells))

	#arcpy.AddMessage("\nDeðerler Alýndý..."+stream_threshold_numcells)
        
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
	if not arcpy.Exists(inter+"\\data.gdb"):
	 arcpy.CreateFileGDB_management(inter,"data","CURRENT")

        # ArcHydro does not allow shapefiles as input or output,
        # so do these in a geodatabase
	ekonum=interws+"data.gb"
        fillkonum=interws+"Fil"
	flow_dir = interws + "flow_dir"
        flow_acc = interws + "flow_acc"
        streams = interws + "streams"
        stream_link = interws + "stream_link"
        stream_sink_link = interws + "str_sink_link"
        catchment_grid = interws + "catch_grid"
        catchment_poly = ekonum + os.sep + "catch_poly"
        drainage_line = ekonum + os.sep + "drainage_line"
        adjoint_catchment = ekonum + os.sep + "adj_catch"
        arcpy.AddMessage("\nHata Var mý...")
        # Make sure all temporary files go in the Intermediate folder
        arcpy.workspace = interws
    except:
        arcpy.AddError("\nError configuring local variables: " + arcpy.GetMessages(2))
        raise Exception
    
    try:
        arcpy.AddMessage("\nBoþlukar Dolduruluyor...")    
	FIL=arcpy.sa.Fill(DEM,"")
	FIL.save(fillkonum)
	ddd13=arcpy.mapping.Layer(fillkonum)
	arcpy.mapping.AddLayer(df,ddd13)        

	arcpy.AddMessage("\nFlow direction...")
	FDR=arcpy.sa.FlowDirection(FIL,"NORMAL","")
	FDR.save(flow_dir)
	ddd12=arcpy.mapping.Layer(flow_dir)
	arcpy.mapping.AddLayer(df,ddd12)

        arcpy.AddMessage("\nFlow accumulation...")
	FAC=arcpy.sa.FlowAccumulation(FDR,"","")
	FAC.save(flow_acc)
	ddd11=arcpy.mapping.Layer(flow_acc)
	arcpy.mapping.AddLayer(df,ddd11)

        arcpy.AddMessage("\nStream definition...")
	arcpy.StreamDefinition_archydrotools(FAC,stream_threshold_numcells,streams,"")

	ddd1=arcpy.mapping.Layer(streams)
	arcpy.mapping.AddLayer(df,ddd1)

        arcpy.AddMessage("\nStream segmentation...")

	strlnk=arcpy.sa.StreamLink("Str",FDR)
	strlnk.save(stream_link)

        arcpy.AddMessage("\nCatchment grid delineation...")
	arcpy.CatchmentGridDelineation_archydrotools(FDR,strlnk,catchment_grid)
	dddd=arcpy.mapping.Layer(catchment_grid)
	arcpy.mapping.AddLayer(df,dddd)
        arcpy.AddMessage("\nCatchment polygons...")
	arcpy.CatchmentPolyProcessing_archydrotools(catchment_grid, catchment_poly)
        arcpy.AddMessage("\nDrainage lines...")
        arcpy.DrainageLineProcessing_archydrotools(stream_link, FDR, drainage_line)
        arcpy.AddMessage("\nAdjoint catchments...")
        arcpy.AdjointCatchment_archydrotools(drainage_line, catchment_poly, adjoint_catchment)

    except:
        arcpy.AddError("\nError creating servicesheds:" + arcpy.GetMessages(2))
        raise Exception    

except:
    arcpy.AddError("\nError running script")  
    raise Exception