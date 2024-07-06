import requests

def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url,headers=headers,json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token

def create_booking():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2024-12-19",
            "checkout" :"2025-01-21"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

#Assertions
    assert response.status_code == 200
#Get the response body and verify  the JSON, Booking id is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

def test_put_request():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = URL = "/booking/"
    param = create_booking()
    PUT_URL = base_url+base_path+str(param)
    cookie ="token=" + create_token()
    headers = {
         "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(headers)