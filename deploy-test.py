import requests
import json

def main():
    url = 'https://m3b8js.deta.dev'
    data = {
        "x": 3,
        "y": 5
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())

if __name__ == '__main__':
    main()