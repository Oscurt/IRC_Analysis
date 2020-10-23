def fun1(packet):
    try:
        if packet['IP']['proto'] == 6:
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'PRIVMSG':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = data[0]+' '+data[1]+' :HACKEADO\r\n'
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None
    