import json

def load_country(country):

    with open("jawiki-country.json", "r") as f:
        data = f.readline()
        while data:
            d = json.loads(data)
            if d["title"] == country:
                return d["text"]
                break
            data = f.readline()

    return ""

