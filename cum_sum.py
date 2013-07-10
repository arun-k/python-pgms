def cumulative_sum(List):
    cum_sum_list=[]
    for i in range(1,len(List)+1):
        cum_sum_list.append(sum(List[:i]))
    return cum_sum_list
