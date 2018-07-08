# -*- ##################
# ---------------------------------------------------------------------------
# create_semih_archydro.py
#
# Coded by :
# Semih DALGIN
# semihdalgin@gmail.com
#
# 
# Requires Arc10
#
#
# ---------------------------------------------------------------------------
# Import system modules
import arcpy, time, datetime, os, sys, string, csv, shutil
try:
    # Script arguments
    arcpy.AddMessage ("\nBaþlangýç Deðerleri Alýnýyor..." )
    try:
        # Folder where output files will be saved
        workspace1 = arcpy.GetParameterAsText(0)
        clipfile = arcpy.GetParameterAsText(1)
        output = arcpy.GetParameterAsText(2)
    except:
        arcpy.AddMessage("\n Hata Girdi Verilerinde: ")
        raise Exception
    # Check and create output folders
    try:
        arcpy.env.workspace=workspace1
        dwgname = arcpy.ListDatasets()
        fccount = len(arcpy.ListFeatureClasses("",""))
        feature_classes = []
        for dirpath, dirnames, filenames in arcpy.da.Walk(workspace1,datatype="FeatureClass",type="Any"):
            for filename in filenames:
                feature_classes.append(os.path.join(dirpath, filename))
        for xox in range (0,fccount,1):
            outfilename=output+"\\"+filenames[xox]
            arcpy.Clip_analysis(feature_classes[xox],clipfile,outfilename)            
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\n Sonda hata")
    raise Exception
