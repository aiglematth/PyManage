#Auteur --> aiglematth
#But    --> Gérer la sauvegarde, récupération des clefs

#Imports
from pickle import dump, load

#Fonctions
def save(obj, path):
    with open(path, "wb") as f:
        return dump(obj, f)

def loadData(path):
    with open(path, "rb") as f:
        return load(f)
