def zip(List1,List2):
    return [(List1[i],List2[i]) for i in range(min(len(List1),len(List2)))]
