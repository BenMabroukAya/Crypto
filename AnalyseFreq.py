from pprint import pprint
def calculeDelalphabet(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
    cal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    text2 = ""
    for i in text:
        cal[alphabet.index(i)] += 1
    return cal
    
def occ(text1):
	text=""
	for i in text1:
		if i!=" ":
			text+=i
	alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for i in range(4,len(text),7):
		c[alpha.index(text[i])]+=1
	n=0
	ic=0
	for i in range(len(c)-1):
		n+=c[i]
	for i in range (len(c)-1):
		ic+=(c[i]*(c[i]-1))/(n*(n-1))
	return ic

def dechiffre(text):
	alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	alpha2="STUVWXYZABCDEFGHIJKLMNOPQR "
	clair=""
	for i in text:
		clair+=alpha2[alpha.index(i)]
	return clair
	
	
def dechiffreAvecIndiceCoin1(text):
	alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	text=text.replace(" ","")
	c=[]
	
	for i in range(7):
		x=[]
		for i in range(26):
			x.append(0)
		c.append(x)
	for j in range(7):
		for i in range(j,len(text),7):
			c[j][alpha.index(text[i])]+=1
	return c
	for i in range (len(cal)):
		print(alphabet[cal[i.index(i.max())-4]

def longCle(text):
	text=text.replace(" ","")
	x=1
	while(True):
		nbChar=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		for i in range(0,len(text),x):
			nbChar[alphabet.index(i)]+=1
		n=0
		for i in nbChar:
			n+=i
		s=0
		for i in range(len(nbChar)):
			s+=(nbChar[i]*(nbChar[i]-1))/(n*(n-1))
		if s>0.06:
			return x
		else:
			x+=1
		
def dechiffavecIndiceCoin2(text):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
	z=dechiffreIndiceCoin1(text)
	for i in alphabet:
    		print(i, end='\t')
		print()
		for i in z:
    			for j in range(26):
				print(i[j], end="\t")
				print()
		for i in range(len(z)):
    				print(alphabet[z[i].index(max(z[i])) - 4])


def vigener(txt, cle):
	global alphabet
	txt = txt.replace(" ", "")
	lt = len(txt)
	lc = len(cle)
	txtclair = ""
	j = 0;
	for i in range(lt):
		poschartxt = alphabet.index(txt[i])
		poscharcle = alphabet.index(cle[j])
		pos = (poschartxt - poscharcle) % 26
		print(pos)
		txtclair += alphabet[pos]
		j += 1
        	if j == lc:
			j = 0
		print(txtclair)

vigener("ADLNEXDOYLSFYQQBZEYFOQRLLAKLOWLLESSQBZOGVFQDLRYIWFOUTPIGQDSOKIUPSZIZJUMGARGGWGFLSPIFXCBDOSPBIAIZKLZTYAEXUGQAUDIHZHHNFUXQGLRHMFQZHTQGKZCSOSMHBCZSQHHGBLADGKUHLCFYUQAVDGPDUFLCAQSAGLEPISXIZIQYUEDYOVIWEQVRDIOQGUOHEVIWMTSPDZQLEFGTGWWEDQHFHLNFHHOCUTDSOQFSEEHLRTLRQRWQGYEEWRGFJEEHHEAHCTMQQGCIDXXQZSEEXHXZLSCYHXOWUUWVMBJEPIFMZJUXPHEHVCWEJQCBEZGRDSSEDIVQOBLQTUAXLTQWWBCYTQTDDZHFARGMHPOZSSQBZTMGNGBLODKDZWZAFMRZBVNOSPYSYCUEOQEBIMTRGFIUFHHBFVMAYYAWYLQTUAXLTATHZGAAOODUBZICYHPSWRAXHSSYEFHDURLRXIVPSCEXSSBSBREIWFCBTQPDOCTMGRDGHLOBIQEHHCWHHZCTBDIXESZEZXUQDYIEIVABARQNRUBALMJRZRHTUSQADLNEXDOYWADQLOSSLQWFUCURQXUAICEOEQABPCMPUQROAFWXESLNAZDZQLAFXFUGJOPIOXVWINQBMVVOAVDOZLODEQSSJLAYGIOATQQFHADADILZHLLOIVFIULAKLOWLLXMEDSKIEXUUPBEEIOABSEEXHDALSPIOMZPCQRFQOWAOLH", "MOHAMED")

print(occ1("ADLNE XDOYL SFYQQ BZEYF OQRLL AKLOW LLESS QBZOG VFQDL RYIWF OUTPI GQDSO KIUPS ZIZJU MGARG GWGFL SPIFX CBDOS PBIAI ZKLZT YAEXU GQAUD IHZHH NFUXQ GLRHM FQZHT QGKZC SOSMH BCZSQ HHGBL ADGKU HLCFY UQAVD GPDUF LCAQS AGLEP ISXIZ IQYUE DYOVI WEQVR DIOQG UOHEV IWMTS PDZQL EFGTG WWEDQ HFHLN FHHOC UTDSO QFSEE HLRTL RQRWQ GYEEW RGFJE EHHEA HCTMQ QGCID XXQZS EEXHX ZLSCY HXOWU UWVMB JEPIF MZJUX PHEHV CWEJQ CBEZG RDSSE DIVQO BLQTU AXLTQ WWBCY TQTDD ZHFAR GMHPO ZSSQB ZTMGN GBLOD KDZWZ AFMRZ BVNOS PYSYC UEOQE BIMTR GFIUF HHBFV MAYYA WYLQT UAXLT ATHZG AAOOD UBZIC YHPSW RAXHS SYEFH DURLR XIVPS CEXSS BSBRE IWFCB TQPDO CTMGR DGHLO BIQEH HCWHH ZCTBD IXESZ EZXUQ DYIEI VABAR QNRUB ALMJR ZRHTU SQADL NEXDO YWADQ LOSSL QWFUC URQXU AICEO EQABP CMPUQ ROAFW XESLN AZDZQ LAFXF UGJOP IOXVW INQBM VVOAV DOZLO DEQSS JLAYG IOATQ QFHAD ADILZ HLLOI VFIUL AKLOW LLXME DSKIE XUUPB EEIOA BSEEX HDALS PIOMZ PCQRF QOWAO LH"))
