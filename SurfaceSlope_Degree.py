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
        # Projeksiyon
        prj = arcpy.GetParameterAsText(1)
        
    except:
        arcpy.AddMessage("\nError in input arguments: " + arcpy.GetMessages(2))
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
            arcpy.AddMessage("\nÇalışılan Dosya " + str(rssa)+" "+str(xox+1))
            dosya=workspace1+"\\"+rstname[xox]
            arcpy.sa.Slope("devrez_havza_y1","DEGREE")
            arcpy.sa.Slope("devrez_havza_y1","PERCENT_RISE"
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\nError running script")
    raise Exception
