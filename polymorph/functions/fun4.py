def fun4(packet):
    try:
        if packet['IP']['proto'] == 6:
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'PING' or data[0] == 'PONG':
                packet['IRC']['request'] = 'NICK hack'
                print("change")
                return packet
    except:
        print("except")
        return None
    