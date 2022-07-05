import json

json_lines = []
with open('./filtred_train_data.json') as f:
    for line in f.readlines():
        try:
            d = json.loads(line)
        except json.decoder.JSONDecodeError as e:
            print(e)
            print("----------------------------------------------------")
            continue
        json_lines.append(d)
print(len(json_lines))
print(json_lines[0])
