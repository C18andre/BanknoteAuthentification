## Main 
import json
with open("src/settings.json") as file:
            settings = json.load(file)
    

from preprocessing.fonctions import cleaner
cleaner(settings)

