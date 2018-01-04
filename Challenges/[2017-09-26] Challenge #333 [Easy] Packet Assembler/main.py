from packet import Packet
from message import Message
from typing import List


def read_file(filename: str):
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
    return lines


def create_packets(lines: List[str]):
    packets = []
    for line in lines:
        m_id, p_id, size, *info = line.split(maxsplit=3)
        m_id, p_id, size = map(int, [m_id, p_id, size])
        info = "" if info == [] else info[0].rstrip()
        packets.append(Packet(m_id, p_id, size, info))
    return packets


def create_messages(packets: List[Packet]):
    messages = {}
    for packet in packets:
        message = messages.setdefault(packet.message_id,
                                      Message(packet.message_id, packet.total))
        message.add_packet(packet)
    return list(messages.values())


if __name__ == '__main__':
    challenge_input = read_file("input.txt")
    packets = create_packets(challenge_input)
    messages = create_messages(packets)
    for message in messages:
        message.print()
