def unflatten_dict(dic):
    result={}
    for key in dic:
        mixed_key=key.split(".")
        if len(mixed_key)>1:
            result[mixed_key[0]]=result.get(mixed_key[0],{})
            result[mixed_key[0]][mixed_key[1]]=dic[key]
        else:
            result[key]=dic[key]
    return result
