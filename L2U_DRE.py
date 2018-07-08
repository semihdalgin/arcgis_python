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
import arcpy, time, datetime, os, sys, string, csv, shutil, fileinput, string
import arcgisscripting
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"Layers")[0]
arcpy.env.overwriteOutput=True


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
        # Donusum Dosyasi
        don = arcpy.GetParameterAsText(1)
        # DRE
        #dre = arcpy.GetParameterAsText(2)
        # Projeksiyon
        prj = arcpy.GetParameterAsText(2)
        
    except:
        arcpy.AddMessage("\nError in input arguments: " + arcpy.GetMessages(2))
        raise Exception
    # Check and create output folders
    try:
        arcpy.AddMessage("\nCreating output folders...")
        thefolders=["DRE","ULKE"]
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
            exportname=workspace1+"\\DRE\\"+rssa+".tif"
            exportname1=workspace1+"\\ULKE\\"+rssa+".tif"
            arcpy.AddMessage("\nÇalışılan Dosya " + str(rssa)+" "+str(xox+1))
            dreal=workspace1+"\\"+rssa+".dre"
            dreadi=workspace1+"\\DRE\\"+rssa+".txt"
                            
            dosyadre = open(dreal) 
            asd = dosyadre.read() 
            dosya1 = open(dreadi, 'a+') 

            with open(dreal) as openfile:
                for line in openfile:
                    for part in line.split():
                        if "RasterPY1=" in part:
                            a1= part.split('=')[1]
                        if "RasterPX1=" in part:
                            a2= part.split('=')[1]
                        if "HaritaPY1=" in part:
                            a3= part.split('=')[1]
                        if "HaritaPX1=" in part:
                            a4= part.split('=')[1]
                        if "RasterPY2=" in part:
                            a5= part.split('=')[1]
                        if "RasterPX2=" in part:
                            a6= part.split('=')[1]
                        if "HaritaPY2=" in part:
                            a7= part.split('=')[1]
                        if "HaritaPX2=" in part:
                            a8= part.split('=')[1]
                        if "RasterPY3=" in part:
                            a9= part.split('=')[1]
                        if "RasterPX3=" in part:
                            a10= part.split('=')[1]
                        if "HaritaPY3=" in part:
                            a11= part.split('=')[1]
                        if "HaritaPX3=" in part:
                            a12= part.split('=')[1]
                        if "RasterPY4=" in part:
                            a13= part.split('=')[1]
                        if "RasterPX4=" in part:
                            a14= part.split('=')[1]
                        if "HaritaPY4=" in part:
                            a15= part.split('=')[1]
                        if "HaritaPX4=" in part:
                            a16= part.split('=')[1]
                
            dosya1.write(a1+","+a2+","+a3+","+a4+"\n"+a5+","+a6+","+a7+","+a8+"\n"+a9+","+a10+","+a11+","+a12+"\n"+a13+","+a14+","+a15+","+a16+"\n") 
            dosya1.close()
   
            if not arcpy.Exists(exportname):
                dosya=workspace1+"\\"+rstname[xox]
                arcpy.AddMessage("\nÇalışılan Dosya " + str(dosya))
                arcpy.WarpFromFile_management(dosya,exportname,dreadi,"POLYORDER1","NEAREST")
                arcpy.DefineProjection_management(exportname,prj)
            if not arcpy.Exists(exportname1):
                dosya1=workspace1+"\\DRE\\"+rstname[xox]
                arcpy.AddMessage("\nÇalışılan Dosya " + str(dosya1))
                arcpy.WarpFromFile_management(dosya1,exportname1,don,"POLYORDER1","NEAREST")
                arcpy.DefineProjection_management(exportname1,prj)             
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\nError running script")
    raise Exception
