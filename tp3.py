import socket, optparse, sys
from socketUtil import recv_msg, send_msg
from cryptoModule import entierAleatoire, trouverNombrePremier, exponentiationModulaire

parser = optparse.OptionParser()
parser.add_option("-s", "--server", action="store_true", dest="serveur", default=False)
parser.add_option("-a", "--address", action="store", dest="address", default="localhost")
parser.add_option("-p", "--port", action="store", dest="port", type=int, default=1337)
opts = parser.parse_args(sys.argv[1:])[0]

if opts.serveur:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind(("localhost", opts.port))
        serversocket.listen(5)
        print("Listening on port " + str(serversocket.getsockname()[1]))

        i = 0
        while True:
            (s, address) = serversocket.accept()
            i += 1
            print(str(i) + " connexion to server")

            modulo = trouverNombrePremier()
            base = entierAleatoire(modulo)

            send_msg(s, str(modulo))
            print("Send modulo: " + str(modulo))

            send_msg(s, str(base))
            print("Send base: " + str(base))

            privateKey = entierAleatoire(modulo)
            publicKey = exponentiationModulaire(base, privateKey, modulo)

            send_msg(s, str(publicKey))

            publicKeyRcv = int(recv_msg(s))

            sharedKey = exponentiationModulaire(publicKeyRcv, privateKey, modulo)

            print("Private key: " + str(privateKey))
            print("Public key: " + str(publicKey))
            print("Public key received: " + str(publicKeyRcv))
            print("Shared key: " + str(sharedKey))

            s.close()

else:
    destination = (opts.address, opts.port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(destination)

    moduloClient = int(recv_msg(s))
    baseClient = int(recv_msg(s))

    print("Received modulo: " + str(moduloClient))
    print("Received base: " + str(baseClient))

    privateKeyClient = entierAleatoire(moduloClient)

    publicKeyClient = exponentiationModulaire(baseClient, privateKeyClient, moduloClient)
    publicKeyRcvClient = int(recv_msg(s))
    send_msg(s, str(publicKeyClient))

    sharedKeyClient = exponentiationModulaire(publicKeyRcvClient, privateKeyClient, moduloClient)

    print("Private key: " + str(privateKeyClient))
    print("Public key: " + str(publicKeyClient))
    print("Public key received: " + str(publicKeyRcvClient))
    print("Shared key: " + str(sharedKeyClient))

    s.close()







