# Import system modules
import arcpy, time, datetime, os, sys, string

verbose = True
cleanup = True


try:
    # Script arguments
    arcpy.AddMessage ("\nValidating arguments..." )
    try: 

        # Make parameters array, and later write input parameter values to an output file
        parameters = []
        now = datetime.datetime.now()
        parameters.append("Date and Time: "+ now.strftime("%Y-%m-%d %H:%M"))
        
                
        # Nokta Dosyası
        SHP = arcpy.GetParameterAsText(0)
        parameters.append("Çalışma Dosyası: " + SHP)

        # Çıktı Dosyası
        GDB = arcpy.GetParameterAsText(1)
        parameters.append("Çıktı MDB: " + GDB)
		
		# KMZ Yapılsın mı Yapılmasın mı
        KMZ = arcpy.GetParameterAsText(2)
        parameters.append("KMZ onay: " + KMZ)
        
    except:
        arcpy.AddMessage("\nBaşlangıç Değerlerini Almada Sıkıntı: " + arcpy.GetMessages(2))
        raise Exception
		
		
	try:
	 number_data = int(arcpy.GetCount_management(SHP).getOutput(0))+1
		for x in range (1,number_data,1):
		 whereClause="OBJECTID"+"="+str(""%d"") %(x)
		 fields=['OBJECTID','ProjectName']
		 with arcpy.da.SearchCursor(SHP,fields,whereClause)as cursor:
     			for RES in cursor:
         		print (RES)
		RES2=RES[1]
		if not arcpy.Exists(GDB+"\\RES2"):
		 Clause = "ProjectNam" + " = '" + res2 + "'"+"AND PointType='K'"
		 arcpy.SelectLayerByAttribute_management(SHP,"NEW_SELECTION",Clause)
		 arcpy.PointsToLine_management(SHP,GDB,"","","CLOSE")
	
	except:
	  arcpy.AddMessage("\nHesaplamalarda Sıkıntı: " + arcpy.GetMessages(2))
          raise Exception
except:
    arcpy.AddError("\nError running script")  
    raise Exception