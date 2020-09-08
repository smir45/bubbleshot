from converter import bin_dec,dec_bin
from gates import xor
from byte_adder import full_adder

def run():
    while True:
        print()
        print("1. To run the program")
        print("2. To quit the program")
        print()
        wish = int(input("Enter Your Wish: "))
        if wish==1:

            num1 = input('input your first decimal number: ')
            num2 = input('input your second decimal number: ')
            num1 = str(dec_bin(num1))
            num2 = str(dec_bin(num2))
            if len(num1)<len(num2):
                num1 = num1.rjust(len(num2),'0')
            elif len(num2)<len(num1):
                num2 = num2.rjust(len(num1),'0')


            print('1st string of bits is : {}, ({})'.format(num1, bin_dec(num1)))
            print('2nd string of bits is : {}, ({})'.format(num2, bin_dec(num2)))
            result = full_adder(num1, num2)
            print('summarized is         : {}, ({})'.format(result, bin_dec(result)))
        else:
            break

run()