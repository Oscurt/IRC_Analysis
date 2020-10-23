def fun2(packet):
    try:
        if packet['IP']['proto'] == 6:
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'NICK':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = data[0]+' '+'name'
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None
    