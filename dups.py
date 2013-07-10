def dups(List):
    dups_list=[]
    for ele,i in zip(List,range(len(List))):
        if ele not in dups_list and ele in List[:i] or ele in List[i+1:]:
            dups_list.append(ele)
    return dups_list
