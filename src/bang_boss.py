import requests
import base64
import json


def get_basic_auth_str(username, password):
    temp_str = username + ':' + password
    bytes_string = temp_str.encode(encoding="utf-8")
    encode_str = base64.b64encode(bytes_string)
    return 'Basic ' + encode_str.decode()


if __name__ == "__main__":
    key = '5f3e5bdb75a03c4818b8dbbc'
    secret = 'x0Wt0DfdNoByYhTCDVhJrRJQfZuX7W7k'
    url = "http://api.jsform.com/api/v1/form/5fab8e43fc918f1d5e328279"

    # r = requests.get(url, headers={'Authorization': get_basic_auth_str(key, secret)})
    # json_str = json.dumps(r.json(), sort_keys=True, indent=4, ensure_ascii=False)
    # print(json_str)

    # r2 = requests.get('http://api.jsform.com/api/v1/report/grouplist', auth=(key, secret))
    # print(json.dumps(r2.json(), sort_keys=True, indent=4, ensure_ascii=False))

    r3 = requests.get('http://api.jsform.com/api/v1/reportlist/5fcf0adafc918f2a72320b61', auth=(key, secret))
    print(json.dumps(r3.json(), sort_keys=True, indent=4, ensure_ascii=False))

    # params = {
    #     "form_id": "5fab8e43fc918f1d5e328279",
    #     "fields": [
    #         "field16",
    #         "field17",
    #         "field18",
    #         "field19"
    #     ]
    # }
    # r3 = requests.post('http://api.jsform.com/api/v1/entry/query', params=params)
