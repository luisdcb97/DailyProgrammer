import time


def baum_sweet(num: int):
    if num < 0:
        raise ValueError("Number has to be greater or equal to 0")
    binary = bin(num)[2:]
    length = 0
    for bit in reversed(binary):
        if bit != '0':
            if length % 2 != 0:
                return 0
            length = 0
            continue
        length += 1
    else:
        return 1


def baum_sweet_generator(stop: int, start: int = 0):
    if stop < 0 or start < 0:
        raise ValueError("Number has to be greater or equal to 0")
    elif start > stop:
        raise ValueError("Start has to be after stop")

    for val in range(start, stop + 1):
        yield baum_sweet(val)


def baum_sweet_sequence(stop: int, start: int = 0):
    if stop < 0 or start < 0:
        raise ValueError("Number has to be greater or equal to 0")
    elif start > stop:
        raise ValueError("Start has to be after stop")

    return [baum_sweet(val) for val in range(start, stop + 1)]


def baum_sweet_sequence_by_generator(stop: int, start: int = 0):
    if stop < 0 or start < 0:
        raise ValueError("Number has to be greater or equal to 0")
    elif start > stop:
        raise ValueError("Start has to be after stop")
    return [val for val in baum_sweet_generator(stop, start)]


if __name__ == '__main__':
    stop_value = int(input("Stop At Value (INCLUDING):"))
    start_value = int(input("Start At Value (DEFAULT=0):") or "0")
    time_table = {
        "List": 0,
        "Generator": 0,
    }
    time_start = time.time()
    list_seq = baum_sweet_sequence(stop_value, start_value)
    time_table["List"] = time.time() - time_start

    time_start = time.time()
    list_gen = baum_sweet_sequence_by_generator(stop_value, start_value)
    time_table["Generator"] = time.time() - time_start

    print("Value", "List", "Generator", "Binary")
    for val in range(start_value, stop_value + 1):
        print(val, list_seq[val - start_value], list_gen[val - start_value],
              bin(val)[2:])

    print("Times:", time_table)
