import sys
#character mapping problem
def char_mapping(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    maps = {}
    for i in range(len(s1)):
        if s1[i] in maps:
            if maps[s1[i]] != s2[i]:
                return False
        else:
            maps[s1[i]] = s2[i]
    return True
            
s1 = sys.argv[1]
s2 = sys.argv[2]

print(char_mapping(s1,s2))
