def reverse(List):
    for i in range(len(List)/2):
	List[i],List[-(i+1)]=List[-(i+1)],List[i]
    return List
