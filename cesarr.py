alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def calculeDelalphabet(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
    cal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    text2 = ""
    for i in text:
        cal[alphabet.index(i)] += 1
    return cal

text = "WXMVA BIKSM ABCVM VAMUJ TMLMT WOQKQ MTAWX MVAWC ZKMXM ZUMBB IVBLM LMXTW GMZLM AQVNZ IABZC KBCZM ALMKT WCLKW UXCBQ VOQVN ZIABZ CKBCZ MMVBI VBYCM AMZDQ KMTIB MKPVW TWOQM XWAAM LMCVM IZKPQ BMKBC ZMUWL CTIQZ MKWUX WAMML MXTCA QMCZA XZWRM BAKWZ ZMTMA VWDIA EQNBO TIVKM MBKYC QXMZU MBBMV BLMKW VBZWT MZTMA LQNNM ZMVBM AZMAA WCZKM ALMAU IKPQV MADQZ BCMTT MABMT TMAYC MTIXC QAAIV KMLMK ITKCT TMABW KSIOM WCMVK WZMTM ZMAMI CTMXZ WRMBM ABXWZ BMXIZ TINWV LIBQW VWXMV ABIKS CVMWZ OIVQA IBQWV VWVKW UUMZK QITMY CQIXW CZJCB LMXZW UWCDW QZTMX ZWRMB WXMVA BIKSI QVAQY CMLMX ZWBMO MZMBL IQLMZ TMALM DMTWX XMCZA MBBWC BMTIK WUUCV ICBMW XMVAB IKSLM VWUJZ MCAMA MVBZM XZQAM AWVBZ MRWQV BTINW VLIBQ WVWXM VABIK SXIZU QKMTT MAKQW VZMBZ WCDMK IVWVQ KITZM LPIBA CAMMV WDIVK MIBBK QAKWL MTTPX QJUGI PWWWZ IKTMW ZIVOM KTWCL EIBBM UKDUE IZMQV BMTKM ABCVT WOQKQ MTTQJ ZMLQA BZQJC MAMTW VTMAB MZUMA LMTIT QKMVK MIXIK PM"
# x=calculeDelalphabet(text)
# for i in range(len(alphabet)):
#   print (alphabet[i]+" = "+str(x[i]))
somme = 0

# for i in range(len(x)-1):
#    somme+=x[i]
# print(somme)
def dechiff(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
    #cal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    text2 = ""
    #for i in text:
       # cal[alphabet.index(i)] += 1
    for i in text:
        text2 += alphabet2[alphabet.index(i)]
    return text2

# print(dechiff(text))
def indiceCoin(x):
    n = 742
    s = 0
    for i in range(len(x) - 1):
        s += (x[i] * (x[i] - 1)) / (n * (n - 1))
    return s

# print(indiceCoin(x))
text2 = "ADLNEXDOYLSFYQQBZEYFOQRLLAKLOWLLESSQBZOGVFQDLRYIWFOUTPIGQDSOKIUPSZIZJUMGARGGWGFLSPIFXCBDOSPBIAIZKLZTYAEXUGQAUDIHZHHNFUXQGLRHMFQZHTQGKZCSOSMHBCZSQHHGBLADGKUHLCFYUQAVDGPDUFLCAQSAGLEPISXIZIQYUEDYOVIWEQVRDIOQGUOHEVIWMTSPDZQLEFGTGWWEDQHFHLNFHHOCUTDSOQFSEEHLRTLRQRWQGYEEWRGFJEEHHEAHCTMQQGCIDXXQZSEEXHXZLSCYHXOWUUWVMBJEPIFMZJUXPHEHVCWEJQCBEZGRDSSEDIVQOBLQTUAXLTQWWBCYTQTDDZHFARGMHPOZSSQBZTMGNGBLODKDZWZAFMRZBVNOSPYSYCUEOQEBIMTRGFIUFHHBFVMAYYAWYLQTUAXLTATHZGAAOODUBZICYHPSWRAXHSSYEFHDURLRXIVPSCEXSSBSBREIWFCBTQPDOCTMGRDGHLOBIQEHHCWHHZCTBDIXESZEZXUQDYIEIVABARQNRUBALMJRZRHTUSQADLNEXDOYWADQLOSSLQWFUCURQXUAICEOEQABPCMPUQROAFWXESLNAZDZQLAFXFUGJOPIOXVWINQBMVVOAVDOZLODEQSSJLAYGIOATQQFHADADILZHLLOIVFIULAKLOWLLXMEDSKIEXUUPBEEIOABSEEXHDALSPIOMZPCQRFQOWAOLH"

# y=calculeDelalphabet(text2)
# print(indiceCoin(y))
def dechiffavecCi(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    alphabet2 = "STUVWXYZABCDEFGHIJKLMNOPQR "
    cal = []
    for j in range(7):
        x = []
        for i in range(26):
            x.append(0)
        cal.append(x)
    text2 = ""
    for j in range(7):
        for i in range(j, len(text), 7):  # 2 3 4 5 6 7 8 9 10 ...
            cal[j][alphabet.index(text[i])] += 1
    return cal

z = dechiffavecCi(text2)
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
    glo bal alphabet
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

vigener(text2, "MOHAMED")

