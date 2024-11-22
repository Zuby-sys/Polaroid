from pprint import pprint
from flask import Flask, json
import os
import requests

def get_img_from_gr():
    img_from_gr = requests.get(data={"name":"url"})
    print(img_from_gr.json())
    return img_from_gr

if __name__ == "__main__":
    img = input("Ждем пост")
    url = get_img_from_gr()
    pprint(url)
