def vowel_count(s):
    dic = {}
    for i in "aeiou":
        dic[i] = s.count(i)
    return dic
