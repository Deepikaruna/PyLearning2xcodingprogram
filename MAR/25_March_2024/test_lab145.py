# API request - HTTP request

import pytest
import allure
import requests


@allure.title("Create booking CRUD")
@allure.description("TC#1 - Verify the create booking!")
@pytest.mark.crud
def test_create_booking_positive():
    pass
base_url="https://restful-booker.herokuapp.com"
base_path ="/booking"
URL = base_url+base_path
headers = {"Content-Type": "application/json"}
payload = {
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
response = requests.post(url=URL,headers=headers,json=payload)

# Response Verification

assert response.status_code == 200
print(response.headers)
response.json = response.json()
booking_id = response.json["bookingid"]
assert booking_id is not None
assert booking_id > 0
assert type(booking_id) == int
firstname = response.json["booking"]["firstname"]
checkin = response.json["booking"]["bookingdates"]["checkin"]
assert firstname == "Jim"
assert checkin == "2024-12-19"

@allure.title("Create booking CRUD")
@allure.description("TC#2 - Verify booking is not created with {} data!")
@pytest.mark.crud
def test_create_booking_negative():
    base_url="https://restful-booker.herokuapp.com"
    base_path ="/booking"
    URL="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL,headers=headers,json=payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

#Assertions
    assert response.status_code == 500


