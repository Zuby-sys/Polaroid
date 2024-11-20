import os
from os import listdir
import csv
from pathlib import Path

images = []
image_path = [] 

folder_dir = "C:\\Steam\\userdata\\991345764\\760\\remote\\4000\\screenshots"
images = Path(folder_dir).glob('*.jpg')
for image in images:
    print(image)
    
filename = 'hzhz.csv'
with open("hzhz.csv", mode="w", encoding='utf-8') as w_file:
    names = ["name", "way"]
    file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                 lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    for file in images:
        file_writer.writerow({"name": images, "way": images})
