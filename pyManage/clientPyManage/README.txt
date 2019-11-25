#Auteur --> aiglematth

### PyManage client ###

  #Fichiers de configuration

    --> conf_client.py : Contient plusieurs options (nottament port source, interfaces à mettre en attente, taille des clefs...)
                         qui sont intéressantes à configurer sur son serveur

    --> constantes.py  : Plusieurs path peuvent être édités via ce fichier ainsi que la taille des clefs
                         (ATTENTION, CE FICHIER N'A PAS POUR VOCATION PREMIERE D'ETRE MODIFIE)

  #Utilisation

    python3 client.py <ip> <port> <username> [-v (si -v est mis, la verbose sera active)] [-c <code_action> ] [-h (permet d'avoir l'aide)]
