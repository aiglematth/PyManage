#Auteur --> aiglematth
#But    --> Implemente le formatage de l'en tete principale
"""
#Implémentation du protocole de la messagerie
  #Format de l'en-tếte
    <code_action>:<CRC>
  #Description de l'utilité des champs
    - <CRC>           : Le crc chiffré
    - <code_action>   : Le saint graal ;)

"""
#Imports
from Crypto.PublicKey import RSA
from random import choice
from hashlib import md5
from .saveAndLoad import loadData
from .constantes import PATH_TO_HIS_KEYS, PATH_TO_OUR_KEYS

#Classe
class Format_code():
    """
    Classe qui formate l'en tete avec le code
    """
    def __init__(self, code=None):
        """
        Constructeur de la classe
        """
        #Les attributs
        self.code = code
        #Le main
        self.en_tete = self.get_en_tete()

    def set_code(self, code):
        self.code = code

    def get_en_tete(self):
        """
        Méthode principale de la classe
        """
        if self.code == None:
            return None

        #Les clefs
        pkey = RSA.importKey(loadData(PATH_TO_OUR_KEYS)["chiffrer"].encode())
        skey = RSA.importKey(loadData(PATH_TO_HIS_KEYS)["chiffrer"].encode())

        mess = f"{self.code}"
        mess += f":{self.crc(mess)}"
        return skey.encrypt(pkey.encrypt(mess.encode(), None)[0], None)[0]

    def crc(self, mess):
        """
        On choppe le CRC
        """
        return md5(mess.encode()).hexdigest()

class Get_code():
    """
    Permet de retrouver le code
    """
    def __init__(self, response=None):
        """
        Constructeur de la classe
        :param response: La reponse a dechiffrer
        """
        self.response = response
        self.code    = self.do_all()

    def set_response(self, response):
        self.response = response

    def do_all(self):
        """
        On forge l'en tete reponse et on extrait le code_action
        """
        if self.response == None:
            return 0

        pkey = RSA.importKey(loadData(PATH_TO_OUR_KEYS)["dechiffrer"].encode())
        skey = RSA.importKey(loadData(PATH_TO_HIS_KEYS)["dechiffrer"].encode())

        messinit = skey.decrypt(pkey.decrypt(self.response)).decode()
        mess = messinit.split(":")
        if len(mess) != 2 or md5(mess[0].encode()).hexdigest() != mess[1]:
            return None
        else:
            return mess[0]
