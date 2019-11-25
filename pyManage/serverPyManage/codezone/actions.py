#Auteur --> aiglematth
#But    --> Contient les classes executables par le serveur

"""
Doivent être callable de la forme NomDeLaClasse(args).start()
avec args de type list, tuple ou None
"""

#Imports
from sys          import exit
from subprocess   import Popen, PIPE, TimeoutExpired
from os.path      import join
from .conf_actions import *
#Classes
#Forme de la classe
class AbstractCall():
    """
    La forme de la classe, peut être surchargée
    """
    def __init__(self, args=None):
        """
        Le Constructeur de la classe
        :param args: Une liste des arguments à use
        """
        self.args = args

    def start(self):
        """
        Methode qui sera appele quand le serv exe le code_action, retourne true si bonne exe sinon false
        """
        return True

class Test(AbstractCall):
    """
    On a un test
    """
    def __init__(self, args):
        AbstractCall.__init__(self, args)

    def start(self):
        print(f"Test, args = {self.args}")
        return True

class Bash_exe(AbstractCall):
    """
    On exe un script bash situé dans le rep des scripts, une securite minimale est set (verification que ../ pas dans les args)
    mais pas de chroot pendant l'exe du script donc vos scripts peuvent agir sur toute la machine ^^
    """
    def __init__(self, args):
        AbstractCall.__init__(self, args)

    def start(self):
        if "../" in self.args[0]:
            return False

        exe = Popen(   (join(PATH_TO_SCRIPTS, self.args[0])   ), shell=True, stdout=PIPE, stderr=PIPE)
        try:
            (out, err) = exe.communicate(timeout=TIMEOUT)
            return True
        except TimeoutExpired:
            return False

#Renseigner vos classes de la sorte:
#   "NOM_EN_MAJUSCULE" : Classe
#
#IMPORTANT LE CODE "FIN" NE DOIT PAS ETRE UTILISE
#
ACTIONS = {
    "TEST"     : Test,
    "BASH_EXE" : Bash_exe
}
