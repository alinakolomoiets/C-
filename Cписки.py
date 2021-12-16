slovo="play in game"
slovo_1=list(slovo)
print(slovo,slovo_1)
while True:
	print("1-Razbieniye stroki po razdelitelu")
	print("2-Sostoit li stroka iz tsifr:")
	print("3-Sostoit li stroka iz simvolov v niznem registre:")
	print("4-Sostoit li stroka iz simvolov v verhnem registre: ")
	print("5-Preobrazovanie stroki k verhnemu registru:")
	print("6-Preobrazovanie stroki k niznemu registru:")
	print("7-Perevesti perviy simvol v verhniy registr , a vse ostalniye v nizniy")
	print("8-Perevesti perviye bukvi kazdogo slova v verhniy registr , a vse ostalniye v nizniy ")
	print("9-Vernut otsentrovannuyu stroku, po krayam kotoroy stoit simvol * ")	
	print("10-S.rpartition(sep)")
	try:
		a=int(input())
		if a==1:
			print(slovo.split())
			print(slovo)
			print()
		elif a==2:
			if slovo.isdigit():
				print("Da sostoit")
			else :
				print("Ne sostoit")
		elif a==3:
			if slovo.islower():
				print("Sostoit")
			else:
				print("Ne sostoit")
		elif a==4:
			if slovo.islower():
				print("Sostoit")
			else:
				print("Ne sostoit")
		elif a==5:
			print(slovo.upper())
		elif a==6:
			print(slovo.lower())
		elif a==7:
			print(slovo.capitalize())
		elif a==8:
			print(slovo.title())
		elif a==9:
			print(slovo.center(14,"*"))
		elif a==10:
			print(slovo.partition("in"))
	except:
		ValueError
		print("Ne to chislo ")
		print()
	
