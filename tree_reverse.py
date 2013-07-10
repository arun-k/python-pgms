def tree_reverse(List):
    result=[]
    for i in range(len(List),0,-1):
        ele=List[i-1]
        if isinstance(ele, list):
            result.append(tree_reverse(ele))
        else:
            result.append(ele)

    return result
