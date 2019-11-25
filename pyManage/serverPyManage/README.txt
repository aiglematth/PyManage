#Auteur --> aiglematth

### PyManage server ###

  #Fichiers de configuration

    --> conf_serv.py    : Contient plusieurs options (nottament port source, interfaces à mettre en attente, taille des clefs...)
                          qui sont intéressantes à configurer sur son serveur

    --> creds           : Fichier qui contient les credientals des users qui pourront se connecter à votre service PyManage, ces
                          creds sont de la forme username@password et sont au nombre de 1 par ligne

    --> actions.py      : Fichier qui contient les actions que votre serveur pourra effectuer, à vous d'ajouter vos codes_actions,
                          pour ce faire, créez une classe qui contient une méthode start().
                          Rajoutez ensuite une ligne dans le dictionnaire ACTIONS, qui sera de la forme :
                             "Nom_de_votre_code_action" : La_Classe_A_Appeler

    --> conf_actions.py : Permet de régler le chemin du dossier qui contiendra les scripts bash qui seront executables, ainsi que
                          le timeout maximal dans lequel l'action doit s'éxécuter

    --> constantes.py   : Plusieurs path peuvent être édités via ce fichier ainsi que la taille des clefs
                          (ATTENTION, CE FICHIER N'A PAS POUR VOCATION PREMIERE D'ETRE MODIFIE)

  #Fichiers logs

    --> logs_connects.txt : Enregistre toutes les connexions

    --> logs_creds.txt    : Enregistre les echecs d'authentification

    --> logs_timeout.txt  : Enregistre les connexions qui ont échouées à cause d'un timeout

    --> logs_error.txt    : Enregistre les erreurs du serveur

  #Utilisation

    python3 server.py
