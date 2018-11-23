def invert_dict(map):
    inverse=dict()
    for item in map:
        val=map[item]
        if val in inverse:
            inverse[val].append(item)
        else:
            inverse[val]=[item]
    return inverse
    

origin_map={'a':1,'b':2,'c':1}
print(invert_dict(origin_map))