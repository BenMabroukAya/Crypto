#!/usr/bin/python3
from pprint import pprint
def ChiffrerDechiffrer(cle,text):
	alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	alpha=["ABCDEFGHIJKLM","NOPQRSTUVWXYZ"]
	x=1
	al=""
	for j in range(12):
		for i in range(13):
			al+=alpha[1][((i+(13-x))%13)]
		alpha.append(al)
		al=""
		x+=1
	chiff=""
	for i in range(len(text)):
		c=cle[i%len(cle)]
		if alphabet.index(c)%2==0:
			 a=(alphabet.index(c)/2)+1
		else:
			 a=(alphabet.index(c)+1)/2

		if text[i] in alpha[0]:
			chiff+=alpha[int(a)][alpha[0].index(text[i])]
		else:
			chiff+=alpha[0][alpha[int(a)].index(text[i])]
	return chiff
p=ChiffrerDechiffrer("mednasr".upper(),"wgqyrjr".upper())
print(p)
