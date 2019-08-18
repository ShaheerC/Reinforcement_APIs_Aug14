import requests
import json

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
body = ottawa_wards_response.json()

# print(body)

for i in range (len(body['objects'])):
    print(body['objects'][i]['name'])

print('----------')

candidates_response = requests.get("https://represent.opennorth.ca/candidates/")
candidates_body = candidates_response.json()

# print(candidates_body)

for x in range (len(candidates_body['objects'])):
    print(candidates_body['objects'][x]['party_name'])

print('----------')
