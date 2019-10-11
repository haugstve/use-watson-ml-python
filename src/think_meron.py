import options
import requests


def request_aim_token():
    return requests.post(
        options.aim_url,
        headers=options.aim_headers,
        data=options.aim_body)


def evaluate_meron_model(token, payload):
    headers = options.meron_headers
    headers["Authorization"] = "Bearer " + token["access_token"]
    return requests.post(
        options.meron_url,
        headers=headers,
        json=payload)


def aim_token():
    print('requesting token from iam')
    r = request_aim_token()
    r.raise_for_status()
    print(f'request successful')
    token = r.json()
    return token
