def anagram(List):
    d={}
    for word in List:
	key="".join(sorted(word))
        d[key]=d.get(key,[])
        d[key].append(word)
    return d.values()
