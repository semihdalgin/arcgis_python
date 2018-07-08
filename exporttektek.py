import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
for sem in range (1,102,1):
  arcpy.SelectLayerByAttribute_management("ORTA_FIRAT_HALK_SULAMALARI_REV6","CLEAR_SELECTION","")
  arcpy.SelectLayerByAttribute_management("ORTA_FIRAT_HALK_SULAMALARI_REV6","NEW_SELECTION","OBJECTID=%d"%sem)
  myList = set([row.getValue("OBJECTID")for row in arcpy.SearchCursor("ORTA_FIRAT_HALK_SULAMALARI_REV6")])
  aa=row.getValue("Firat_HD_HALK_SULAMALARI_sul_adi")
  bb=aa.split()
  ccc=0
  ee="SD_"
  for ff in bb:
      ccc=ccc+1
  for xox in range (0,ccc,1):
      ee=ee+bb[xox]
  outputfile="V:\\3-CALISMALAR\\10_CIGDEM\\ZÝRAAT\\SHP\\ziraat2.gdb"
  out=outputfile+ee
  arcpy.env.workspace=outputfile
  for dirpath, dirnames, filenames in arcpy.da.Walk(outputfile,datatype="FeatureClass",type="Any"):
    for filename in filenames:
      feature_classes.append(os.path.join(dirpath, filename))
  if not arcpy.Exists(ee):
    arcpy.FeatureClassToFeatureClass_conversion("ORTA_FIRAT_HALK_SULAMALARI_REV6",outputfile,ee)
  else:
    print "Yok"
  

