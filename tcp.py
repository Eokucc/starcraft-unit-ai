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
        self.sock.listen(2)

    def accept(self):
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        self.connection, self.client_address = self.sock.accept()
	self.connected = True
        print("Connected to " + str(self.client_address))

    def read(self):
        #read header
        header = self.connection.recv(8)
	if not header:
		self.connected=False
		return [-1]
	if len(header) != 8:
		raise Exception("Got header of invalid size.")

        #print(header)
        magic_number = struct.unpack('B',header[0])[0]
        if magic_number != 37:
            raise Exception("Error while receiving data: Magic Number is wrong. Is " + str(magic_number) +" but should be 37.")
        
        message_length = struct.unpack('>H',header[1:3])[0]
        #print("message length" + str(message_length))

        data_as_string = self.connection.recv(message_length)
	if not data_as_string:
		self.connected=False
		return [-1]
        nr_of_doubles = message_length/8

        return struct.unpack('d'*nr_of_doubles, data_as_string)

    def send(self,message):
        message_length = len(message)*8
	
	header = struct.pack('>BH5x', 37, message_length)

        self.connection.send(header)
        data = ''
	
	for number in message:
		data += struct.pack('d',number)
	self.connection.send(data)

    def is_connected(self):
	return self.connected
