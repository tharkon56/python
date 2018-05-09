import socket

def Main():
        host = 'localhost'
        port = 5002

        mySocket = socket.socket()
        mySocket.connect((host,port))
        print("Entrez le nom du premier pokemon :")
        message1 = raw_input(" -> ")
        print("Entrez le nom du deuxieme pokemon :")
        message2 = raw_input(" -> ")
        message = message1 + " " + message2

        mySocket.send(message.encode())

        data = mySocket.recv(1024).decode()
        print (data)
        mySocket.close()

        '''
        while message != 'q':

                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()


                if data == "Ce pokemon nexiste pas":
                    print("Ce pokemon nexiste pas")

                else:
                    data = data[1:-1]
                    data = data.split(',')
                    nom = data[1].split("'")[1]
                    print(nom)



                message = raw_input(" -> ")

        mySocket.close()
        '''

if __name__ == '__main__':
    Main()
