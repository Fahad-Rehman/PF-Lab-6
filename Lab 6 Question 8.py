def converter(start_point, end_point):
    print('\t\t\tDecimal\t\t\t\t\t\t\tBinary\t\t\t\t\t\t  Octal\t\t\t\t\t\t  Hexa-decimal')
    for i in range(start_point, end_point):
        print('The value in decimal system is: {0}\tin binary system is: {1}\t in octal system is: {2}\t in hexa-decimal system is: {3}'.format(i, bin(i), oct(i), hex(i)))

converter(1, 6)