import time, socket, sys
from ngc_codes import ngc_object

# Config for Socket
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 5051
soc.bind((host_name, port))
print(host_name, f'({ip})')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print(f'Connection Established. Connected From: {addr[0]}, ({addr[1]})')

# Receiving messages
message_string = ""
while True:
    incoming_message = connection.recv(1024)
    incoming_message = incoming_message.decode()
    print(f"Incoming message: {incoming_message}")
    if len(incoming_message) > 1 and '?' in incoming_message: # When receiving from another application
        #print (ngc_object[incoming_message])
        incoming_message = incoming_message.strip('\n')
        try:
            print(f'Response for code {incoming_message}: {ngc_object[incoming_message]}')
            connection.send(f'{ngc_object[incoming_message]}'.encode())
        except Exception as e:
            print (f"Error: {e}")
            connection.send("Unknown code\n".encode())
    elif len(incoming_message) == 1 and '\n' not in incoming_message: # When receiving from a Telnet terminal, chars sent on keystroke
        message_string += incoming_message  # Build received message string
    elif '\n' in incoming_message:
        incoming_message = message_string.strip('\n')
        print(f'received string is: {incoming_message} and that is all')
        try:
            connection.send(f'{ngc_object[incoming_message]}\n\r'.encode())
        except Exception as e:
            print(f"Error: {e}")
            connection.send("Unknown code, please try again\n".encode())
        message_string = ""
    else:
        connection.send("Unknown request\n".encode())
        
