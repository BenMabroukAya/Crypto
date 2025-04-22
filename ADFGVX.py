def cryptage_adfgvx(cle,text):
    cle2="ADFGVX"
    ch=""
    for i in text:
        pos=cle.index(i)
        ch += cle2[int(pos/6)]
        ch+=cle2[pos%6]
    return ch
def cryptage_adfgvx2(cle,text):
    dif=len(text)%len(cle)
    if dif!=0:
        for i in range (len(cle)-dif):
            text+="x"
    tab=[]
    for i in range (len(cle)):
        tab.append("")
    for i in range (len(cle)):
        for j in range(i,len(text),len(cle)):
            tab[i]+=text[j]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    chiffrer=""
    for i in alphabet:
        if i in cle :
            chiffrer+=tab[cle.index(i)]
    return chiffrer

def dechiffrer(cle,text):
    text.lower()
    tab=[]
    for i in range (len(cle)):
        tab.append("")
    for i in range (len(cle)):
        tab[i]=text[i*len(text)//len(cle):len(text)//len(cle)+i*len(text)//len(cle)]
    clo=sorted(list(cle))
    ch=""
    chaine=""
    tab2=[]
    for i in range (len(cle)):
        tab2.append("")
    for i in cle:
        tab2[cle.index(i)]+=tab[clo.index(i)]
        clo[clo.index(i)]
        cle=cle.replace()
    print(tab2)

print(cryptage_adfgvx("c10fwjymt5b4i7a28sp3oqhxkeul6dvrgzn9","cestunprincipedittomogrammiquecestadireunregroupementdecaractere"))
print(cryptage_adfgvx2("ingessat",cryptage_adfgvx("c10fwjymt5b4i7a28sp3oqhxkeul6dvrgzn9","cestunprincipedittomogrammiquecestadireunregroupementdecaractere")))
print(cryptage_adfgvx("c10fwjymt5b4i7a28sp3oqhxkeul6dvrgzn9","lespyramidesdegyptedetouslesvestigesmonumentauxquenousontlegueslesegyptiensdelantiquiteetnotammentlestroisgrandespyramidesdegizehsontalafoislesplusimpressionnantesetlesplusemblematiquesdecettecivilisation"))
print(cryptage_adfgvx2("ingessat",cryptage_adfgvx("c10fwjymt5b4i7a28sp3oqhxkeul6dvrgzn9","lespyramidesdegyptedetouslesvestigesmonumentauxquenousontlegueslesegyptiensdelantiquiteetnotammentlestroisgrandespyramidesdegizehsontalafoislesplusimpressionnantesetlesplusemblematiquesdecettecivilisation")))
print(dechiffrer("ingessat","GDFDVVFDFVDGGXXVXFVXVVDVVGXVXVVVXFFGFVGXVFFVDVAVFFXDDXDFFGDFFDFDXGDXAVGAFVDFFXVADXAXFFDFAXVDGGDDGXFAAAVXVVDDVVXGVVVFVVFGXVFDXDDDFXGDFFFFGVVGFXVVVDDGVDFFFVDFVGVFXFDDFVVDVVDVVDFDFXFFFFFVXGDAVVDFXDDGVVFFVAVDGAAXADXAADDFFFFFDADDFAFFVXAFXFDFVFGGGDXVFFADDAXDAGFFFVXVGVFVXXGXGVFVDFFGVGDVXXVDFVXGVFFFXFFFVVDFVVDXFGADXAXFXFXFFGFVFGFAXVFDFDDFDDDXDDVFXAADFVDXXGFDADAFV"))
print(dechiffrer("ingessat",dechiffrer("GDFDVVFDFVDGGXXVXFVXVVDVVGXVXVVVXFFGFVGXVFFVDVAVFFXDDXDFFGDFFDFDXGDXAVGAFVDFFXVADXAXFFDFAXVDGGDDGXFAAAVXVVDDVVXGVVVFVVFGXVFDXDDDFXGDFFFFGVVGFXVVVDDGVDFFFVDFVGVFXFDDFVVDVVDVVDFDFXFFFFFVXGDAVVDFXDDGVVFFVAVDGAAXADXAADDFFFFFDADDFAFFVXAFXFDFVFGGGDXVFFADDAXDAGFFFVXVGVFVXXGXGVFVDFFGVGDVXXVDFVXGVFFFXFFFVVDFVVDXFGADXAXFXFXFFGFVFGFAXVFDFDDFDDDXDDVFXAADFVDXXGFDADAFV")))

