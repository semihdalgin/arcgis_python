# -*- coding: cp1254 -*-
# -*- ##################
# ---------------------------------------------------------------------------
# create_semih_archydro.py
#
# Coded by :
# Semih DALGIN
# semihdalgin@gmail.com
#
#
# ---------------------------------------------------------------------------
# Import system modules
import arcpy, time, datetime, os, sys, string, csv, shutil
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
try:
    # Script arguments
    arcpy.AddMessage ("\nDr.Semih DALGIN tarafından yapıldı.")
    arcpy.AddMessage ("\nİletişim adresi: semihdalgin@gmail.com")
    arcpy.AddMessage ("\nBaşlangıç Değerleri Alınıyor..." )
    try:
        # Make parameters array, and later write input parameter values to an output file
        parameters = []
        now = datetime.datetime.now()
        parameters.append("Date and Time: "+ now.strftime("%Y-%m-%d %H:%M"))
        # Folder where output files will be saved
        workspace1 = arcpy.GetParameterAsText(0)
        # Donusum Dosyası
        don = arcpy.GetParameterAsText(1)
        # Projeksiyon
        prj = arcpy.GetParameterAsText(2)
        # 6 Derece Projeksiyon
        sistem=arcpy.GetParameterAsText(3)
    except:
        arcpy.AddMessage("\nError in input arguments: " + arcpy.GetMessages(2))
        raise Exception
    # Check and create output folders
    try:
        arcpy.AddMessage("\nCreating output folders...")
        thefolders=["ED50","ED50_6"]
        for folder in thefolders:
            if not arcpy.Exists(workspace1 + folder):
                arcpy.CreateFolder_management(workspace1, folder)
    except:
        arcpy.AddError("\nError creating output folders: " + arcpy.GetMessages(2))
        raise Exception
    # Calculations
    try:
        arcpy.env.workspace=workspace1
        rstname = arcpy.ListDatasets()
        cc=0
        for fc in rstname:
            cc=cc+1
        for xox in range (0,cc,1):
            rssa=rstname[xox].split(os.extsep)[0]
            exportname=workspace1+"\\ED50\\"+rssa+".tif"
            exportname2=workspace1+"\\ED50_6\\"+rssa+".tif"
            if not arcpy.Exists(exportname):
                dosya=workspace1+"\\"+rstname[xox]
                arcpy.WarpFromFile_management(dosya,exportname,don,"POLYORDER1","NEAREST")
                arcpy.DefineProjection_management(exportname,prj)
            if not arcpy.Exists(exportname2):
                dosya6=workspace1+"\\ED50\\"+rstname[xox]
                arcpy.ProjectRaster_management(dosya6,exportname2,sistem,"NEAREST")                
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\nError running script")
    raise Exception
