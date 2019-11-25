#Auteur --> aiglematth
#But    --> Implémente la classe qui formate l'INIT mess
"""
#Implémentation du protocole d'envoi de username@password
    #Format de l'en-tête
        username@password
    #Description de l'utilité des champs
        - username@password : chiffre par notre seconde paire de clefs et la clef publique du destinataire

"""
#Imports
from Crypto.PublicKey import RSA
from .constantes import PATH_TO_OUR_KEYS, PATH_TO_HIS_KEYS, K
from .saveAndLoad import loadData

#Classe
class Format_cred():
    """
    La classe qui contient l'implementation
    """
    def __init__(self, credientals):
        """
        Constructeur de la classe
        :param credientals: Liste [username, password]
        """
        self.en_tete = self.get_en_tete(credientals)

    def get_en_tete(self, credientals):
        """
        Formate l'en-tête
        :param credientals: Liste [username, password]
        """
        creds = f"{credientals[0]}@{credientals[1]}".encode()
        pk = RSA.importKey(loadData(PATH_TO_OUR_KEYS)["chiffrer"].encode())
        sk = RSA.importKey(loadData(PATH_TO_HIS_KEYS)["chiffrer"].encode())
        mess = sk.encrypt(pk.encrypt(creds, K)[0], K)[0]
        return mess
