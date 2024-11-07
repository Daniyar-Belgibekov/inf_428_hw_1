import math



def to_cyclic(time):
    angle = (time / 24) * 2 * math.pi
    sin_val = math.sin(angle)
    cos_val = math.cos(angle)
    return [sin_val, cos_val]


def main():
    time1 = to_cyclic(21)
    time2 = to_cyclic(5)
    difference = math.acos(time1[0] * time2[0] + time1[1] * time2[1]) * (24 / (2 * math.pi))
    print(difference)


main()