def fun3(packet):
    try:
        if packet['IP']['proto'] == 6:
            data = packet['IRC']['request'].split(" ")
            if data[0] == 'JOIN':
                print(packet['IRC']['request'])
                packet['IRC']['request'] = data[0]+' '+'#hack'
                print(packet['IRC']['request'])
                return packet
    except:
        print("except")
        return None
    