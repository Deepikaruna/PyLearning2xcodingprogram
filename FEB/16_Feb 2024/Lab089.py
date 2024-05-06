api_response = {
    "first_name": "Deepika",
    "age": 34,
    "last_name": "kr",
    "email": "deepika@live.com",
    "password": "Test@123",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))

api_response['password'] = "Deepika"
print(api_response)


for key, value in api_response.items():
    print(key," = >",  value)