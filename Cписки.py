#Kmd=[]#tühi järjenid(пустой список)
#Km=10 #esimine päev
#print("1.päeval pikkus oli",Km)
#Kmd.append(Km)
#print(Kmd)
#for p in range(2,8):
#	Km*=1.1 #>10%
#	Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11)+1)
#Kmd.remove(10) #Если pop то 0
#print(Kmd,"listis on kokku",Kmd.count(16.11),"elemendid mis võrdub 16.11")
#print(len(Kmd),"on jäänud listis")
#Задание 3: Бесполезные числа
#len, max



#Задание 2: Перемена мест
from random import*
from keyboard import*
spisok=[]
N=int(input("N"))#>2
for i in range(N):
	spisok.append(randint(1,100))
print(spisok)
max_=max(spisok)
print(max_)
max_2=max(spisok)/len(spisok)
print(max_2)
a=spisok.index(max_)
spisok.pop(a)
spisok.insert(a,max_2)
print(spisok)
#for s in spisok:
#	print(s)
#pervyi=spisok[0]
#posledni=spisok[N-1]#-1 последний элемент
#spisok.pop(0)
#spisok.insert(0,posledni)
#spisok.remove(posledni)#?
#spisok.append(pervyi)

#max_number=max(spisok)
#b=print("chislo",max_number)
#i=len(spisok)
#a=b/i

#spisok_c=spisok.copy()
#spisok_c.reverse()
#print(spisok_c)
#len(spisok)%2==0








#Задание 1: Почтовый индекс
Maakonnad=["Tallinn","Narva,Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa,Jõgevamaa","Tartu linn","Tartumaa,Põlvamaa,Võrumaa,Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while 1:
	try:
		Index=int(input("Index"))
		if len(str(Index))==5:
			break
	except ValueError:
		print("Valesti sisestatud index!")
i_list=list(str(Index))
print(Index)
print(i_list)
i_list[0]
s1=int(str(i_list[0]))#1->0,2->1.....
print(Maakonnad[s1-1])
if s1 in[1,2,3] :
	print("Jätke kodus!")
else:
	print("Kanna maski!")