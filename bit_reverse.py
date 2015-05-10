def bit_reverse(num):
    bits = list('{:032b}'.format(num))
    bits.reverse()
    return int(''.join(bits), 2)
