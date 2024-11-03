import json
import glob

rootp = "UnderTheHood/Images/"

def introduce_files(Classvar):
    "introduce as filename.json"
    while True:
        print ("What's the name of the piece?")
        name = input()
        namesearch = name[:3] +"*.jpg"
        globsearch = rootp + Classvar.class_path + namesearch
        imagelist = []
        imagelist = glob.glob(globsearch)
        data = {"name" : name, "images" : imagelist}
        with open('data.json', 'r+') as json_file:
            json.dump(data, json_file)

        nopare = None
        print ("For more input type 2")
        nopare = input()
        if nopare != 2:
            break