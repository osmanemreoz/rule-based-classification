###############################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
###############################

############
# İş Problemi
############

# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
# seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
# oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
# şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
# istemektedir.
# Örneğin:
# Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
# kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
# isteniyor


# Veri seti Hikayesi:

# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
# ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
# seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
# tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
# kullanıcı birden fazla alışveriş yapmış olabilir


# DEĞİŞKENLER:

# PRICE – Müşterinin harcama tutarı
# SOURCE – Müşterinin bağlandığı cihaz türü
# SEX – Müşterinin cinsiyeti
# COUNTRY – Müşterinin ülkesi
# AGE – Müşterinin yaşı

# Görev 1: Aşağıdaki soruları yanıtlayınız

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
# Soru 3: Kaç unique PRICE vardır?
# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
# Soru 7: SOURCE türlerine göre satış sayıları nedir?
# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir


# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?



# Görev 3: Çıktıyı PRICE'a göre sıralayınız.

# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde
# PRICE'a göre uygulayınız

# Çıktıyı agg_df olarak kaydediniz.



# Görev 4: İndekste yer alan isimleri değişkene çeviriniz.

# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.



# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.

# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'



# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.

# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based
# değişkenini oluşturmanız gerekmektedir.



# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.

# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz. (Segmentlere göre group by yapıp price mean,max,sum'larını alınız.)



# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir
# kazandırması beklenir?
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir
# kazandırması beklenir?


# GÖREV 1:

import pandas as pd
pd.set_option("display.max_rows", None)
# import numpy as np
# from matplotlib import pyplot as plt
df = pd.read_csv("1. Hafta Veri Bilimi için Python Programlama/Ödev/persona.csv")
df.head()
# df.describe()
# df.tail(5)
# df.columns
# df.index
# len(df)
# df.isnull()
# df.isnull().sum()
df.shape
# df.dtypes
df.info()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır?
df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Soru 7: SOURCE türlerine göre satış sayıları nedir?
# df.groupby("SOURCE").agg({"PRICE": "sum"})
df["SOURCE"].value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

# # Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})



# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()


# Görev 3: Çıktıyı PRICE'a göre sıralayınız.
#
# # Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde
# # PRICE'a göre uygulayınız
#
# # Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()



# Görev 4: İndekste yer alan isimleri değişkene çeviriniz.
#
# # Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# # Bu isimleri değişken isimlerine çeviriniz.

agg_df.index
agg_df = agg_df.reset_index()
agg_df.head()
# agg_df.set_index(["COUNTRY", "SOURCE", "SEX", "AGE"])



# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#
# # Age sayısal değişkenini kategorik değişkene çeviriniz.
# # Aralıkları ikna edici şekilde oluşturunuz.
# # Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'


# AGE değişkeninin bölüneceği aralıklar
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# bölünen aralıkların isimlendirilmeleri
mylabels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]

# AGE'i bölme işlemi
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
# agg_df["AGE"] = agg_df["AGE_CAT"]
agg_df.head()


# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
#
# # Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# # Yeni eklenecek değişkenin adı: customers_level_based
# # Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based
# # değişkenini oluşturmanız gerekmektedir.


# [agg_df["COUNTRY"][i] + "_".upper() + agg_df["SOURCE"][i] + "_".upper() + agg_df["SEX"][i] + "_".upper() + agg_df["AGE_CAT"][i] for i in agg_df.values]

# agg_df["customers_level_based"] = [agg_df["COUNTRY"][i] + "_".upper() + agg_df["SOURCE"][i] + "_".upper() + agg_df["SEX"][i] + "_".upper() + agg_df["AGE_CAT"][i] for i in agg_df.values]

# agg_df["customers_level_based"] = agg_df["COUNTRY"][0] + "_" + agg_df["SOURCE"][0] + "_" + agg_df["SEX"][0] + "_" + agg_df["AGE_CAT"][0]

# [i.upper() for i in agg_df["customers_level_based"]]


# değişken isimleri
agg_df.columns

for row in agg_df.values:
    print(row)

# gözlem değişkenlerine erişim (for döngüsüyle)
for row in agg_df.values:
    print(row[1])


# list comprehension ile COUNTRY, SOURCE, SEX, AGE_CAT değişkenlerinin değerlerinin isimlerini büyültüp
# yan yana koyup ve _ ile birleştirme işlemi
# burda row[0] country, row[1] source, row[2] sex, row[5] age_cat değişkenlerinin değerlerini temsil ediyor.
[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]


# veri setine ekleme işlemi
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()


# gereksiz değişkenleri çıkarma işlemi
agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))


# bir çok aynı segment var burada. bunları groupby yapıp price ortalamalarını aldıktan sonra
# segmentleri tekilleştirme işlemi
agg_df["customers_level_based"].value_counts()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df.head()

# customer_level_based index'te yer alıyor şuan. değişkene çevirme işlemi
agg_df = agg_df.reset_index()
agg_df.head()

# burada kontrol ettiğimizde segmentler tekilleşmiş olacak
agg_df["customers_level_based"].value_counts()
agg_df.head()





# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
#
# # Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# # Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# # Segmentleri betimleyiniz. (Segmentlere göre group by yapıp price mean,max,sum'larını alınız.)

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

agg_df.head(30)

agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})




# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
#
# # 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir
# # kazandırması beklenir?
# # 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir
# # kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
