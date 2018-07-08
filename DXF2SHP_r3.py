# -*- ##################
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
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
try:
    # Script arguments
    arcpy.AddMessage ("\nBaþlangýç Deðerleri Alýnýyor..." )
    try:
        # Make parameters array, and later write input parameter values to an output file
        parameters = []
        now = datetime.datetime.now()
        parameters.append("Date and Time: "+ now.strftime("%Y-%m-%d %H:%M"))

        # Folder where output files will be saved
        workspace1 = arcpy.GetParameterAsText(0)
        parameters.append("Workspace: " + workspace1)

    except:
        arcpy.AddMessage("\nError in input arguments: " + arcpy.GetMessages(2))
        raise Exception
    # Check and create output folders
    try:
        dwgname=[]
        arcpy.env.workspace=workspace1
        dwgname = arcpy.ListDatasets()
        cc=0
        for fc in dwgname:
            cc=cc+1
        sem=[]
        for xox in range (0,cc,1):   
            sem.append(dwgname [xox] + " Polyline")
            arcpy.MakeFeatureLayer_management(dwgname[xox] + "/Polyline",sem[xox])        
        for aa in range (0,23,1):
            alfabe="abcdefghijklmnoprstuvyz"
            aalfabe=alfabe[aa:aa+1]
            for y in range (1,90,1):
                for x in range (1,5,1):
                    for z in range (0,4,1):
                        harf="abcd"
                        xharf=harf[z:z+1]
                        name="%s" %aalfabe+"%s" %y+"%s" %xharf + "%d"%x+".dxf Polyline"
                        if arcpy.Exists("%s" %name):
                            arcpy.SelectLayerByAttribute_management("%s" %name,"CLEAR_SELECTION","")
                            arcpy.SelectLayerByAttribute_management("%s" %name,"NEW_SELECTION","Layer = 'ANA_MUNHANI' OR Layer = 'ARA_MUNHANI' OR Layer = 'YRD_MUNHANI'")
                            exportname="%s" %aalfabe+"%s" %y+"%s" %xharf + "%d"%x+".shp"
                            arcpy.FeatureClassToFeatureClass_conversion("%s" %name,workspace1,exportname,"","","")
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\nError running script")
    raise Exception
