import arcpy
arcpy.env.workspace = "D:\\TOPRAK\\3"
featureClass = r"V:\3-CALISMALAR\01_SEMIH\00_TOPRAK_KAYNAKLARI\MDB3\outgdb.dbf"
rows = arcpy.SearchCursor(featureClass)
for semsem in range (1,100,1):
    row=rows.next()
    exname=row.AD + ".mdb"
    ex=row.AD
    girdi="D:\\TOPRAK\\3"
    arazi=girdi+"\\"+exname+"\\Arazi_Katmani"
    features = arcpy.UpdateCursor(arazi)
    for feature in features:
        if feature.ana_sinif == "7":
            feature.ana_sinif = "6_Orman"
            features.updateRow(feature)
        if feature.ana_sinif == "8":
            feature.ana_sinif = "6_Mezarlik"
            features.updateRow(feature)
        if feature.ana_sinif == "9":
            feature.ana_sinif = "6_Aks"
            features.updateRow(feature)
        if feature.ana_sinif == "10":
            feature.ana_sinif = "6_Gol"
            features.updateRow(feature)
        if feature.ana_sinif == "11":
            feature.ana_sinif = "6_Yer"
            features.updateRow(feature)
        if feature.ana_sinif == "12":
            feature.ana_sinif = "6_Yol"
            features.updateRow(feature)
        if feature.ana_sinif == "13":
            feature.ana_sinif = "6_Dere"
            features.updateRow(feature)
        if feature.ana_sinif == "14":
            feature.ana_sinif = "6_Yer_dis"
            features.updateRow(feature)
        if feature.islah_sinif == "1":
            feature.islah_sinif = "5t"
            features.updateRow(feature)
        if feature.islah_sinif == "2":
            feature.islah_sinif = "5s"
            features.updateRow(feature)
        if feature.islah_sinif == "3":
            feature.islah_sinif = "5d"
            features.updateRow(feature)
        if feature.islah_sinif == "4":
            feature.islah_sinif = "5h"
            features.updateRow(feature)
        if feature.islah_sinif == "5":
            feature.islah_sinif = "5st"
            features.updateRow(feature)
        if feature.islah_sinif == "6":
            feature.islah_sinif = "5td"
            features.updateRow(feature)
        if feature.islah_sinif == "7":
            feature.islah_sinif = "5sd"
            features.updateRow(feature)
        if feature.islah_sinif == "8":
            feature.islah_sinif = "5std"
            features.updateRow(feature)
        if feature.tali_sinif == "2":
            feature.tali_sinif = "2t"
            features.updateRow(feature)
        if feature.tali_sinif == "3":
            feature.tali_sinif = "2s"
            features.updateRow(feature)
        if feature.tali_sinif == "4":
            feature.tali_sinif = "2d"
            features.updateRow(feature)
        if feature.tali_sinif == "5":
            feature.tali_sinif = "2st"
            features.updateRow(feature)
        if feature.tali_sinif == "6":
            feature.tali_sinif = "2sd"
            features.updateRow(feature)
        if feature.tali_sinif == "7":
            feature.tali_sinif = "2td"
            features.updateRow(feature)
        if feature.tali_sinif == "8":
            feature.tali_sinif = "2std"
            features.updateRow(feature)
        if feature.tali_sinif == "9":
            feature.tali_sinif = "3s"
            features.updateRow(feature)
        if feature.tali_sinif == "10":
            feature.tali_sinif = "3t"
            features.updateRow(feature)
        if feature.tali_sinif == "11":
            feature.tali_sinif = "3d"
            features.updateRow(feature)
        if feature.tali_sinif == "12":
            feature.tali_sinif = "3st"
            features.updateRow(feature)
        if feature.tali_sinif == "13":
            feature.tali_sinif = "3sd"
            features.updateRow(feature)
        if feature.tali_sinif == "14":
            feature.tali_sinif = "3std"
            features.updateRow(feature)
        if feature.tali_sinif == "15":
            feature.tali_sinif = "4Ps"
            features.updateRow(feature)
        if feature.tali_sinif == "16":
            feature.tali_sinif = "4Pd"
            features.updateRow(feature)
        if feature.tali_sinif == "17":
            feature.tali_sinif = "4Pt"
            features.updateRow(feature)
        if feature.tali_sinif == "18":
            feature.tali_sinif = "4Pst"
            features.updateRow(feature)
        if feature.tali_sinif == "19":
            feature.tali_sinif = "4Pstd"
            features.updateRow(feature)
        if feature.tali_sinif == "20":
            feature.tali_sinif = "4F"
            features.updateRow(feature)
        if feature.tali_sinif == "21":
            feature.tali_sinif = "4F"
            features.updateRow(feature)
        if feature.tali_sinif == "22":
            feature.tali_sinif = "4R"
            features.updateRow(feature)
        if feature.tali_sinif == "23":
            feature.tali_sinif = "6s"
            features.updateRow(feature)
        if feature.tali_sinif == "24":
            feature.tali_sinif = "6t"
            features.updateRow(feature)
        if feature.tali_sinif == "25":
            feature.tali_sinif = "6d"
            features.updateRow(feature)
        if feature.tali_sinif == "26":
            feature.tali_sinif = "6st"
            features.updateRow(feature)
        if feature.tali_sinif == "27":
            feature.tali_sinif = "6sd"
            features.updateRow(feature)
        if feature.tali_sinif == "28":
            feature.tali_sinif = "6std"
            features.updateRow(feature)
        if feature.arazi_kullanim == "1":
            feature.arazi_kullanim = "C"
            features.updateRow(feature)
        if feature.arazi_kullanim == "2":
            feature.arazi_kullanim = "L"
            features.updateRow(feature)
        if feature.arazi_kullanim == "3":
            feature.arazi_kullanim = "P"
            features.updateRow(feature)
        if feature.arazi_kullanim == "4":
            feature.arazi_kullanim = "G"
            features.updateRow(feature)
        if feature.arazi_kullanim == "5":
            feature.arazi_kullanim = "B"
            features.updateRow(feature)
        if feature.arazi_kullanim == "6":
            feature.arazi_kullanim = "W"
            features.updateRow(feature)
        if feature.drenaj_yetenegi == "1":
            feature.drenaj_yetenegi = "X"
            features.updateRow(feature)
        if feature.drenaj_yetenegi == "2":
            feature.drenaj_yetenegi = "Y"
            features.updateRow(feature)
        if feature.drenaj_yetenegi == "3":
            feature.drenaj_yetenegi = "Z"
            features.updateRow(feature)
        if feature.islah_yetersiz == "1":
            feature.islah_yetersiz = "a"
            features.updateRow(feature)
        if feature.islah_yetersiz == "2":
            feature.islah_yetersiz = "A"
            features.updateRow(feature)
        if feature.islah_yetersiz == "3":
            feature.islah_yetersiz = "o"
            features.updateRow(feature)
        if feature.islah_yetersiz == "4":
            feature.islah_yetersiz = "f"
            features.updateRow(feature)
        if feature.islah_yetersiz == "5":
            feature.islah_yetersiz = "w5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "6":
            feature.islah_yetersiz = "aA"
            features.updateRow(feature)
        if feature.islah_yetersiz == "7":
            feature.islah_yetersiz = "ao"
            features.updateRow(feature)
        if feature.islah_yetersiz == "8":
            feature.islah_yetersiz = "af"
            features.updateRow(feature)
        if feature.islah_yetersiz == "9":
            feature.islah_yetersiz = "aw5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "10":
            feature.islah_yetersiz = "Ao"
            features.updateRow(feature)
        if feature.islah_yetersiz == "11":
            feature.islah_yetersiz = "Af"
            features.updateRow(feature)
        if feature.islah_yetersiz == "12":
            feature.islah_yetersiz = "Aw5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "13":
            feature.islah_yetersiz = "of"
            features.updateRow(feature)
        if feature.islah_yetersiz == "14":
            feature.islah_yetersiz = "fw5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "15":
            feature.islah_yetersiz = "aAo"
            features.updateRow(feature)
        if feature.islah_yetersiz == "16":
            feature.islah_yetersiz = "aAf"
            features.updateRow(feature)
        if feature.islah_yetersiz == "17":
            feature.islah_yetersiz = "aAw5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "18":
            feature.islah_yetersiz = "ofw5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "19":
            feature.islah_yetersiz = "Aof"
            features.updateRow(feature)
        if feature.islah_yetersiz == "20":
            feature.islah_yetersiz = "Aow5"
            features.updateRow(feature)
        if feature.islah_yetersiz == "21":
            feature.islah_yetersiz = "aAofw5"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "1":
            feature.Profil_kisitliligi = "e1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "2":
            feature.Profil_kisitliligi = "e2"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "3":
            feature.Profil_kisitliligi = "e3"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "4":
            feature.Profil_kisitliligi = "e4"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "5":
            feature.Profil_kisitliligi = "e6"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "6":
            feature.Profil_kisitliligi = "k1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "7":
            feature.Profil_kisitliligi = "k2"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "8":
            feature.Profil_kisitliligi = "k3"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "9":
            feature.Profil_kisitliligi = "k4"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "10":
            feature.Profil_kisitliligi = "k6"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "11":
            feature.Profil_kisitliligi = "b1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "12":
            feature.Profil_kisitliligi = "b2"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "13":
            feature.Profil_kisitliligi = "b3"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "14":
            feature.Profil_kisitliligi = "b4"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "15":
            feature.Profil_kisitliligi = "b6"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "16":
            feature.Profil_kisitliligi = "ş1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "17":
            feature.Profil_kisitliligi = "z1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "18":
            feature.Profil_kisitliligi = "z2"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "19":
            feature.Profil_kisitliligi = "z3"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "20":
            feature.Profil_kisitliligi = "z4"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "21":
            feature.Profil_kisitliligi = "z6"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "22":
            feature.Profil_kisitliligi = "Z1"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "23":
            feature.Profil_kisitliligi = "Z2"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "24":
            feature.Profil_kisitliligi = "Z3"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "25":
            feature.Profil_kisitliligi = "Z4"
            features.updateRow(feature)
        if feature.Profil_kisitliligi == "26":
            feature.Profil_kisitliligi = "Z6"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "1":
            feature.Tuz_sodyum = "a1"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "2":
            feature.Tuz_sodyum = "a2"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "3":
            feature.Tuz_sodyum = "a3"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "4":
            feature.Tuz_sodyum = "a6"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "5":
            feature.Tuz_sodyum = "a1A"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "6":
            feature.Tuz_sodyum = "a2A"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "7":
            feature.Tuz_sodyum = "a3A"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "8":
            feature.Tuz_sodyum = "a5A"
            features.updateRow(feature)
        if feature.Tuz_sodyum == "9":
            feature.Tuz_sodyum = "A"
            features.updateRow(feature)
        if feature.gecirgenlik == "1":
            feature.gecirgenlik = "p2"
            features.updateRow(feature)
        if feature.gecirgenlik == "2":
            feature.gecirgenlik = "p3"
            features.updateRow(feature)
        if feature.gecirgenlik == "3":
            feature.gecirgenlik = "hp2"
            features.updateRow(feature)
        if feature.gecirgenlik == "4":
            feature.gecirgenlik = "hp3"
            features.updateRow(feature)
        if feature.egim == "1":
            feature.egim = "g2"
            features.updateRow(feature)
        if feature.egim == "2":
            feature.egim = "g3"
            features.updateRow(feature)
        if feature.egim == "3":
            feature.egim = "g4"
            features.updateRow(feature)
        if feature.egim == "4":
            feature.egim = "g5"
            features.updateRow(feature)
        if feature.egim == "5":
            feature.egim = "g6"
            features.updateRow(feature)
        if feature.egim == "6":
            feature.egim = "j2"
            features.updateRow(feature)
        if feature.egim == "7":
            feature.egim = "j3"
            features.updateRow(feature)
        if feature.egim == "8":
            feature.egim = "j4"
            features.updateRow(feature)
        if feature.egim == "9":
            feature.egim = "j5"
            features.updateRow(feature)
        if feature.egim == "10":
            feature.egim = "j6"
            features.updateRow(feature)
        if feature.duzleme == "1":
            feature.duzleme = "u1"
            features.updateRow(feature)
        if feature.duzleme == "2":
            feature.duzleme = "u2"
            features.updateRow(feature)
        if feature.duzleme == "3":
            feature.duzleme = "u3"
            features.updateRow(feature)
        if feature.duzleme == "4":
            feature.duzleme = "u6"
            features.updateRow(feature)
        if feature.yuzey_tasi == "1":
            feature.yuzey_tasi = "r1"
            features.updateRow(feature)
        if feature.yuzey_tasi == "2":
            feature.yuzey_tasi = "r2"
            features.updateRow(feature)
        if feature.yuzey_tasi == "3":
            feature.yuzey_tasi = "r3"
            features.updateRow(feature)
        if feature.yuzey_tasi == "4":
            feature.yuzey_tasi = "r6"
            features.updateRow(feature)
        if feature.yuzey_tasi == "5":
            feature.yuzey_tasi = "R1"
            features.updateRow(feature)
        if feature.yuzey_tasi == "6":
            feature.yuzey_tasi = "R2"
            features.updateRow(feature)
        if feature.cali_agac == "1":
            feature.cali_agac = "c1"
            features.updateRow(feature)
        if feature.cali_agac == "2":
            feature.cali_agac = "c2"
            features.updateRow(feature)
        if feature.cali_agac == "3":
            feature.cali_agac = "c3"
            features.updateRow(feature)
        if feature.cali_agac == "4":
            feature.cali_agac = "c6"
            features.updateRow(feature)
        if feature.cali_agac == "5":
            feature.cali_agac = "ç1"
            features.updateRow(feature)
        if feature.cali_agac == "6":
            feature.cali_agac = "ç2"
            features.updateRow(feature)
        if feature.cali_agac == "7":
            feature.cali_agac = "ç3"
            features.updateRow(feature)
        if feature.cali_agac == "8":
            feature.cali_agac = "ç6"
            features.updateRow(feature)
        if feature.taban_suyu == "1":
            feature.taban_suyu = "w2"
            features.updateRow(feature)
        if feature.taban_suyu == "2":
            feature.taban_suyu = "w3"
            features.updateRow(feature)
        if feature.taban_suyu == "3":
            feature.taban_suyu = "w5"
            features.updateRow(feature)
        if feature.feyezan == "1":
            feature.feyezan = "f1"
            features.updateRow(feature)
        if feature.feyezan == "2":
            feature.feyezan = "f2"
            features.updateRow(feature)
        if feature.feyezan == "3":
            feature.feyezan = "f3"
            features.updateRow(feature)
        if feature.feyezan == "4":
            feature.feyezan = "f5"
            features.updateRow(feature)
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
