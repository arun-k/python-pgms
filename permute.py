def permute(lst):
    if len(lst)<2:
        return [lst]
    else:
        rslt=[]
        for i in range(len(lst)):
            lst[0],lst[i]=lst[i],lst[0]
            permu_lst=permute(lst[1:])
            rslt+=[[lst[0]]+ls for ls in permu_lst]
        return rslt
