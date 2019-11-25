#Auteur --> aiglematth
#But    --> Le serveur de l'application

"""
NOTE : on pourra multithreader le serv pour qu'il accepte plusieurs clients en meme temps
"""

#Imports
#Lib python
from socket                     import socket, AF_INET, SOCK_STREAM, timeout
from sys                        import exit
from time                       import sleep
#Lib moi ^^
from confzone.conf_serv         import *
from codezone.proto_send_key    import *
from codezone.proto_verif_creds import *
from codezone.proto_com         import *
from codezone.proto_exe         import *
from codezone.log               import *

#Classes
class Server():
    """
    Attention...la big classe du serveur
    """
    def __init__(self):
        """
        Le constructeur de la classe
        """
        #Le matos dont j'aurai besoin pour traiter les demandes client
        self.register   = Register_keys()
        self.verif_cred = Format_verif()
        self.get_code   = Get_code()
        self.exe        = Exe()
        self.log        = Log()

    def run_server(self):
        """
        La méthode principale
        """
        try:
            with socket(AF_INET, SOCK_STREAM) as sock:
                #On gère l'aspect reseau
                sock.bind(SOCK)
                sock.listen(LISTEN)
                while True:
                    (client, infos) = sock.accept()
                    #On log la connection du client
                    self.log.set_infos(infos)
                    self.log.log()
                    #On set un timeout
                    client.settimeout(TIMEOUT)
                    try:
                        #On attend l'envoi des clefs
                        clefs = client.recv(SIZE_TO_RECV_KEYS)
                        #On les stock
                        self.register.register(clefs)
                        #On genere les notres
                        nos_clefs = Format_keys()
                        #On les send
                        client.send(nos_clefs.en_tete)
                        #On attend les creds
                        creds = client.recv(SIZE_TO_RECV)
                        #On genere l'en tete reponse
                        self.verif_cred.set_response(creds)
                        reponse = self.verif_cred.generate_en_tete()
                        #On l'envoi au client
                        client.send(reponse)
                        #On tcheck la reponse
                        if reponse == b"NOP":
                            raise Exception
                        elif reponse == b"OKI":
                            #On met un timeout long
                            client.settimeout(TIMEOUT_ACTIONS)
                            #Boucle de reception des actions
                            while True:
                                try:
                                    #On attend ses codes_actions
                                    code_action = client.recv(SIZE_TO_RECV)
                                    #Et on le traite
                                    self.get_code.set_response(code_action)
                                    code_action = self.get_code.do_all()
                                    #Si code de fin on quitte
                                    if reponse == b"FIN":
                                        break
                                    self.exe.set_code_action(code_action)
                                    self.exe.parse_code_action()
                                    reponse = self.exe.exe()
                                    #On envoi le code reponse
                                    client.send(reponse)

                                except timeout:
                                    #Si trop de temps entre deux actions on met fin à la communication
                                    client.send(b"FIN")
                                    break
                    except timeout:
                        #On log dans un fichier bien specifique
                        self.log.log_exceptTimeout()
                    except Exception:
                        self.log.log_exceptCreds(self.verif_cred.creds)
                    finally:
                        try:
                            #On ferme le client
                            client.close()
                        except:
                            pass

        except KeyboardInterrupt:
            try:
                client.close()
            except:
                pass
            finally:
                exit(0)

if __name__ == '__main__':
    Server().run_server()
