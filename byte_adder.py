from gates import xor


def full_adder(first,last):
    c_out = 0
    result = ''
    for i in range(len(first)-1,-1,-1):
        sum_ = xor(xor(int(first[i]),int(last[i])),c_out)
        c_out = (int(first[i]) and int(last[i])) or (c_out and (xor(int(first[i]),int(last[i]))))
        result += str(sum_)
    result+=str(c_out)
    return result[::-1]