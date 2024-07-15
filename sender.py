import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
# target_ip = "127.0.0.1"
target_ip = "10.1.0.80" # Enter the correct ip address of your network
port_no = 2525
target_address = (target_ip, port_no)

while True:
    message = input("Please drop your message here : ")
    encrypt_message = message.encode('ascii')
    s.sendto(encrypt_message, target_address)