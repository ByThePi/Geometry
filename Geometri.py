"""
authors : Salih Özsoy, Enes Soylu
Geometrik şekillerin alan ve çevrelerini hesaplayan program...

"""

import time
from math import pi

print("Geometrik AI v.1'e hos geldiniz!")

sekil = int(input("""
Programi kapatmak istiyorsaniz 1'i tiklayiniz,
Kare alan ve cevre hesaplamak istiyorsaniz 2'yi tiklayiniz,
Ucgen alan ve cevre hesaplamak istiyorsaniz 3'u tiklayiniz,
Dikdortgen alan ve cevre hesaplamak istiyorsaniz 4'u tiklayiniz,
Daire alan ve cevre hesaplamak istiyorsaniz 5'i tiklayiniz:"""))

def kare():
	print("Kare Alan ve Cevre Hesaplama")
	i = float(input("Kare'nin bir kenar uzunlugunu giriniz:"))#Kenar uzunluğu
	kareAlan = i*i
	kareCevre = i*4
	print("Alan:", kareAlan,"\n" "Cevre:", kareCevre)

def ucgen():
	print("Ucgen Alan ve Cevre Hesaplama")
	a = float(input("Birinci kenari giriniz:"))#Birinci Kenar
	b = float(input("Ikinci kenari giriniz:"))#İkinci Kenar
	c = float(input("Ucuncu kenari giriniz:"))#Üçüncü Kenar
	u = (a+b+c)/2
	ucgenAlan = (u*(u-a)*(u-b)*(u-c))**1/2
	ucgenCevre = (a+b+c)
	print("Alan:", ucgenAlan,"\n" "Cevre:", ucgenCevre)
	
def dikdortgen():
	print("Dikdortgen Alan ve Cevre Hesaplama")
	a = float(input("Ilk kenari giriniz:")) #Ilk Kenar
	b = float(input("Ikinci kenari giriniz")) #Ikinci Kenar
	dikdortgenAlan = a*b
	dikdortgenCevre = (a+b)*2
	print("Alan:", dikdortgenAlan,"\n" "Cevre:", dikdortgenCevre)

def daire():
	r = float(input ("Dairenin yaricapini giriniz: "))
	print("Dairenin alani:" + str(pi * r**2))
	print("Dairenin cevresi:" + str(2 * pi * r))


while (True):
	if sekil == 1:
		break
	elif sekil == 2:
		kare()
		break
	elif sekil == 3:
		ucgen()
		break
	elif sekil == 4:
		dikdortgen()
		break
	elif sekil == 5:
		daire()
		break

time.sleep(15)
print("Uygulamamizi kullandiginiz icin tesekkurler!")
print("Uygulama kapatiliyor...")
time.sleep(10)