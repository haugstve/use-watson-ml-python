import options
import requests
import json
import random


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


def load_aim_token():
    with open(options.aim_token_file_path, "r") as token_file:
        return json.load(token_file)


def aim_token():
    print('loading aim token')
    try:
        print(
            f'trying to read aim token from '
            f'file: {options.aim_token_file_path}'
        )
        token = load_aim_token()
        print('success, aim token found on file')
        return token
    except FileNotFoundError:
        print('failed to read aim token from file')
        print('requesting token from iam')
        r = request_aim_token()
        r.raise_for_status()
        print(
            f'request successful, storing aim token '
            'to file {options.aim_token_file_path}'
        )
        token = r.json()
        with open(options.aim_token_file_path, "w+") as token_file:
            json.dump(token, token_file, indent=4)
        return token


if __name__ == "__main__":
    with open('payloads_meron.json', 'r') as f:
        payloads = json.load(f)
        token = aim_token()
        selection = random.randint(0, len(payloads))
        result = evaluate_meron_model(token, payloads[selection])
        print(result.status_code)
        print(result.content)
