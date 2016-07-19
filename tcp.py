import socket
import sys
import struct

class TCPConnection:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 11421
        # Bind the socket to the port
        server_address = ('', self.port)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        self.sock.bind(server_address)

        #Calling listen() puts the socket into server mode...
        self.sock.listen(1)
        #and accept() waits for an incoming connection.

        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        self.connection, self.client_address = self.sock.accept()

        print("Connected to " + str(self.client_address))

    def read(self):
        #read header
        header = self.connection.recv(8)
        print(header)
        magic_number = struct.unpack('B',header[0])[0]
        if magic_number != 37:
            raise Exception("Error while receiving data: Magic Number is wrong. Is " + str(magic_number) +" but should be 37.")
        #length = data[1]*256 + data[2]
        message_length = struct.unpack('H',header[1:3])[0]
        print("message length" + str(message_length))

        data_as_string = self.connection.recv(message_length)
        nr_of_doubles = message_length/8
        #data_as_list = [0]*nr_of_double

        #for i in range(nr_of_double):
        ##    data_as_list[i] = struct.unpack
        return struct.unpack('d'*nr_of_doubles, data_as_string)

    @staticmethod
    def send(message):
#    def send(self,message):
        header = [0]*8
        header[0] = 37
        message_length = len(message)*8
        header[1] = int(message_length/256)
        header[2] = message_length % 256

        #self.connection.send(header)
        for number in message:
            data=[0]*8
            struct.pack_into('s', data,0,number)
            #self.connection.send(data)
            print(data)
