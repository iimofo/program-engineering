def remove_first_occurrence(tpl, element):
    data_list = list(tpl)
    
    try:
        index_to_remove = data_list.index(element)
        data_list.pop(index_to_remove)
        return tuple(data_list)
    
    except ValueError:
        return tpl

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
