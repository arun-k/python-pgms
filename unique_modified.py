def unique(List,key):
    unique_list=[]
    for i in range(len(List)):
        List[i]=key(List[i])
    for ele in List:
        if ele in unique_list:
            pass

        else:
            unique_list.append(ele)
    return unique_list
