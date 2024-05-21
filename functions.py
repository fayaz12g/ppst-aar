import struct
import keystone
from keystone import *
import binascii
import math
import os

def make_hex(x, r):
    p = math.floor(math.log(x, 2))
    a = round(16*(p-2) + x / 2**(p-4))
    if a<0: a += 128
    a = 2*a + 1
    h = hex(a).lstrip('0x').rjust(2,'0').upper()
    hex_value = f'0{r}' + h[1] + '02' + h[0] + '1E' 
    print(hex_value)
    return hex_value

def asm_to_hex(asm_code):
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
    encoding, count = ks.asm(asm_code)
    return ''.join('{:02x}'.format(x) for x in encoding)

def float_to_reversed_hex(num):
    # Round the number to 15 decimal places
    num = round(num, 15)
    
    # Pack the number as a floating point number
    packed = struct.pack('!f', num)
    
    # Convert the packed bytes to hex representation
    full_hex = ''.join('{:02x}'.format(b) for b in packed)
    
    # Reverse the hex in groups of two
    reversed_hex = ''.join([full_hex[i:i+2] for i in range(0, len(full_hex), 2)][::-1])
    
    return reversed_hex

def float2hex(f):
        return hex(struct.unpack('>I', struct.pack('<f', f))[0]).lstrip('0x').rjust(8,'0').upper()
