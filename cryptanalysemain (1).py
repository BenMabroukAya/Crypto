text = "WXMVA BIKSM ABCVM VAMUJ TMLMT WOQKQ MTAWX MVAWC ZKMXM ZUMBB IVBLM LMXTW GMZLM AQVNZ IABZC KBCZM ALMKT WCLKW UXCBQ VOQVN ZIABZ CKBCZ MMVBI VBYCM AMZDQ KMTIB MKPVW TWOQM XWAAM LMCVM IZKPQ BMKBC ZMUWL CTIQZ MKWUX WAMML MXTCA QMCZA XZWRM BAKWZ ZMTMA VWDIA EQNBO TIVKM MBKYC QXMZU MBBMV BLMKW VBZWT MZTMA LQNNM ZMVBM AZMAA WCZKM ALMAU IKPQV MADQZ BCMTT MABMT TMAYC MTIXC QAAIV KMLMK ITKCT TMABW KSIOM WCMVK WZMTM ZMAMI CTMXZ WRMBM ABXWZ BMXIZ TINWV LIBQW VWXMV ABIKS CVMWZ OIVQA IBQWV VWVKW UUMZK QITMY CQIXW CZJCB LMXZW UWCDW QZTMX ZWRMB WXMVA BIKSI QVAQY CMLMX ZWBMO MZMBL IQLMZ TMALM DMTWX XMCZA MBBWC BMTIK WUUCV ICBMW XMVAB IKSLM VWUJZ MCAMA MVBZM XZQAM AWVBZ MRWQV BTINW VLIBQ WVWXM VABIK SXIZU QKMTT MAKQW VZMBZ WCDMK IVWVQ KITZM LPIBA CAMMV WDIVK MIBBK QAKWL MTTPX QJUGI PWWWZ IKTMW ZIVOM KTWCL EIBBM UKDUE IZMQV BMTKM ABCVT WOQKQ MTTQJ ZMLQA BZQJC MAMTW VTMAB MZUMA LMTIT QKMVK MIXIK PM"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text2 = "ADLNEXDOYLSFYQQBZEYFOQRLLAKLOWLLESSQBZOGVFQDLRYIWFOUTPIGQDSOKIUPSZIZJUMGARGGWGFLSPIFXCBDOSPBIAIZKLZTYAEXUGQAUDIHZHHNFUXQGLRHMFQZHTQGKZCSOSMHBCZSQHHGBLADGKUHLCFYUQAVDGPDUFLCAQSAGLEPISXIZIQYUEDYOVIWEQVRDIOQGUOHEVIWMTSPDZQLEFGTGWWEDQHFHLNFHHOCUTDSOQFSEEHLRTLRQRWQGYEEWRGFJEEHHEAHCTMQQGCIDXXQZSEEXHXZLSCYHXOWUUWVMBJEPIFMZJUXPHEHVCWEJQCBEZGRDSSEDIVQOBLQTUAXLTQWWBCYTQTDDZHFARGMHPOZSSQBZTMGNGBLODKDZWZAFMRZBVNOSPYSYCUEOQEBIMTRGFIUFHHBFVMAYYAWYLQTUAXLTATHZGAAOODUBZICYHPSWRAXHSSYEFHDURLRXIVPSCEXSSBSBREIWFCBTQPDOCTMGRDGHLOBIQEHHCWHHZCTBDIXESZEZXUQDYIEIVABARQNRUBALMJRZRHTUSQADLNEXDOYWADQLOSSLQWFUCURQXUAICEOEQABPCMPUQROAFWXESLNAZDZQLAFXFUGJOPIOXVWINQBMVVOAVDOZLODEQSSJLAYGIOATQQFHADADILZHLLOIVFIULAKLOWLLXMEDSKIEXUUPBEEIOABSEEXHDALSPIOMZPCQRFQOWAOLH"


def calculeDelalphabet(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    cal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in text:
        cal[alphabet.index(i)] += 1
    return cal


def occ(text1):
    text = ""
    for i in text1:
        if i != " ":
            text += i
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(4, len(text), 7):
        c[alpha.index(text[i])] += 1

    n = 0
    ic = 0
    for i in range(len(c) - 1):
        n += c[i]
    for i in range(len(c) - 1):
        ic += (c[i] * (c[i] - 1)) / (n * (n - 1))
    return ic


def longeurdecle(text1):
    text1 = text1.replace(" ", "")
    x = 1
    while (True):
        nbchar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(text1), x):
            nbchar[alphabet.index(text1[i])] += 1
        n = 0
        for i in nbchar:
            n += i
        s = 0
        for i in range(len(nbchar)):
            s += (nbchar[i] * (nbchar[i] - 1)) / (n * (n - 1))
        if s > 0.06:
            return x
        else:
            x += 1


def dechiffavecCi(text, l):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    text = text.replace(" ", "")
    cal = []
    for j in range(l):
        x = []
        for i in range(26):
            x.append(0)
        cal.append(x)
    for j in range(l):
        for i in range(j, len(text), l):
            cal[j][alphabet.index(text[i])] += 1
    return cal


def cle(z):
    cle=""
    for i in range(len(z)):
        cle+=alphabet[z[i].index(max(z[i])) - 4]
    return cle


def vigener(txt,cle):
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
        txtclair += alphabet[pos]
        j += 1
        if j == lc:
            j = 0
    print(txtclair)


def dechiffrementCryptAnalyse(text):
    x = calculeDelalphabet(text)
    somme = 0
    for i in range(len(x) - 1):
        somme += x[i]
    l = longeurdecle(text)
    z = dechiffavecCi(text, l)
    cle1 = cle(z)
    return(vigener(text,cle1))

print(calculeDelalphabet("AYZLEVWQSASOKUZGHOQGUUGZODEDGHUEQWHQZLUPPJDOLTASNMPQFVLAOHSLEEPDECZIQJQOSUEMWDUVVOAQIVOSBEPRH"))

print(longeurdecle(text2))
print(dechiffrementCryptAnalyse("ADLNE XDOYL SFYQQ BZEYF OQRLL AKLOW LLESS QBZOG VFQDL RYIWF OUTPI GQDSO KIUPS ZIZJU MGARG GWGFL SPIFX CBDOS PBIAI ZKLZT YAEXU GQAUD IHZHH NFUXQ GLRHM FQZHT QGKZC SOSMH BCZSQ HHGBL ADGKU HLCFY UQAVD GPDUF LCAQS AGLEP ISXIZ IQYUE DYOVI WEQVR DIOQG UOHEV IWMTS PDZQL EFGTG WWEDQ HFHLN FHHOC UTDSO QFSEE HLRTL RQRWQ GYEEW RGFJE EHHEA HCTMQ QGCID XXQZS EEXHX ZLSCY HXOWU UWVMB JEPIF MZJUX PHEHV CWEJQ CBEZG RDSSE DIVQO BLQTU AXLTQ WWBCY TQTDD ZHFAR GMHPO ZSSQB ZTMGN GBLOD KDZWZ AFMRZ BVNOS PYSYC UEOQE BIMTR GFIUF HHBFV MAYYA WYLQT UAXLT ATHZG AAOOD UBZIC YHPSW RAXHS SYEFH DURLR XIVPS CEXSS BSBRE IWFCB TQPDO CTMGR DGHLO BIQEH HCWHH ZCTBD IXESZ EZXUQ DYIEI VABAR QNRUB ALMJR ZRHTU SQADL NEXDO YWADQ LOSSL QWFUC URQXU AICEO EQABP CMPUQ ROAFW XESLN AZDZQ LAFXF UGJOP IOXVW INQBM VVOAV DOZLO DEQSS JLAYG IOATQ QFHAD ADILZ HLLOI VFIUL AKLOW LLXME DSKIE XUUPB EEIOA BSEEX HDALS PIOMZ PCQRF QOWAO LH"))