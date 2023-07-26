import requests
import json

access_token = 'ZTEzMTNhYzAtODQ4Zi00Mzc2LTg3NWUtNjM4ZmE2ZjQ0NjEzMWU3ZThhZTAtYzRm_P0A1_c9a3c616-b39c-460f-b134-dd9f31b56890'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmY2OGQxNTAtMmJkMi0xMWVlLTkzYjMtYjkwYjJmZDNhOGQ3'
message = 'Hello **DevNet Associates** _WICIDA SAMARINDA_!!'

url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))