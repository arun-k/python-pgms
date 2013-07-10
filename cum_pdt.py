def product(List):
    pdt=1
    for ele in List:
        pdt=pdt*ele
    return pdt

def cumulative_product(List):
    cum_pdt_list=[]
    for i in range(1,len(List)+1):
        cum_pdt_list.append(product(List[:i]))
    return cum_pdt_list
