def unique_set(List,key):
    for i in range(len(List)):
        List[i]=key(List[i])
    return set(List)
