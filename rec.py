import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = "10.1.0.80" # Enter you valid ip address of the network
port_no = 2525

complete_address = (ip_address, port_no)
s.bind(complete_address)

print("Ready for communication")

# Keep the socket open to receive messages
while True:
    message = s.recvfrom(100)
    print(message)
