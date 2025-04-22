#!/usr/bin/python3
alphabet="abcdefghijklmnopqrstuvwxyz"
def getTransposition(cle):
	alphabet.lower()
	cle=cle.lower()
	ch=''
	for c in alphabet:
		for i in cle:
			if i==c:
				ch+=i
	tr=[]
	for i in  range (len(ch)):
		tr.append(ch.index(cle[i]))
		ch=ch.replace(cle[i],'#',1)
	return tr
	
def chiffrementTransposition(cle,chaine):
	listCle=getTransposition(cle)
	chaine=chaine.replace(" ","")
	textChiffre=""
	n=len(chaine)
	m=len(listCle)
	if n<m:
		for c in range (m-n):
			chaine+="x"
	else:
		for c in range(m-(n%m)):
			chaine+="x"
		print(chaine)
	liste=[(chaine[i:i+m]) for i in range(0,len(chaine),m)]
	print(liste)
	for k in liste:
		for i in listCle:
			textChiffre+=k[i].upper()
	return textChiffre
	
			
#print(getTransposition("cryptographie"))
print(chiffrementTransposition("transposition","salut les ingenieurs"))
	
