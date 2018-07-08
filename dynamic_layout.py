mxd = arcpy.mapping.MapDocument("CURRENT")
layers=arcpy.mapping.ListLayers(mxd,"ORTA_FIRAT_HALK*")
pdf=r'V:\3-CALISMALAR\10_CIGDEM\ZÝRAAT\PDF'
for sem in range (1,102,1):
    query = "[OBJECTID]="+"%d"%sem
    layers[0].definitionQuery=query
    ddp = mxd.dataDrivenPages
    pageID = sem
    mxd.dataDrivenPages.currentPageID = pageID
    exportname=pdf+"\\SD"+str(sem)
    arcpy.mapping.ExportToPDF(mxd, exportname) # export the current Page to pdf
    
