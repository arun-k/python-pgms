def treemap(fun,List):
    result=[]
    for ele in List:
        if isinstance(ele, list):
            result.append(treemap(fun,ele))
        else:
            result.append(fun(ele))

    return result
