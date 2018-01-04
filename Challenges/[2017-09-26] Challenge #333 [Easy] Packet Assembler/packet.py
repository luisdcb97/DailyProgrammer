class Packet(object):
    def __init__(self, message_id: int, packet_id: int, total_packets: int,
                 information: str):
        self.message_id = message_id
        self.packet_id = packet_id
        self.total = total_packets
        self.information = information

    def __lt__(self, other):
        return self.packet_id < other.packet_id

    def print(self):
        print(self.packet_id, self.information)
