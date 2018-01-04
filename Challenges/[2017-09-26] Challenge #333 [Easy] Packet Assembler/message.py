from packet import Packet
from typing import List


class Message(object):
    def __init__(self, _id: int = 0, size: int = 0):
        self.packets: List[Packet] = []
        self.id: int = _id
        self.size: int = size

    def add_packet(self, packet: Packet):
        if packet.message_id != self.id:
            raise ValueError("Packet must belong to the message")
        elif packet.total != self.size:
            raise ValueError("Packet must have the same message size")
        elif packet.packet_id >= self.size:
            raise ValueError("Packet must be within message size")
        elif packet in self.packets:
            raise ValueError("Packet already in message")

        self.packets.append(packet)

    def sort(self):
        self.packets.sort()

    def print(self):
        self.sort()
        print(self.id, self.size, ":")
        for packet in self.packets:
            print(end="\t")
            packet.print()
