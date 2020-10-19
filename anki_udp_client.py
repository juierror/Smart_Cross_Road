import socket
from overdrive import Overdrive

tmp_clockwise = True
tmp_piece = 0

def locationChangeCallback(addr, location, piece, speed, clockwise):
    global tmp_clockwise, tmp_piece
    print(" Location from " + addr + " : " + "Piece=" +
          str(piece) + " Location=" + str(location) + " Clockwise=" + str(clockwise))
    tmp_clockwise = str(clockwise)
    tmp_piece = str(piece)


# UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.settimeout(0.1)
client.bind(("", 37020))

# Anki
car = Overdrive("E2:81:E9:52:65:97")
car.setLocationChangeCallback(locationChangeCallback)
car.changeSpeed(200, 300)

while True:
    message = str(tmp_clockwise) + " " + str(tmp_piece)
    client.sendto(message, ('172.27.0.3', 44444))
    data, addr = client.recvfrom(1024)
    if data == "0":
        car.changeSpeed(0, 1000)
input()
