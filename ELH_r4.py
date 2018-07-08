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
try:
    # Script arguments
    arcpy.AddMessage ("\nBaþlangýç Deðerleri Alýnýyor..." )
    try:
        # Folder where output files will be saved
        pdf = arcpy.GetParameterAsText(0)
        bas = arcpy.GetParameterAsText(1)
        bit = arcpy.GetParameterAsText(2)
        callayer=arcpy.GetParameterAsText(3)
        scalesem=arcpy.GetParameterAsText(4)
        sulkat = arcpy.GetParameterAsText(5)
        sirala= arcpy.GetParameterAsText(6)
        mxd = arcpy.mapping.MapDocument("CURRENT")
        layers=arcpy.mapping.ListLayers(mxd,"*HALK*")
        df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0] 
        veris=int(bit)+1
    except:
        arcpy.AddMessage("\n Hata Girdi Verilerinde: ")
        raise Exception
    # Check and create output folders
    try:
        for sem in range (int(bas),veris,1):
            query = sirala+"="+"%d"%sem
            layers[0].definitionQuery=query
            myList = set([row.getValue(sirala)for row in arcpy.SearchCursor(callayer)])
            aa=row.getValue(sulkat)
            bb=aa.split()
            ccc=0
            ee="SD_"
            for ff in bb:
                ccc=ccc+1
            for xox in range (0,ccc,1):
                ee=ee+bb[xox] 
            exportname=pdf+"\\"+str(ee)
            ddp = mxd.dataDrivenPages
            pageID = sem
            mxd.dataDrivenPages.currentPageID = pageID
            df.scale = scalesem # we set the scale to 1:25,000  
            arcpy.mapping.ExportToPDF(mxd,exportname) # export the current Page to pdf   
    except:
        arcpy.AddError("\nHata Hesaplamalarda" + arcpy.GetMessages(2))
        raise Exception    
except:
    arcpy.AddError("\n Sonda hata")
    raise Exception
