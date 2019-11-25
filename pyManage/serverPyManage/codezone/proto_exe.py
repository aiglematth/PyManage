#Auteur --> aiglematth
#But    --> Gère la bonne exe du code action

#Imports
from .actions import *
from .log import *

#Classe
class Exe():
    """
    La classe qui traite le code action
    """
    def __init__(self, code_action=None):
        """
        Le Constructeur de la classe
        :param code_action: Le code action à gérer
        """
        self.code_action = code_action
        self.en_tete     = self.parse_code_action()

    def set_code_action(self, code_action):
        self.code_action = code_action

    def parse_code_action(self):
        if self.code_action == None:
            return None

        spl = self.code_action.split("@")
        if len(spl) == 1:
            self.code_action = (spl[0], None)
        else:
            args = spl[1].split(",")
            self.code_action = (spl[0], args)

    def exe(self):
        """
        La méthode qui va exe, retourne TRUE si bonne exe, sinon FALSE ou NONE si pas de code_action
        """
        if self.code_action == None or self.code_action[0].upper() == "FIN":
            return b"FIN"

        try:
            code_retour = ACTIONS[self.code_action[0].upper()](self.code_action[1]).start()
            if code_retour == True:
                return b"TRUE"
            else:
                return b"FALSE"
        except KeyError:
            #Code action invalide
            return b"NONE"
        except Exception as e:
            Log().log_error(e)
            #Code action erreur
            return b"NOP"
