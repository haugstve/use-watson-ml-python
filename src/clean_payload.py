import json
from path import raw_data_path, processed_data_path


data = []
for i in range(7):
    file_path = raw_data_path / f'history_payloads_{i}.json'
    with open(file_path) as f:
        payloads = json.load(f)
        for payload in payloads:
            request = payload['request']
            data.append(request)

meron_data_path = processed_data_path / 'payloads_meron.json'
with open(meron_data_path, 'w+') as f:
    json.dump(data, f)
