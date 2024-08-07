def list_dict_search(lst, key, value):
    for d in lst:
        if d[key] == value:
            return d