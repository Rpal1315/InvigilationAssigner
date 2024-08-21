def list_dict_search(lst, key, value):
    for d in lst:
        if d[key] == value:
            return d
        
def abbreviate(name):
    out = []
    name_l = name.split()
    for i in name_l:
        out.append(i[0].upper())

    return "".join(out)
