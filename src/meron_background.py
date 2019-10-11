import schedule
import time
import random
import json
from think_meron import aim_token, evaluate_meron_model
from path import processed_data_path, root


def job():
    data_path = processed_data_path / 'payloads_meron.json'
    with open(data_path, 'r') as f:
        payloads = json.load(f)

    token = aim_token()
    selection = random.randint(0, len(payloads))
    response = evaluate_meron_model(token, payloads[selection])

    log_path = root / 'response.log'
    with open(log_path, 'a+') as f:
        f.write(f'status: {response.status_code}'
                f', content: {response.content}\n')


schedule.every().minute.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
