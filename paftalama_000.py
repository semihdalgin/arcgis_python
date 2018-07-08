mxd = arcpy.mapping.MapDocument("CURRENT")
layers=arcpy.mapping.ListLayers(mxd,"Mamak_2013_TM_ED50*")
pdf=r'D:\semih.dalgin\MAMAK5000'

for sem in range (0,140,1):
...     arcpy.SelectLayerByAttribute_management("Join_Output","NEW_SELECTION","FID=%d"%sem)
...     df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
...     df.zoomToSelectedFeatures()
...     fc="Join_Output"
...     fields=['Text']
...     with arcpy.da.SearchCursor(fc,fields) as cursor:
...         for row in cursor:
...             filenames=row[0]
...             print filenames
...             sems=pdf+"\\"+str(sem)+".shp"
...             arcpy.Select_analysis("Join_Output",sems)
...             ds=arcpy.Describe(sem)
...             frame = str(ds.extent)
...             frame = str(ds.extent).strip(" NaN")
...             print frame
...             print sem
...             isim=pdf+"\\"+filenames+".tif"
...             arcpy.Clip_management("Mamak_2013_TM_ED50.ecw", frame,isim,sem,"256","ClippingGeometry","MAINTAIN_EXTENT")
...             arcpy.SelectLayerByAttribute_management("Join_Output","CLEAR_SELECTION","")