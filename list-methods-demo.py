from unittest import result


names=["Ali","Yağmur","Hakan","Deniz"]
years=[1998,2000,1998,1987]

# 1-Cenk ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)


# 2-Sena ismini listenin başına ekleyiniz
names[0]="Sena"
print(names)


# 3-Deniz ismin listeden siliniz
# names.remove("Deniz")
# print(names)


# 4-Deniz isminin indeksi nedir?
# indexs=names.index("Deniz")
# print(indexs)


# 5-Ali listenin bir elemanı mıdır?
result="Ali" in names

print(result)

# 6-Liste elemanlarını ters çevirin
names.reverse()
print(names)


# 7-Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)


# 8-years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)

# 9-str="Chevrolet","Dacia" karakter dizisini listeye çeviriniz
str="Chevrolet,Dacia"
print(str.split(","))


# 10-years dizisinin en büyük ve en küçük elemanı nedir?
min = min(years)
max = max(years)
print(min, max)

# 11-years dizisinde kaç tane 1998 değeri vardır?
sonuc=years.count(1998)
print(sonuc)

# 12-years dizisini tüm elemanlarını siliniz
cls=years.clear()
print(cls)


# 13-Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
brands=[]

brand=input("1.Marka Giriniz..")
brands.append(brand)

brand=input("2.Marka Giriniz..")
brands.append(brand)

brand=input("3.Marka Giriniz..")
brands.append(brand)
print(brands)
