"""
This is the working python interface for wifi communication for the HAMR (as of 11/14/2016)
If not working- be sure to check the ip address of the HAMR and make sure it matches with
the first value in the address tuple.
Also be sure that the second int for the tuple (the local port) matches up.
Also be sure that the message type is the same.
"""
import socket
import struct

SERVER_IP = '192.168.1.1'
SERVER_PORT = 2390
address = (SERVER_IP, SERVER_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP

# arbitrarily set message_type as 103
message_type = 103

def message_generator(message_type, data=[]):
    # test message takes three ints and turns them into floats.
    msg = chr(message_type)
    msg += struct.pack("<" + 'fff', *data)
    return msg

def send_message(message):
    for _ in range(0, 2):
        sock.sendto(message, address)

while True:
    print 'What values?'
    answer = raw_input("")
    data = answer.split(" ")
    converted_data = []
    for i in data:
        print float(i)
        converted_data.append(float(i))

    message = message_generator(message_type, converted_data)
    send_message(message)
