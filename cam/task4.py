def track_employee_entries(id_tuple, target_id):
    if target_id not in id_tuple:
        return ()

    try:
        first_index = id_tuple.index(target_id)
    except ValueError:
        return ()

    try:
        second_index = id_tuple.index(target_id, first_index + 1)
        return id_tuple[first_index:second_index + 1]

    except ValueError:
        return id_tuple[first_index:]


# Test Cases
print(track_employee_entries((1, 2, 3), 8))
print(track_employee_entries((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(track_employee_entries((1, 2, 8, 5, 1, 2, 9), 8))
print(track_employee_entries((1, 2, 3, 4, 5, 10), 10))