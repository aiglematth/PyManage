#Auteur --> aiglematth
#But    --> Contient la classe qui formate la réponse OK ou NOP
"""
#Implementation du protocole de verification de l'identite
  #Format de l'en-tête
    <cred_chiffre>
  #Format de l'en-tête de reponse
    <code_reponse>
  #Description de l'utilité des champs
    - <cred_chiffre> : Chacun chiffre ses credientals avec sa clef publique de la seconde paire, puis chiffre l'en-tête
                     avec la clef publique du destinataire
    - <code_reponse> : Si le dechiffrage se fait sans encombre, code_reponse = OKI sinon code_reponse = NOP
"""
#Imports
from Crypto.PublicKey import RSA
from .saveAndLoad import loadData
from .constantes import PATH_TO_OUR_KEYS, PATH_TO_HIS_KEYS, PATH_TO_CREDS

#Classe
class Format_verif():
    """
    Classe qui se chargera de former l'en-tête de la verif
    """
    def __init__(self, response=None):
        """
        Le constructeur de la classe
        """
        self.response = response
        self.en_tete = self.generate_en_tete()
        self.creds = None

    def set_response(self, response):
        self.response = response

    def generate_en_tete(self):
        """
        Var qui retournera l'en-tête appropriée
        """
        if self.response == None:
            return None

        if self.tcheck() == True:
            return self.get_oki()
        else:
            return self.get_nop()

    def tcheck(self):
        """
        Va tcheck si le mess se dechiffre
        """
        #On va chercher les creds
        creds = None
        with open(PATH_TO_CREDS, "r") as f:
            creds = f.readlines()
        #On degage les \n a la fin
        for x in range(len(creds)):
            creds[x] = creds[x].strip().split("@")
        #Import des clefs
        pKey = RSA.importKey(loadData(PATH_TO_OUR_KEYS)["dechiffrer"].encode())
        sKey = RSA.importKey(loadData(PATH_TO_HIS_KEYS)["dechiffrer"].encode())
        cred = sKey.decrypt(pKey.decrypt(self.response)).decode().split("@")
        self.creds = cred

        for c in creds:
            if c == cred:
                return True
        return False

    def get_oki(self):
        return b"OKI"

    def get_nop(self):
        return b"NOP"
