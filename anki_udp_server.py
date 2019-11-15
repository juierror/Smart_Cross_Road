import socket
import time

addr0 = "172.27.0.4"
addr1 = "172.27.0.5"

anki0 = {"clockwise": True, "piece": 0}
anki1 = {"clockwise": True, "piece": 0}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.bind(("", 44444))

while True:
    data, addr = server.recvfrom(1024)
    clock_wise, piece = str(data).strip().split()
    clock_wise = clock_wise[:-1]
    piece = piece[:-1]

    # Save data part
    if addr[0] == addr0:
        anki0["clockwise"] = clock_wise
        anki0["piece"] = piece

    if addr[0] == addr1:
        anki1["clockwise"] = clock_wise
        anki1["piece"] = piece

    # Logic part
    if ((anki0["piece"] == 17 and anki1["piece"] == 40) or (anki0["piece"] == 40 and anki1["piece"] == 17)) and anki0["clockwise"] != anki1["clockwise"]:
        message = b"0"
        server.sendto(message, (addr0, 37020))
        server.sendto(message, (addr1, 37020))
