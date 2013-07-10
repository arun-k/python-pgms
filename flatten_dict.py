def flatten_dict(dic, key="", result=None):
    if result is None:
        result = {}

    for keys in dic:
        if isinstance(dic[keys], dict):
            flatten_dict(dic[keys], keys+".", result)
        else:
            result[key+keys]=dic[keys]

    return result
