#Auteur --> aiglematth
#But    --> Le client de notre application

#Imports
#Lib python
from sys                           import exit
from argparse                      import ArgumentParser
from getpass                       import getpass
from socket                        import socket, AF_INET, SOCK_STREAM, timeout
#Lib moi ^^
from codezone.constantes           import REP_CODE
from codezone.proto_send_key       import *
from codezone.proto_com            import *
from codezone.proto_cred           import *
from confzone.conf_client          import *

#Classes
class Parser():
    """
    Le parser de nos arguments
    """
    def __init__(self):
        """
        Le constructeur de la classe
        """
        #Le parser
        self.parser = ArgumentParser()
        #Ses règles
        self.parser.add_argument("s", type=str, help="L'ip ou le nom d'hôte à joindre")
        self.parser.add_argument("p", type=int, help="Le port du serveur à joindre")
        self.parser.add_argument("u", type=str, help="Votre nom d'utilisateur pour ce service")
        self.parser.add_argument("-c", type=str, help="Le code action a envoyer")
        self.parser.add_argument("-v", action="store_true", help="Active le mode verbeux, sans ce mode, seul le code retour apparait sans explications")
        #Les resultats
        self.args = self.parser.parse_args()

class Client():
    """
    Le client enfiiiiiin
    """
    def __init__(self):
        """
        Le constructeur de la classe
        """
        #Nos classes
        self.format_code = Format_code()
        self.register   = Register_keys()
        #On recup les options
        self.args = Parser().args
        self.sock = (self.args.s, self.args.p)
        self.user = self.args.u
        self.comm = self.args.c
        self.verb = self.args.v
        #Et la le password
        self.password = getpass(f"Mot de passe [{self.user}] : ")
        #On lance le tout
        self.client()


    def client(self):
        """
        La méthode principale
        """
        try:
            with socket(AF_INET, SOCK_STREAM) as sock:
                #On gère l'aspect reseau
                sock.connect(self.sock)
                #On set un timeout
                sock.settimeout(TIMEOUT)
                try:
                    #On genere nos clefs
                    nos_clefs = Format_keys()
                    #On les send
                    sock.send(nos_clefs.en_tete)
                    #On attend l'envoi des clefs
                    clefs = sock.recv(SIZE_TO_RECV_KEYS)
                    #On les stock
                    self.register.register(clefs)
                    #On génère les creds
                    creds = Format_cred([self.user, self.password]).en_tete
                    #On l'envoi au serv
                    sock.send(creds)
                    #On attend le code repoonse
                    reponse = sock.recv(SIZE_TO_RECV_RESPONSE_CODE)
                    #On tcheck la reponse
                    if reponse == b"NOP":
                        raise Exception
                    elif reponse == b"OKI":
                        try:
                            #Interractive mode
                            if self.comm == None:
                                #On met un timeout long
                                sock.settimeout(TIMEOUT_ACTIONS)
                                    #Boucle d'envoi des actions des actions
                                while True:
                                    #On demande le code action
                                    code_action = input("Code_action > ")
                                    reponse = self.do_exe(code_action, sock)
                                    #On verif si c'est la fin
                                    if reponse == "FIN":
                                        break
                                    #On affiche...
                                    self.affiche(reponse)
                            else:
                                        reponse = self.do_exe(self.comm, sock)
                                        #On affiche...
                                        self.affiche(reponse)
                        except Exception:
                            self.pr("Erreur, liaison close, vous avez pu :\n  - mettre trop de temps à envoyer votre commande par rapport au temps maximum d'attente accepté par le serveur\n  - Envoyer un code_action trop long")

                except timeout:
                    #On log dans un fichier bien specifique
                    self.pr("### Serveur trop long à répondre lors de la phase d'initialisation de la connection, il y a pu avoir eu une erreur ###")
                except Exception:
                    self.pr("### Nom d'utilisateur ou mot de passe incorrect ###")
                finally:
                    raise KeyboardInterrupt

        except KeyboardInterrupt:
            self.pr("\n### ARRET SERVICE ###")
            exit(0)

    def do_exe(self, code_action, sock):
        #Et on le traite
        self.format_code.set_code(code_action)
        en_tete = self.format_code.get_en_tete()
        sock.send(en_tete)
        if code_action.upper() == "FIN":
            return "FIN"
        #On envoi le code reponse
        reponse = sock.recv(SIZE_TO_RECV_RESPONSE_CODE).decode()
        return reponse

    def affiche(self, reponse):
        if self.verb == True:
            print(f"{reponse.upper()} : {REP_CODE[reponse.upper()]}")
        else:
            print(f"{reponse.upper()}")

    def pr(self, prompt):
        if self.verb == True:
            print(prompt)


if __name__ == '__main__':
    Client()
