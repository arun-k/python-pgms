def group(List,size):
    grp_list=[]
    for i in range(0,len(List),size):
        grp_list.append(List[i:i+size])
    return grp_list
