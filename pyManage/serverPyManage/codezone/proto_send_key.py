#Auteur --> aiglematth
#But    --> Contient la classe qui génère l'en-tête du protocole d'envoi des clefs des clefs
"""
#Implémentation du protocole d'envoi des clefs
    #Format de l'en-tête
        <la_clef_publique>:<la_clef_prive_de_la_seconde_paire>
    #Description de l'utilité des champs
        - <la_clef_publique>                  : Celle avec laquelle le destinataire chiffrera ses messages
        - <la_clef_prive_de_la_seconde_paire> : Celle avec laquelle la souce chiffrera le mot d'authenticité et le CRC
"""
#Imports
from Crypto.PublicKey import RSA
from .constantes import SIZE_OF_PRIMARY_KEY, SIZE_OF_SECONDARY_KEY, PATH_TO_OUR_KEYS, PATH_TO_HIS_KEYS
from .saveAndLoad import save

#Classe
class Format_keys():
    """
    Classe de l'implementation du protocole de l'envoi des clefs
    """
    def __init__(self):
        """
        Constructeur de la classe
        """
        #Les objets clefs
        self.pK   = RSA.generate(SIZE_OF_PRIMARY_KEY)
        self.sK = RSA.generate(SIZE_OF_SECONDARY_KEY)
        #L'en tête formatée, prête à envoyer
        self.en_tete = f"{self.pK.publickey().exportKey().decode()}:{self.sK.exportKey().decode()}".encode()
        save({"dechiffrer":self.pK.exportKey().decode() , "chiffrer":self.sK.publickey().exportKey().decode()}, PATH_TO_OUR_KEYS)

    def get_en_tete(self):
        return self.en_tete

class Register_keys():
    """
    Enregistre les clefs recues
    """
    def __init__(self, en_tete=None):
        """
        Constructeur de la classe
        """
        self.register(en_tete)

    def register(self, en_tete):
        if en_tete == None:
            return None

        to_register = en_tete.decode().split(":")
        to_register = {"chiffrer":to_register[0] , "dechiffrer":to_register[1]}
        save(to_register, PATH_TO_HIS_KEYS)
