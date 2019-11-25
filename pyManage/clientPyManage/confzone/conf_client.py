#Auteur --> aiglematth
#But    --> Fichier de conf du serveur

#Les params reseau

SIZE_TO_RECV_RESPONSE_CODE = 256 # la taille de max de reception du code retour que le serveur envoi au client
SIZE_TO_RECV      = 512          # la taille max de reception des credientals et codes_action, conseillée à max 512
SIZE_TO_RECV_KEYS = 4096         # la taille max de reception des clefs, conseillee superieure ou egale à 1024
TIMEOUT           = 10           # Le timeout max d'envoi des clefs puis des creds
TIMEOUT_ACTIONS   = 5 * 60       # Le timeout entre max entre la reception des reponses serveur des codes acions envoyées en secondes
