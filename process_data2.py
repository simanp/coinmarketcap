import csv, json

d = {}
with open('dict.json', 'r') as fp:
    d = json.load(fp)
v = ['Time Stamp'] + list(d.keys())

with open("big_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows([v])