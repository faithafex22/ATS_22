

def convert(binary):
    power = 0
    num = 0
    while binary > 0:
        num = num + ((binary % 10) * 2**power)
        binary = binary // 10
        power += 1
    return num

print(convert(101))
