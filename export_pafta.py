mxd = arcpy.mapping.MapDocument("CURRENT")
layers=arcpy.mapping.ListLayers(mxd,"ORTA_FIRAT_HALK*")
pdf=r'V:\3-CALISMALAR\10_CIGDEM\ZÝRAAT\PDF'
for sem in range (1,5,1):
    query = "[OBJECTID]="+"%d"%sem
    layers[0].definitionQuery=query
    arcpy.SelectLayerByAttribute_management("ORTA_FIRAT_HALK_SULAMALARI_REV6","NEW_SELECTION","OBJECTID=%d"%sem)
    df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
    df.zoomToSelectedFeatures()
    arcpy.SelectLayerByAttribute_management("ORTA_FIRAT_HALK_SULAMALARI_REV6","CLEAR_SELECTION","")
    ddp = mxd.dataDrivenPages
    pageID = sem
    mxd.dataDrivenPages.currentPageID = pageID
    exportname=pdf+"\\sd"+str(sem)
    arcpy.mapping.ExportToPDF(mxd, pdf) # export the current Page to pdf
    arcpy.mapping.ExportToJPEG(mxd,exportname) #jpeg

