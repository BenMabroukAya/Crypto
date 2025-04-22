#!usr/bin/python3
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def affine (text,a,b):
	text=text.upper().replace(" ","")
	chiff=""
	for i in text:
		chiff+=alphabet[((alphabet.index(i)*a)+b)%26]
	return chiff
def  aprime(a):
	x=1
	while ((a*x)%26) !=1:
		x+=2
		if x==13:
			x=15
	return x
def Dechiffre(text,a,b):
	ap=aprime(a)
	text=text.upper().replace(" ","")
	chiff=""
	for i in text:
		chiff+=alphabet[((alphabet.index(i)-b)*ap)%26]
	return chiff.lower()
def formater (text,chiff=1):
	if chiff==1:
		text=text.upper()
	else:
		text=text.lower()
	chaine=""
	for i in range(len(text)):
		if i%5==0 and i!=0:
			chaine+=" "
		chaine+=text[i]
	return chaine
ch=affine("deux entiers",7,16)
print(ch)
c=Dechiffre("LSAVSDTUSFM",7,16)
print(formater(c))
	
