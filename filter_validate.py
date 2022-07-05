import json

json_lines = []
validate_attribute = ["overall", "verified", "reviewTime", "reviewerID",
                      "asin", "style", "reviewerName", "reviewText", "summary", "unixReviewTime"]
with open('./filtred_train_data.json') as f:
    for line in f.readlines():
        try:
            d = json.loads(line)
        except json.decoder.JSONDecodeError as e:
            print(e)
            print("----------------------------------------------------")
            continue
        if all([attribute in d for attribute in validate_attribute]):
            json_lines.append(d)
print(len(json_lines))

with open('validate.json', 'w') as f:
    json.dump(json_lines, f, indent=4)