#Auteur --> aiglematth

### PyManage ###

  #Synopsis du projet
    Création d'un manager de services point à point sécurisé au niveau des communications

    L'avantage par rapport au ssh , on peut faire du one line pour effectuer des actions nécessitant
    un traîtement long, et le chiffrememnt reste du RSA tout au long de la communication, et ne passe
    pas à du AES, de plus l'utilisateur n'aura accès qu'à des codes_actions prédéterminés par vos soins.

    L'inconvénient est la taille limite du code_action (voir plus loin pour comprendre ce mot) que nous
    pouvons envoyer.

  #Principe
    #Pour assurer la confidentialitée
      - Magré la lourdeur des calculs demandés par le chiffrement asymétrique, il sera utilisé tout au long de
        la communication afin de chiffrer les en-têtes envoyées
    #Pour assurer l'authenticitée
      - Utilisation d'un "mot d'authenticité", le principe est simple, à chaque communication, une seconde paire de
        clefs RSA va être générée par chacun des partis, et chaque parti diffusera la clef privé de cette paire de clefs, ensuite,
        à chaque envoi de messages, chacun des membres de la conversation va chiffrer son en-tete avec la clef publique de sa seconde paire,
        si une fois le message déchiffré le format de l'en tete est bien retrouvé, l'authenticitée est assurée
    #Pour assurer l'intégritée
      - Toujours avec la seconde paire de clefs, chaque message possèdera un CRC qui sera le hash MD5 de l'en-tếte
        Il sera envoyé a la fin de l'en-tête, si quand le destinataire recalcule le CRC il tombe
        sur le même, le message est intègre.

    #Implémentation du protocole d'envoi des clefs
      #Format de l'en-tête
        <la_clef_publique>:<la_clef_prive_de_la_seconde_paire>
      #Description de l'utilité des champs
        - <la_clef_publique>                  : Celle avec laquelle le destinataire chiffrera ses messages
        - <la_clef_prive_de_la_seconde_paire> : Celle avec laquelle la souce chiffrera le mot d'authenticité et le CRC

    #Implémentation du protocole d'envoi de username@password
      #Format de l'en-tête
        username@password
      #Description de l'utilité des champs
        - username@password : chiffre par notre seconde paire de clefs et la clef publique du destinataire

    #Implementation du protocole de verification de l'identite
      #Format de l'en-tête
        <cred_chiffre>
      #Format de l'en-tête de reponse
        <code_reponse>
      #Description de l'utilité des champs
        - <cred_chiffre> : Chacun chiffre ses credientals avec sa clef publique de la seconde paire, puis chiffre l'en-tête
                         avec la clef publique du destinataire
        - <code_reponse> : Si le dechiffrage se fait sans encombre, code_reponse = OKI sinon code_reponse = NOP

    #Implémentation du protocole de la messagerie
      #Format de l'en-tếte
        <code_action>:<CRC>
      #Description de l'utilité des champs
        - <CRC>           : Le crc chiffré
        - <code_action>   : Le saint graal, de la forme code_action@arg1,arg2,arg3,[...],argn
      #Reponse
        - TRUE  : Exe sans encombre
        - FALSE : Code action existant mais renvoi False de la fonction executée
        - NONE  : Code action inexistant
        - NOP   : Code action égal à None
