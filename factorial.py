def product(List):
    pdt=1
    for ele in List:
        pdt=pdt*ele
    return pdt

def factorial(num):
    if num==0:
        return 1
    return product(range(1,num+1))
