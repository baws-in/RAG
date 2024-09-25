import re
font_set = set()

def chanakya901_to_unicode(str_input):
    array_one = [
        "aa", "a", "ZZ", "Z", "sas", "sa", "as", "sa", "Q+Z", "QZ+",
         "‘",'"',"’",'"',"“","'","”","'", "ƒ", "१", "„", "२",
        "…", "३", "†", "४", "‡", "५", "ˆ", "६", "‰", "७", "Š", "८",
        "‹", "९", "Œ", "०", "å", "०", "v‚", "ऑ", "vks", "ओ", "vkS", "औ",
        "vk", "आ", "v", "अ", "b±", "ईं", "Ã", "ई", "bZ", "ई", "b", "इ",
        "mQ", "ऊ", "m", "उ", "Å", "ऊ", ",s", "ऐ", ",", "ए", "½", "ऋ",
        "˝", "ऋ", "d+", "क़", "[+", "ख़्", "x+", "ग़", "T+", "ज़्", "t+", "ज़",
        "M+", "ड़", "<+", "ढ़", "¶+", "फ़्", "I+kQ", "फ़", "i+Q", "फ़", ";+", "य़",
        "j+", "ऱ", "u+", "ऩ", "d", "क", "D", "क्", "£", "र्f", "[", "ख्",
        "x", "ग", "X", "ग्", "Ä", "घ", "?", "घ्", "³", "ङ", "p", "च",
        "P", "च्", "N", "छ", "t", "ज", "T", "ज्", ">", "झ", "÷", "झ्",
        "Ö", "झ्", "¥", "ञ", "V", "ट", "B", "ठ", "M", "ड", "<", "ढ",
        ".", "ण्", "r", "त", "R", "त्", "F", "थ्", "n", "द", "/", "ध",
        "Ë", "ध्", "è", "ध्", "č", "ध्", "u", "न", "U", "न्", "IkQ", "फ",
        "iQ", "फ", "¶", "फ्", "i", "प", "I", "प्", "c", "ब", "C", "ब्",
        "Ò", "भ", "H", "भ्", "e", "म", "E", "म्", ";", "य", "¸", "य्",
        "Õ", "य्", "j", "र", "y", "ल", "Y", "ल्", "G", "ळ", "o+Q", "क़",
        "oQ", "क", "OkQ", "क", "Ok", "व", "o", "व", "O", "व्", "Üo", "श्व",
        "Üz", "श्र्", "Ü", "श्", "'", "श्", '"', "ष्", "l", "स", "L", "स्",
        "g", "ह", "Ń", "कृ", "Ñ", "कृ", "—", "कृ", "ô", "क्क", "äQ", "क्त",
        "ä", "त्त", "{", "क्ष्", "K", "ज्ञ", "ê", "ट्ट", "Í", "ट्ट", "ë", "ट्ठ",
        "Î", "ट्ठ", "ð", "ठ्ठ", "Ï", "ड्ड", "ì", "ड्ड", "ï", "ड्ढ", "Ô", "ड्ढ",
        "Ù", "त्त्", "Ú", "फ्र", "Ů", "त्त्", "=", "त्र्", "«", "त्र्", "–", "दृ",
        "Ì", "द्द", "í", "द्द", "Ľ", "द्ध", "¼", "द्ध", "˜", "द्भ", "ö", "द्भ",
        "|", "द्य", "}", "द्व", "é", "न्न", "™", "न्न्", "ó", "स्त्र", "â", "हृ",
        "à", "ह्न", "ã", "ह्म", "á", "ह्य", "º", "ह्", "J", "श्र", "Ø", "क्र",
        "Ř", "क्र", "Ý", "फ्", "æ", "द्र", "ç", "प्र", "Á", "प्र", "प्रQ", "फ्र",
        "व्रQ", "क्र", "#", "रु", ":", "रू", "Ó", "्य", "î", "्य", "z", "्र",
        "ª", "्र", "Ş", "्र", "È", "ीं", "Ê", "Zी", "›", "Zैं", "õ", "Zैं",
        "±", "Zं", "Æ", "र्f", "É", "र्Ż", "्k", "", "‚", "ॉ", "¨", "ो",
        "®", "ो", "ks", "ो", "©", "ौ", "kS", "ौ", "h", "ी", "q", "ु",
        "w", "ू", "`", "ृ", "s", "े", "¢", "े", "S", "ै", "a", "ं",
        "¡", "ँ", "ˇ", "ँ", "%", "ः", "W", "ॅ", "•", "ऽ", "∙", "ऽ",
        "·", "ऽ", "~", "्", "+", "़", "k", "ा", "A", "।", "ñ", "॰",
        "\\", "?", "^", "‘", "*", "’", "Þ", "“", "ß", "”", "μ", "-",
        "¿", "{", "À", "}", "¾", "=", "-", ".", "&", "-", "]", ",",
        "@", "/", " ः", " :", "अौ", "औ", "अो", "ओ", "आॅ", "ऑ", "आे", "ओ",
        "आै", "औ", "ाे", "ो", "ाॅ", "ॉ", "ाो", "ो"
    ]

    array_one_length = len(array_one)
    
    def replace_symbols(modified_substring):
        if modified_substring:
            modified_substring = re.sub(r'é', r'Â', modified_substring)
            modified_substring = re.sub(r'ÝQ', r'iQ', modified_substring)
            modified_substring = re.sub(r'Õk', r';', modified_substring)
            modified_substring = re.sub(r'([ ])([kzsSqwWa¡`±ZQ\+‚¨®sS©h¢ˇ%•∙·~ÈÊ\›õ])', r'\2', modified_substring)
            modified_substring = re.sub(r'([ZzsSqwa¡`]+)Q', r'Q\1', modified_substring)
            modified_substring = re.sub(r'([ZzsSqwa¡`]+)\+', r'+\1', modified_substring)
            modified_substring = re.sub(r'([ZzsSqwa¡`]+)ª', r'्र\1', modified_substring)

            for input_symbol_idx in range(0, array_one_length - 1, 2):
                modified_substring = modified_substring.replace(array_one[input_symbol_idx], array_one[input_symbol_idx + 1])

            modified_substring = modified_substring.replace('¯', 'Ż')
            modified_substring = modified_substring.replace('Ł', 'र्f')
            modified_substring = re.sub(r'([fŻ])([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])', r'\2\1', modified_substring)
            modified_substring = re.sub(r'([fŻ])((्[कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])+)', r'\2\1', modified_substring)
            modified_substring = modified_substring.replace('f', 'ि')
            modified_substring = modified_substring.replace('Ż', 'िं')

            modified_substring = modified_substring.replace('±', 'Zं')
            modified_substring = re.sub(r'([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ])([ािीुूृेैोौंँ]*)([Z])', r'\3\1\2', modified_substring)
            modified_substring = re.sub(r'(([कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहक़ख़ग़ज़ड़ढ़फ़य़ऱऩ][्])+)(Z)', r'\3\1', modified_substring)
            modified_substring = modified_substring.replace('Z', 'र्')

            modified_substring = re.sub(r'([ंँ॰])([ािीुूृेैोौ])', r'\2\1', modified_substring)
            modified_substring = re.sub(r'([ािीुूृेैोौंँ])([ािीुूृेैोौ])', r'\1', modified_substring)
            modified_substring = re.sub(r'([0-9])ण्', r'\1.', modified_substring)
            modified_substring = re.sub(r'ण्([0-9])', r'.\1', modified_substring)

        return modified_substring

    text_size = len(str_input)
    processed_text = ""
    sthiti1 = 0
    sthiti2 = 0
    max_text_size = 6000

    while sthiti2 < text_size:
        sthiti1 = sthiti2
        if sthiti2 < text_size - max_text_size:
            sthiti2 += max_text_size
            while str_input[sthiti2] not in ['\n', '\t', ' ']:
                sthiti2 -= 1
        else:
            sthiti2 = text_size

        modified_substring = str_input[sthiti1:sthiti2]
        processed_text += replace_symbols(modified_substring)

    return processed_text


def kruti2unicode(input_str: str) -> str:
    # Mapping of Krutidev characters to Unicode
    char_map = [
        ("aa", "a"), ("ZZ", "Z"), ("=kk", "=k"), ("f=k", "f="), ("Q+Z", "QZ+"),
        ("sas", "sa"), ("‘" ,	"\"" ), ("’", "\""), ("“", "'"), ("”", "'"),
        ("ƒ", "१"), ("„", "२"), ("…", "३"), ("†", "४"), ("‡", "५"),
        ("ˆ", "६"), ("‰", "७"), ("Š", "८"), ("‹", "९"), ("Œ", "०"),
        ("å", "०"), ("v‚", "ऑ"), ("vks", "ओ"), ("vkS", "औ"), ("vk", "आ"),
        ("v", "अ"), ("b±", "ईं"), ("Ã", "ई"), ("bZ", "ई"), ("b", "इ"),
        ("m", "उ"), ("Å", "ऊ"), (",s", "ऐ"), (",", "ए"), ("_", "ऋ"),
        ("d+", "क़"), ("[+", "ख़्"), ("x+", "ग़"), ("T+", "ज़्"), ("t+", "ज़"),
        ("M+", "ड़"), ("<+", "ढ़"), ("¶+", "फ़्"), ("Q+", "फ़"), (";+", "य़"),
        ("j+", "ऱ"), ("u+", "ऩ"), ("d", "क"), ("D", "क्"), ("£", "ख्र"),
        ("[", "ख्"), ("x", "ग"), ("X", "ग्"), ("Ä", "घ"), ("?", "घ्"),
        ("³", "ङ"), ("p", "च"), ("P", "च्"), ("N", "छ"), ("t", "ज"),
        ("T", "ज्"), (">", "झ"), ("÷", "झ्"), ("Ö", "झ्"), ("¥", "ञ"),
        ("V", "ट"), ("B", "ठ"), ("M", "ड"), ("<", "ढ"), (".", "ण्"),
        ("r", "त"), ("R", "त्"), ("F", "थ्"), ("n", "द"), ("/", "ध्"),
        ("Ë", "ध्"), ("è", "ध्"), ("u", "न"), ("U", "न्"), ("i", "प"),
        ("I", "प्"), ("Q", "फ"), ("¶", "फ्"), ("c", "ब"), ("C", "ब्"),
        ("Ò", "भ"), ("H", "भ्"), ("e", "म"), ("E", "म्"), (";", "य"),
        ("¸", "य्"), ("j", "र"), ("y", "ल"), ("Y", "ल्"), ("G", "ळ"),
        ("Üo", "श्व"), ("Ük", "श"), ("Üz", "श्र्"), ("o", "व"), ("O", "व्"),
        ("'", "श्"), ("\"", "ष्"), ("l", "स"), ("L", "स्"), ("g", "ह"),
        ("Ñ", "कृ"), ("—", "कृ"), ("ô", "क्क"), ("ä", "क्त"), ("{", "क्ष्"),
        ("K", "ज्ञ"), ("ê", "ट्ट"), ("Í", "ट्ट"), ("ë", "ट्ठ"), ("Î", "ट्ठ"),
        ("ð", "ठ्ठ"), ("Ï", "ड्ड"), ("ì", "ड्ड"), ("ï", "ड्ढ"), ("Ô", "ड्ढ"),
        ("Ù", "त्त्"), ("=", "त्र"), ("«", "त्र्"), ("–", "दृ"), ("Ì", "द्द"),
        ("í", "द्द"), ("\\)", "द्ध"), ("˜", "द्भ"), ("ö", "द्भ"), ("|", "द्य"),
        ("}", "द्व"), ("é", "न्न"), ("™", "न्न्"), ("ó", "स्त्र"), ("â", "हृ"),
        ("à", "ह्न"), ("ã", "ह्म"), ("á", "ह्य"), ("º", "ह्"), ("J", "श्र"),
        ("Ø", "क्र"), ("Ý", "फ्र"), ("æ", "द्र"), ("ç", "प्र"), ("Á", "प्र"),
        ("#", "रु"), (":", "रू"), ("Ó", "्य"), ("î", "्य"), ("z", "्र"),
        ("ª", "्र"), ("È", "ीं"), ("Ê", "Zी"), ("\\›", "Zैं"), ("õ", "Zैं"),
        ("±", "Zं"), ("Æ", "र्f"), ("É", "र्Ç"), ("्k", ""), ("‚", "ॉ"),
        ("¨", "ो"), ("®", "ो"), ("ks", "ो"), ("©", "ौ"), ("kS", "ौ"),
        ("h", "ी"), ("q", "ु"), ("w", "ू"), ("`", "ृ"), ("s", "े"),
        ("¢", "े"), ("S", "ै"), ("a", "ं"), ("¡", "ँ"), ("%", "ः"),
        ("W", "ॅ"), ("•", "ऽ"), ("·", "ऽ"), ("∙", "ऽ"), ("·", "ऽ"),
        ("~", "्"), ("+", "़"), ("k", "ा"), ("A", "।"), ("ñ", "॰"),
        ("\\\\", "?"), (" ः", " :"), ("^", "‘"), ("*", "’"), ("Þ", "“"),
        ("ß", "”"), ("(", ";"), ("¼", "("), ("½", ")"), ("¿", "{"),
        ("À", "}"), ("¾", "="), ("-", "."), ("&", "-"), ("]", ","),
        ("@", "/"), ("~ ", "् "), ("ाे", "ो"), ("ाॅ", "ॉ"), ("े्र", "्रे"),
        ("अौ", "औ"), ("अो", "ओ"), ("आॅ", "ऑ")
    ]


    def replace_symbols(modified_substring):
        for old, new in char_map:
            modified_substring = modified_substring.replace(old, new)
        # Adjusting position of i maatraas
        modified_substring = re.sub(r'([fÇ])([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])', r'\2\1', modified_substring)
        modified_substring = re.sub(r'([fÇ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])', r'\2\3\1', modified_substring)
        modified_substring = re.sub(r'([fÇ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])', r'\2\3\1', modified_substring)

        modified_substring = modified_substring.replace('f', 'ि')
        modified_substring = modified_substring.replace('Ç', 'िं')

        # Adjusting position of reph (half r)
        modified_substring = re.sub(r'([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])([ािीुूृेैोौंँ]*)([Z])', r'\3\1\2', modified_substring)
        modified_substring = re.sub(r'([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])([्])([Z])', r'\3\1\2', modified_substring)
        modified_substring = re.sub(r'([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक़ख़ग़ज़ड़ढ़फ़])([्])([Z])', r'\3\1\2', modified_substring)

        modified_substring = modified_substring.replace('Z', 'र्')

        # Remove maatras typed wrongly
        modified_substring = re.sub(r'([ंँ॰])([ािीुूृेैोौ])', r'\2\1', modified_substring)
        modified_substring = re.sub(r'([ािीुूृेैोौंँ])([ािीुूृेैोौ])', r'\1', modified_substring)

        return modified_substring

    # Process the input string in chunks
    max_chunk_size = 6000
    processed_text = ""
    for i in range(0, len(input_str), max_chunk_size):
        chunk = input_str[i:i+max_chunk_size]
        # Ensure chunk ends at a word boundary
        if i + max_chunk_size < len(input_str):
            chunk = chunk.rsplit(None, 1)[0]
        processed_text += replace_symbols(chunk)

    return processed_text


def chanakya905_to_unicode(input_str):
    array_one_905 = ["ñ", "॰", "Q+Z", "QZ+", "sas", "sa", "aa", "a", "¼Z", 
                     "र्द्ध", "ZZ", "Z", "å", "०", "ƒ", "१", "„", "२", "…", 
                     "३", "†", "४", "‡", "५", "ˆ", "६", "‰", "७", "Š", 
                     "८", "‹", "९", "¶+", "फ़्", "d+", "क़", "[+k", "ख़", 
                     "[+", "ख़्", "x+", "ग़", "T+", "ज़्", "t+", "ज़", "M+", 
                     "ड़", "<+", "ढ़", "Q+", "फ़", ";+", "य़", "j+", "ऱ", 
                     "u+", "ऩ", "Ùk", "त्त", "Ù", "त्त्", "ä", "क्त", "–", 
                     "दृ", "—", "कृ", "é", "न्न", "™", "न्न्", "=kk", "=k", 
                     "f=k", "f=", "à", "ह्न", "á", "ह्य", "â", "हृ", "ã", 
                     "ह्म", "ºz", "ह्र", "º", "ह्", "í", "द्द", "{k", "क्ष", 
                     "{", "क्ष्", "f=", "त्रि", "=k", "त्र", "«", "त्र्", "Nî", 
                     "छ्य", "Vî", "ट्य", "Bî", "ठ्य", "Mî", "ड्य", "<î", 
                     "ढ्य", "|", "द्य", "K", "ज्ञ", "}", "द्व", "J", "श्र", 
                     "Vª", "ट्र", "Mª", "ड्र", ">ª", "ढ्र", "Nª", "छ्र", 
                     "Ø", "क्र", "Ý", "फ्", "nzZ", "र्द्र", "æ", "द्र", "ç", 
                     "प्र", "Á", "प्र", "xz", "ग्र", "#", "रु", ":", "रू", 
                     "v‚", "ऑ", "vks", "ओ", "vkS", "औ", "vk", "आ", 
                     "v", "अ", "b±", "ईं", "Ã", "ई", "bZ", "ई", "b", 
                     "इ", "mQ", "ऊ", "m", "उ", "Å", "ऊ", ",s", "ऐ", 
                     ",", "ए", "½", "ऋ", "ô", "क्क", "d", "क", "Dk", 
                     "क", "D", "क्", "£", "र्f", "[k", "ख", "[", "ख्", 
                     "x", "ग", "Xk", "ग", "X", "ग्", "Ä", "घ", "?k", 
                     "घ", "?", "घ्", "³", "ङ", "p", "च", "Pk", "च", 
                     "P", "च्", "N", "छ", "”k", "ज", "”", "ज्", "t", 
                     "ज", "Tk", "ज", "T", "ज्", ">", "झ", "÷", "झ्", 
                     "¥", "ञ", "ê", "ट्ट", "ë", "ट्ठ", "V", "ट", "B", 
                     "ठ", "ì", "ड्ड", "ï", "ड्ढ", "M+", "ड़", "<+", "ढ़", 
                     "M", "ड", "<", "ढ", ".k", "ण", ".", "ण्", "r", 
                     "त", "Rk", "त", "R", "त्", "Fk", "थ", "F", "थ्", 
                     "n", "द", "/", "ध", "èk", "ध", "è", "ध्", "Ë", "ध्", 
                     "u", "न", "Uk", "न", "U", "न्", "iQ", "फ", "i", "प", 
                     "Ik", "प", "I", "प्", "\"", "ष्", "¶", "\"", "c", "ब", "Ck", "ब", 
                     "C", "ब्", "Hk", "भ", "H", "भ्", "e", "म", "Ek", "म", 
                     "E", "म्", ";", "य", "¸", "\"", "j", "र", "y", "ल", "Yk", 
                     "ल", "Y", "ल्", "G", "ळ", "oQ", "क", "o", "व", "Ok", "व", 
                     "O", "व्", "'k", "श", "'", "श्", "Ük", "श", "Ü", "श्", "\"k", 
                     "ष", "l", "स", "Lk", "स", "L", "स्", "g", "ह", 
                     "È", "ीं", "z", "्र", "Ì", "द्द", "Í", "ट्ट", "Î", "ट्ठ", "Ï", 
                     "ड्ड", "Ñ", "कृ", "Ò", "भ", "Ó", "्य", "Ô", "ड्ढ", "Ö", 
                     "झ्", "Ø", "क्र", "Ù", "त्त्", "¼", "द्ध", "Ú", "फ्र", "É", 
                     "ह्न", "Ů", "त्त्", "Ľ", "द्ध", "˝", "ऋ", "Ř", "क्र", "Ń", 
                     "कृ", "Q", "फ़", "č", "ध्", "Ş", "्र", "‚", "ॉ", "¨", 
                     "ो", "ks", "ो", "©", "ौ", "kS", "ौ", "k", "ा", "h", 
                     "ी", "q", "ु", "w", "ू", "`", "ृ", "s", "े", "¢", "े", 
                     "S", "ै", "a", "ं", "¡", "ँ", "ˇ", "ँ", "%", "ः", "W", 
                     "ॅ", "•", "ऽ", "·", "ऽ", "∙", "ऽ", "·", "ऽ", "+", "़", 
                     "\\", "?", "‘", "\"", "’", "\"", "“", "'", "^", "‘", 
                     "*", "’", "Þ", "“", "ß", "ह्र", "¾", "=", "&", "-", "μ", 
                     "-", "¿", "{", "À", "}", "A", "।", "Œ", "॰", "]", ",", 
                     "@", "/", "ः", ":", "~", "्", "्ा", "", "ाे", "ो", "ाॅ", 
                     "ॉ", "अौ", "औ", "अो", "ओ", "आॅ", "ऑ"]


    def chanakya905_replace_symbols(modified_substring, array_one, array_one_length):
            if modified_substring:
                modified_substring = re.sub(r'é', r'Â', modified_substring)
                modified_substring = re.sub(r'ÝQ', r'iQ', modified_substring)
                modified_substring = re.sub(r'Õk', r';', modified_substring)
                modified_substring = re.sub(r'([ZzsSqwa¡`]+)Q', r'Q\1', modified_substring)

                for input_symbol_idx in range(0, array_one_length - 1, 2):
                    idx = 0
                    while idx != -1:
                        #idx = modified_substring.find(array_one[input_symbol_idx])
                        #if idx != -1:
                        #    print(array_one[input_symbol_idx], array_one[input_symbol_idx + 1])
                        modified_substring = modified_substring.replace(array_one[input_symbol_idx], array_one[input_symbol_idx + 1])
                        idx = modified_substring.find(array_one[input_symbol_idx])
            

                # Additional replacements as per the original script
                replacements = [
                    (r'([ेैुूं]+)्र', r'्र\1'),
                    (r'ं([ाेैुू]+)', r'\1ं'),
                    (r'([ \n])ा', r'\1श'),
                    (r'¯', 'f'),
                    (r'Ł', 'र्f'),
                    (r'([fŻ])([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])', r'\2\1'),
                    (r'([fŻ])(्)([कखगघङचछजझञटठडड़ढढ़णतथदधनपफबभमयरलवशषसहक्ष])', r'\2\3\1'),
                    (r'f', 'ि'),
                    (r'Ż', 'िं'),
                    (r'±', 'Zं'),
                    (r'([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([ािीुूृेैोौंँ]*)([Z])', r'\3\1\2'),
                    (r'([कखगघचछजझटठडड़ढढ़णतथदधनपफबभमयरलळवशषसहक्षज्ञ])([्])([Z])', r'\3\1\2'),
                    (r'Z', 'र्')
                ]

                for pattern, replacement in replacements:
                    modified_substring = re.sub(pattern, replacement, modified_substring)

            return modified_substring

    array_one_length = len(array_one_905)
    modified_substring = input_str
    text_size = len(modified_substring)
    processed_text = ''

    sthiti1 = 0
    sthiti2 = 0
    chale_chalo = True
    chunk_size = 6000

    while chale_chalo:
        sthiti1 = sthiti2
        if sthiti2 < (text_size - chunk_size):
            sthiti2 += chunk_size
        else:
            sthiti2 = text_size
            chale_chalo = False

        modified_substring = input_str[sthiti1:sthiti2]
        modified_substring = chanakya905_replace_symbols(modified_substring, array_one_905, array_one_length)
        processed_text += modified_substring

    return processed_text

    
result = chanakya905_to_unicode("""vlÝQy""")

def legacy2unicode(str, font):
    font_set.add(font)
    if re.search("kruti", font, re.IGNORECASE):
        return kruti2unicode(str)
    elif re.search("chanakya901", font, re.IGNORECASE):
        return chanakya901_to_unicode(str)
    elif re.search("chanakya905", font, re.IGNORECASE):
        return chanakya905_to_unicode(str)
    elif re.search("chanakya902", font, re.IGNORECASE):
        return chanakya905_to_unicode(str)
    else:
        return str



