#! /usr/bin/env python


myPass = [None] * 32

myPass[0]  = 'd'
myPass[29] = '9'
myPass[4]  = 'r'
myPass[2]  = '5'
myPass[23] = 'r'
myPass[3]  = 'c'
myPass[17] = '4'
myPass[1]  = '3'
myPass[7]  = 'b'
myPass[10] = '_'
myPass[5]  = '4'
myPass[9]  = '3'
myPass[11] = 't'
myPass[15] = 'c'
myPass[8]  = 'l'
myPass[12] = 'H'
myPass[20] = 'c'
myPass[14] = '_'
myPass[6]  = 'm'
myPass[24] = '5'
myPass[18] = 'r'
myPass[13] = '3'
myPass[19] = '4'
myPass[21] = 'T'
myPass[16] = 'H'
myPass[27] = '5'
myPass[30] = '2'
myPass[25] = '_'
myPass[22] = '3'
myPass[28] = '0'
myPass[26] = '7'
myPass[31] = 'e'

print("picoCTF{{{}}}".format(''.join(myPass)))
