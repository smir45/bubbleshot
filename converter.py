def dec_bin(num):
    num = int(num)
    num = bin(num).replace('0b','')
    return int(num)

def bin_dec(number):
    return int(number,2)