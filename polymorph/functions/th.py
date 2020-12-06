def th(packet):
    from datetime import datetime
    if (packet['TCP']['dstport'] == 6667 or packet['TCP']['srcport'] == 6667):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time + " " + str(packet['IP']['len']))
    return packet
