request = int(input('Введите номер кабинета: ')) 

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
}

dictionary_for_missing = {
    None: {'key': 'None', 'access': 'False'},
}

if request in dictionary:
    response = dictionary[request]
else:
    response = dictionary_for_missing[None]

key = response.get('key')
access = response.get('access')
print(key)
print(access)