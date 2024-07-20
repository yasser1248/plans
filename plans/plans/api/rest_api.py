# import frappe
from uu import encode
import requests
import json
# from frappe import _
def new_api():
    base_url = "http://192.168.1.10:8100/"
    headers = {
    "Authorization": "token 93e1826d4d726ba:5b4e6294861134e",
    }
    doc_type = "CIB Loans"
    response = requests.get( f"{base_url}/api/v2/document/{doc_type}",headers=headers )

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: ", response.status_code , response.text )
new_api()