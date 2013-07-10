def invertdict(dic):
    for key,value in dic.items():
        dic[value]=key
        del dic[key]
    return dic
