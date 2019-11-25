#Auteur --> aiglematth
#But    --> Fichier de conf du serveur

#Les params reseau
SOCK                = ("", 5555)   # tuple de la forme --> (INTERFACES, PORT)
LISTEN              = 1            # nombre d'attente
SIZE_TO_RECV        = 512          # la taille max de reception des credientals et codes_action, conseillée à max 512
SIZE_TO_RECV_KEYS   = 4096         # la taille max de reception des clefs, conseillee superieure ou egale à 1024
TIMEOUT             = 5            # Le timeout max d'envoi des clefs puis des creds, est enleve ensuite
TIMEOUT_ACTIONS     = 5 * 60       # Le timeout entre max entre deux acions envoyées en secondes
"""
TIME_BETWEEN_TWO_CO = 5            # Le time durant lequel vous ferez dormir votre serveur entre deux connections, important
                                   # pour laisser le temps à votre OS de re-rendre libre le port
"""
