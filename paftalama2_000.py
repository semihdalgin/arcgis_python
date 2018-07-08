for sem in range (0,1,1):
...     arcpy.SelectLayerByAttribute_management("1000_index","NEW_SELECTION","FID=%d"%sem)
...     df = arcpy.mapping.ListDataFrames(mxd, "Layers") [0]
...     df.zoomToSelectedFeatures()
...     fc="1000_index"
...     fields=['Text']
...     with arcpy.da.SearchCursor(fc,fields) as cursor:
...         for row in cursor:
...             filenames=row[0]
...             print filenames
...             sems=pdf+"\\"+str(sem)+".shp"
...             arcpy.Select_analysis("1000_index",sems)
...             ds=arcpy.Describe(sem)
...             frame = str(ds.extent)
...             frame = str(ds.extent).strip(" NaN")
...             print frame
...             print sem
...             isim=pdf+"\\"+filenames+".tif"
