import requests
import json

access_token = 'ZTEzMTNhYzAtODQ4Zi00Mzc2LTg3NWUtNjM4ZmE2ZjQ0NjEzMWU3ZThhZTAtYzRm_P0A1_c9a3c616-b39c-460f-b134-dd9f31b56890'
url = 'https://webexapis.com/v1/rooms'

headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
