from digit_convertion import *
if __name__ == '__main__':
    try:
        number = int(input('enter a number\n'))
        digit = int(input('enter a digit\n'))
    except Exception:
        print('pass in parameter errot')
    method = Convertion(digit, number)
    print(method.calculation())