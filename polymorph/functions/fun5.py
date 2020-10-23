def fun5(packet):
    try:
        if packet['IP']['proto'] == 6:
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'JOIN':
                packet['IRC']['request'] = 'QUIT : WeeChat2.9'
                print('desconectalo')
                return packet
    except:
        print("except")
        return None
    