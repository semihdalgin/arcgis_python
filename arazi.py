import arcpy
arcpy.env.workspace = "D:\\TOPRAK\\3"
featureClass = r"V:\3-CALISMALAR\01_SEMIH\00_TOPRAK_KAYNAKLARI\MDB3\outgdb.dbf"
rows = arcpy.SearchCursor(featureClass)
for semsem in range (1,100,1):
    row=rows.next()
    exname=row.AD + ".mdb"
    ex=row.AD
    girdi="D:\\TOPRAK\\3"
    arazi=girdi+"\\"+exname+"\\Drenaj_Katmani"
    features = arcpy.UpdateCursor(arazi)
    for feature in features:
        if feature.drenaj_sistemi == "1":
            feature.drenaj_sistemi = "YD_30"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "2":
            feature.drenaj_sistemi = "YD_45"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "3":
            feature.drenaj_sistemi = "YD_60"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "4":
            feature.drenaj_sistemi = "YD_75"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "5":
            feature.drenaj_sistemi = "YD_90"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "6":
            feature.drenaj_sistemi = "YD_100"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "7":
            feature.drenaj_sistemi = "ÇD"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "8":
            feature.drenaj_sistemi = "PDD"
            features.updateRow(feature)
        if feature.drenaj_sistemi == "9":
            feature.drenaj_sistemi = "ÇH"
            features.updateRow(feature)
