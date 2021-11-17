import requests


def post_text(url, text):
    result = requests.post(url, json={"text": text})
    return result
