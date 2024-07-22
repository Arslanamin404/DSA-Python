# GIVEN A LIST OF HETEROGENEOUS ELEMENTS. WRITE A PY SCRIPT TO REMOVE ALL THE NON INT VALUES FROM LIST

def remove_non_int(list):
    return [x for x in list if type(x) is int]


my_list = [1, 2, 1.5, 'admin', 8, 1.2]
non_int_list = remove_non_int(my_list)
print(non_int_list)
