from pprint import pprint
import requests
import os

def get_img_from_gr():
    img_from_gr = requests.put(data={"name":"url"})
    return img_from_gr

if __name__ == "__main__":
    img = input("Ждем пост")
    url = get_img_from_gr()
    pprint(url)
