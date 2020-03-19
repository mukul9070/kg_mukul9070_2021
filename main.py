import sys
#one to one character mapping function
def char_mapping(s1, s2):
    # edge case to eliminate unequal lengths
    if len(s1) != len(s2):
        return False
    
    # mappings stored for checking later
    maps = {}
    for i in range(len(s1)):
        if s1[i] in maps:
            if maps[s1[i]] != s2[i]:
                return False # did not map
        else:
            maps[s1[i]] = s2[i]
    return True # no maps failed
            
s1 = sys.argv[1]
s2 = sys.argv[2]

print(char_mapping(s1,s2))
