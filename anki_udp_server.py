import socket
import time

addr0 = "172.27.0.4"
addr1 = "172.27.0.5"
addr2 = "172.27.0.6"

anki0 = {"clockwise": True, "piece": 0}
anki1 = {"clockwise": True, "piece": 0}
anki2 = {"clockwise": False, "piece": 0}

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
      
    if addr[0] == addr2:
        anki2["clockwise"] = clock_wise
        anki2["piece"] = piece

    # Logic part
    anki00 = anki0["piece"]
    anki01 = anki1["piece"]
    anki02 = anki2["piece"]
    if ((anki00== 17 and anki01 == 40) or (anki00 == 40 and anki01)) and anki0["clockwise"] != anki1["clockwise"]:
        message = b"0"
        server.sendto(message, (addr0, 37020))
        server.sendto(message, (addr1, 37020))
