time = input()
if(time!="GSW")and(time!="HOU")and(time!="CLE")and(time!="BOS"):
	print("Nenhum time de interesse jogando.")
else:
	nj = input()
	at = (int(input()))
	ac = (int(input()))
	at3 = (int(input()))
	ac3 = (int(input()))
	pt = ac*2 + ac3*3
	pc2 = ac/at
	pc3 = ac3/at3
	if(pt>30) or ((pc2>0.5) and (at>10)) or ((pc3 >0.4)and(at3>7)):
		print("O time", time, "estah jogando, e", nj ,"estah indo bem.")
	else:
		print("O time", time, "estah jogando, mas", nj,"nao estah indo bem.")
