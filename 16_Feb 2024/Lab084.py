# Dictonary example

phone_book = {"Batman": 987654321, "Superman": 123456789, "Wonder": 987654321}
print(len(phone_book))
print(phone_book["Batman"])

phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get('GB'))
print(phone_book2.get('GB'))

Karuna_details = dict(name='karuna', age=34, isFemale=True, Address='PB')
Karuna_details1 = {"name": "karuna", "age": "34", "isFemale": True, "Address": "PB"}
print(Karuna_details1.get("age"))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(len(my_dict))
print(my_dict)
