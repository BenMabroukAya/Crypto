#!/usr/bin/python3
def constH(cle):
	cle=cle.upper()
	alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alphaT=cle+alpha
	alpha2=""
	for i in alphaT:
		if i in alpha:
			alpha2+=i
			alpha=alpha.replace(i,"#")
	return alpha2


print(constH("MohamedNasr"))
