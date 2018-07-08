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
import arcgisscripting, time, datetime, os, sys, string, csv, shutil
gp= arcgisscripting.create(9.3)
gp.overwriteoutput = 1
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
try:
    # Script arguments
    gp.AddMessage ("\nDr.Semih DALGIN tarafından yapıldı.")
    gp.AddMessage ("\nİletişim adresi: semihdalgin@gmail.com")
    gp.AddMessage ("\nBaşlangıç Değerleri Alınıyor..." )
    try:
        # Folder where output files will be saved
        workspace1 = gp.GetParameterAsText(0)
        # Donusum Dosyasi
        don = gp.GetParameterAsText(1)
        
    except:
        gp.AddMessage("\nError in input arguments: " + gp.GetMessages(2))
        
    # Check and create output folders
    try:
        gp.AddMessage("\nKlasörler Oluşturuluyor...")
        thefolders=["ULKE"]
        for folder in thefolders:
            if not gp.Exists(workspace1 + folder):
                gp.CreateFolder_management(workspace1, folder)
    except:
        gp.AddError("\nDosya Oluşturmada Hata: " + gp.GetMessages(2))
        raise Exception
        
    # Calculations
    try:
        gp.workspace=workspace1
        rstname = gp.ListDatasets()
        cc=0
        dosyadre = open(don)
        SourcePoints=dosyadre.readline()
        gp.AddMessage("\nResim Koordinatları:  " + str(SourcePoints))
        TargetPoints=dosyadre.readline()
        gp.AddMessage("\nHarita Koordinatları:  " + str(TargetPoints))
        for fc in rstname:
            cc=cc+1
        for xox in range (0,cc,1):
            rssa=rstname[xox].split(os.extsep)[0]
            exportname=workspace1+"\\ULKE\\"+rssa+".tif"
            gp.AddMessage("\nÇalışılan Dosya " + str(rssa)+" "+str(xox+1))
            if not gp.Exists(exportname):
                dosya=workspace1+"\\"+rstname[xox]
                gp.Warp(dosya,SourcePoints,TargetPoints,exportname,"POLYORDER1","NEAREST")              
    except:
        gp.AddError("\nHata Hesaplamalarda" + gp.GetMessages(2))
        raise Exception
          
except:
    gp.AddError("\nError running script")
    raise Exception
    
