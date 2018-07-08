# Import system modules
import arcpy, time, datetime, os, sys, string

try:
    # Script arguments
    arcpy.AddMessage ("\nValidating arguments..." )
    try:         
        # Nokta Dosyas�
        SHP = arcpy.GetParameterAsText(0)
        # ��kt� Dosyas�
        GDB = arcpy.GetParameterAsText(1)
	#GDB="C:\\150827\\Maras.gdb"
	# KMZ Yap�ls�n m� Yap�lmas�n m�
        KMZ = arcpy.GetParameterAsText(2)       
    except:
        arcpy.AddMessage("\nBa�lang�� De�erlerini Almada S�k�nt�: " + arcpy.GetMessages(2))
        raise Exception	
    try:
	number= int(arcpy.GetCount_management(SHP).getOutput(0))
	for x in range (0,number,1):
	     whereClause="FID"+"="+str("%d") %(x)
	     fields=['FID','ProjectNam']
	     with arcpy.da.SearchCursor(SHP,fields,whereClause)as cursor:
	         for RES in cursor:
	             res2=RES[1]
		     arcpy.AddMessage(res2+"Yap�l�yor")
	             duzelt=res2.split()
	             YOL=GDB+"\\"+duzelt[0]+duzelt[1]
	             if not arcpy.Exists(YOL):
	                 Clause = "ProjectNam" + " = '" + res2 + "'"+"AND PointType='K'"
	                 arcpy.SelectLayerByAttribute_management(SHP,"NEW_SELECTION",Clause)
	                 arcpy.PointsToLine_management(SHP,YOL,"","","CLOSE")
	             else:
	                 arcpy.SelectLayerByAttribute_management(SHP, "CLEAR_SELECTION")
     except:
	 arcpy.AddMessage("\nHesaplamalarda S�k�nt�: " + arcpy.GetMessages(2))
         raise Exception
except:
    arcpy.AddError("\nError running script")  
    raise Exception