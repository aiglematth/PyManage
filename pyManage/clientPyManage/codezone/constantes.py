#Auteur --> aiglematth
#But    --> Toutes les constantes de l'app

#Imports
from os.path import curdir, join, pardir, abspath

SIZE_OF_PRIMARY_KEY   = 4096
SIZE_OF_SECONDARY_KEY = 1024

name                 = ""
path_to_keys         = "keys"
path_to_logs         = "logs"
path_to_creds        = "creds"

PATH_TO_OUR_KEYS     = join(abspath(name), path_to_keys, "keys.txt")
PATH_TO_HIS_KEYS     = join(abspath(name), path_to_keys, "hiskeys.txt")
PATH_TO_CREDS        = join(abspath(name), path_to_creds, "creds.txt")
PATH_TO_LOGS         = join(abspath(name), path_to_logs, "logs_connects.txt")
PATH_TO_LOGS_TIMEOUT = join(abspath(name), path_to_logs, "logs_timeout.txt")
PATH_TO_LOGS_CREDS   = join(abspath(name), path_to_logs, "logs_creds.txt")
PATH_TO_LOGS_ERROR   = join(abspath(name), path_to_logs, "logs_errors.txt")

K = 32

REP_CODE = {
    "TRUE"  : "Le code action s'est exe et il retourne True",
    "FALSE" : "Le code action s'est exe mais retourne False",
    "NONE"  : "Le code action est inexistant",
    "NOP"   : "Une erreur inconnue est survenue"
}
