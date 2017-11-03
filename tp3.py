import socket, optparse, sys
from socketUtil import recv_msg, send_msg
from cryptoModule import entierAleatoire, trouverNombrePremier, exponentiationModulaire

parser = optparse.OptionParser()
parser.add_option("-s", "--server", action="store-true", dest="serveur", default=False)
parser.add_option("-a", "--adress", action="store", dest="adress", default="localhost")
parser.add_option("-p", "--port", action="store", deest="port", type=int, default=1337)
opts = parser.parse_args(sys.argv[1:])[0]


