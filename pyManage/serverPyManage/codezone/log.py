#Auteur --> aiglematth
#But	--> On cree un fichier log

#Imports
from .constantes import PATH_TO_LOGS, PATH_TO_LOGS_TIMEOUT, PATH_TO_LOGS_CREDS, PATH_TO_LOGS_ERROR
from datetime import datetime

#Classe
class Log():
    """
    La classe qui log les connections
    """
    def __init__(self, infos=None):
        """
        Le constructeur de la classe
        :param infos: Un tuple généré par socket.accept()
        """
        self.infos = infos

    def set_infos(self, infos):
        self.infos = infos

    def log_abstract(self, path, creds=None, error=None):
        """
        Méthode abstraite
        Log de la forme : IP:<ip>,PORT:<port>\n
        """
        if creds != None:
            format = f"IP:{self.infos[0]},PORT:{str(self.infos[1])},CREDS:{creds},DATE:{str(datetime.now())}\n"
        elif error != None:
            format = f"{e}\n,DATE:{str(datetime.now())}"
        else:
            format = f"IP:{self.infos[0]},PORT:{str(self.infos[1])},DATE:{str(datetime.now())}\n"

        with open(path, "a") as file:
            file.write(format)

    def log(self):
        self.log_abstract(PATH_TO_LOGS)

    def log_exceptTimeout(self):
        self.log_abstract(PATH_TO_LOGS_TIMEOUT)

    def log_exceptCreds(self, creds):
        self.log_abstract(PATH_TO_LOGS_CREDS, creds=creds)

    def log_error(self, e):
        self.log_abstract(PATH_TO_LOGS_ERROR, error=e)
