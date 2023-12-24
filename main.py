import socket

#FriendlyFiberCraft
FriendlyFiberCraftIp = "116.202.216.91"
FriendlyFiberCraftPortRange = {27015: "Ragnarok",27016: "Fjordur",27017: "Genesis 2",27018: "The Center",27019: "Extinction",27020: "Valguero",27021: "The Island"}


def Check_if_up(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        sock.connect_ex((ip,port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
total = 0
for port in FriendlyFiberCraftPortRange:
    openPort = Check_if_up(FriendlyFiberCraftIp,port)
    if openPort == True:
        print(f"Port : {port} open with map : {FriendlyFiberCraftPortRange.get(port)}")
        total += 1
    

percentatge = f'{round(total/7*100,2)}%'
