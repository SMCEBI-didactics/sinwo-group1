"""
"""

def compute(address, mask):
    """ Funkcja przeliczająca adres IP.

        Args:
            address (str): Adres IP.
            mask (str): Maska IP.

        Returns:
            str: Binary address name.
            str: Klasa.
            str: Adres rozgłoszeniowy.
            str: Zakres górny.
            str: Zakres dolny.

    """
    address = address.split(".")
    mask = mask.split(".")

    if len(address) != 4 or len(mask) != 4:
        print("error")


    address = [bin(int(oktet))[2:] for oktet in address]
    mask = [bin(int(oktet))[2:] for oktet in mask]

    binary_address = []
    for oktet in address:
        final = oktet
        while len(final) < 8:
            final = "0" + final
        binary_address.append(final)
        
    binary_mask = []
    for oktet in mask:
        final = oktet
        while len(final) < 8:
            final = "0" + final
        binary_mask.append(final)    

    binary_address_name = []
    for x in range(len(binary_address)):
        oktet = ""
        for y in range(len(binary_address[x])):
            if binary_address[x][y] == "1" and binary_mask[x][y] == "1":
                oktet += "1"
            else:
                oktet += "0"
        binary_address_name.append(oktet)
        
    broadcast_address = []
    for x in range(len(binary_address)):
        oktet = ""
        for y in range(len(binary_address[x])):
            if binary_mask[x][y] == "0":
                oktet += "1"
            else:
                oktet += binary_address[x][y]
        broadcast_address.append(oktet)
        
    binary_address_name = ".".join([str(int(oktet, 2)) for oktet in binary_address_name])
    broadcast_address = ".".join([str(int(oktet, 2)) for oktet in broadcast_address])

    if int(binary_address_name.split(".")[0]) >= 1 and int(binary_address_name.split(".")[0]) < 128:
        klasa = "A"
    elif int(binary_address_name.split(".")[0]) >= 128 and int(binary_address_name.split(".")[0]) < 192:
        klasa = "B"
    elif int(binary_address_name.split(".")[0]) >= 192 and int(binary_address_name.split(".")[0]) < 224:
        klasa = "C"
    elif int(binary_address_name.split(".")[0]) >= 224 and int(binary_address_name.split(".")[0]) < 240:
        klasa = "D"
    else:
        klasa = "E"
        
    range_down = ".".join(binary_address_name.split(".")[0:3]) + "." + str(int(binary_address_name.split(".")[3])+1)
    range_up = ".".join(broadcast_address.split(".")[0:3]) + "." + str(int(broadcast_address.split(".")[3])-1) 
    return binary_address_name, klasa, broadcast_address, range_up, range_down
    


