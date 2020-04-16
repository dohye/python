"""
Label Error Rate(LER)
Reference : https://www.cs.toronto.edu/~graves/icml_2006.pdf
            https://lovit.github.io/nlp/2018/08/28/levenshtein_hangle/
"""

def LabelErrorRate(x,z, debug=False, jamo=False):
    
    if jamo:
        x, z = jamo_decompose(x), jamo_decompose(z)

    S = len(x)
    
    for i in range(len(x)):

        if jamo :
            ED = jamo_levenshtein(x[i], z[i])
        else:
            ED = levenshtein(x[i], z[i])
        
        mean_norm = sum(ED/len(z[i]))
        
        if debug : print("{}, {}, ED : {}".format(x[i] , z[i], ED))
    
    LER = mean_norm / S
    
    return LER
    
    
    
    # levenshtein
    def levenshtein(s1, s2, debug=False):
    
    if len(s1) < len(s2):
        return levenshtein(s2, s1, debug)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            current_row.append(min(insertions, deletions, substitutions))
            
        if debug:
            print(current_row[1:])
            
        previous_row = current_row
        
    return previous_row[-1]


# jamo_levenshtein

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',
                 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def decompose(c):
    i = ord(c)
    
    if c == ' ':
        return (' ')
    
    if (ord('ㄱ') <= i <= ord('ㅎ')):
        return (c, ' ', ' ')
    
    if (ord('ㅏ') <= i <= ord('ㅣ')):
        return (' ', c, ' ')
    
    # decomposition rule
    i -= ord('가') # 44032
    cho = i // 588
    jung = (i - cho * 588) // 28
    jong = (i - cho * 588 - jung * 28)
    
    return (chosung_list[cho], jungsung_list[jung], jongsung_list[jong])


def jamo_decompose(x,):
    x_ = list()
    
    for xi in range(len(x)):
        string = ''.join([comp for c in x[xi] for comp in decompose(c)])
        x_.append(string)
        
    return x_


def jamo_levenshtein(s1, s2):
    if len(s1) < len(s2):
        return jamo_levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)
    
    def get_jamo_cost(c1, c2):
        if c1 == c2:
            return 0
        jamo1 = decompose(c1)
        jamo2 = decompose(c2)
        if jamo1 is None or jamo2 is None:
            return 1
        return levenshtein(decompose(c1), decompose(c2)) / 3

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + get_jamo_cost(c1, c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]
