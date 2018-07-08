# Import system modules
import arcpy, time, datetime, os, sys, string

try:
    # Script arguments
    arcpy.AddMessage ("\nValidating arguments..." )
    try:         
        # Nokta Dosyası
        SHP = arcpy.GetParameterAsText(0)
        # Çıktı Dosyası
        GDB = arcpy.GetParameterAsText(1)
	#GDB="C:\\150827\\Maras.gdb"
	# KMZ Yapılsın mı Yapılmasın mı
        KMZ = arcpy.GetParameterAsText(2)       
    except:
        arcpy.AddMessage("\nBaşlangıç Değerlerini Almada Sıkıntı: " + arcpy.GetMessages(2))
        raise Exception	
    try:
	number= int(arcpy.GetCount_management(SHP).getOutput(0))
	for x in range (0,number,1):
	     whereClause="FID"+"="+str("%d") %(x)
	     fields=['FID','ProjectNam']
	     with arcpy.da.SearchCursor(SHP,fields,whereClause)as cursor:
	         for RES in cursor:
	             res2=RES[1]
		     arcpy.AddMessage(res2+"Yapılıyor")
	             duzelt=res2.split()
	             YOL=GDB+"\\"+duzelt[0]+duzelt[1]
	             if not arcpy.Exists(YOL):
	                 Clause = "ProjectNam" + " = '" + res2 + "'"+"AND PointType='K'"
	                 arcpy.SelectLayerByAttribute_management(SHP,"NEW_SELECTION",Clause)
	                 arcpy.PointsToLine_management(SHP,YOL,"","","CLOSE")
	             else:
	                 arcpy.SelectLayerByAttribute_management(SHP, "CLEAR_SELECTION")
    except:
	 arcpy.AddMessage("\nHesaplamalarda Sıkıntı: " + arcpy.GetMessages(2))
     raise Exception
except:
    arcpy.AddError("\nError running script")  
    raise Exception