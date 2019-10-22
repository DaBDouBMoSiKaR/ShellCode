#!/usr/bin/python

import argparse
import sys
import struct
import os


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encoder", help="The encoder to use ex: xor")
parser.add_argument("-l", "--list", action="store_true", help="List of Encoded")
parser.add_argument("-f", "--find", action="store_true", help="Find magic byte encoder in shellcode")
parser.add_argument("-s", "--shellcode", help="Shellcode")
parser.add_argument("-b", "--bytes", help="byte to encode the shellcode 'Xor, Insertion'")
args = parser.parse_args()


if args.list:
	print "Xor encoded JMP CALL"
	print "Not encoded JMP CALL"
	sys.exit(0)

if args.encoder:
	encoder = args.encoder
	if encoder.upper() not in ["XOR", "NOT", "INSERTION"]:
		print "\x1b[0;30;41mEncoder not found please see the help for more detail\x1b[0m"
	else:
		encoded =""
		encoded2=""
		if encoder.upper() == "XOR":
			if args.bytes:
				
				magic = args.bytes.replace("\\x", "").decode("hex")
				
				if args.shellcode:
					print "\x1b[0;30;43mOld shellcode : \x1b[0m" +  args.shellcode
					bits = args.shellcode.replace("\\x", "").decode("hex")
					if magic in bytearray(bits):
						print "\x1b[0;30;41mYour magic byte was found in the shellcode, the encoded shellcode will not work please use -f to find a valid magic byte\x1b[0m"
						sys.exit(-5)
					for code in bytearray(bits):
						code^=struct.unpack("B", magic)[0]
        				encoded += "\\x"
        				encoded += "%02x" % code

        				encoded2 +="0x"
        				encoded2 += "%02x, " % code



					print "\x1b[6;30;42mC format :\x1b[0m%s" % encoded
					print "\x1b[6;30;42mNasm format :\x1b[0m %s" %encoded2

					print "\x1b[6;30;42mLen of shellcode :\x1b[0m %d" % len(bytearray(bits))
				else:
					print "\x1b[0;30;41mYou must spesifie the shellcode, use -s \"\\0xE9\\0x030\\0x44...\".\x1b[0m"
		elif encoder.upper() == "NOT":
			if args.shellcode:
				print "\x1b[0;30;43mOld shellcode : \x1b[0m" +  args.shellcode
				bits = args.shellcode.replace("\\x", "").decode("hex")
				for code in bytearray(bits):
					code=~code
					encoded += "\\x"
					encoded += "%02x" % (code & 0xff)
					
					encoded2 +="0x"
					encoded2 += "%02x, " % (code & 0xff)
					
                		print "\x1b[6;30;42mC format :\x1b[0m%s" % encoded
				print "\x1b[6;30;42mNasm format :\x1b[0m %s" %encoded2
				
				print "\x1b[6;30;42mLen of shellcode :\x1b[0m %d" % len(bytearray(bits))
			else:
				print "\x1b[0;30;41mYou must spesifie the shellcode, use -s \"\\0xE9\\0x030\\0x44...\".\x1b[0m"
		elif encoder.upper() == "INSERTION":
			if args.shellcode:
				if args.bytes:
					print "\x1b[0;30;43mOld shellcode : \x1b[0m" +  args.shellcode
					bits = args.shellcode.replace("\\x", "").decode("hex")
					magic = args.bytes.replace("\\x", "").decode("hex")
					for code in bytearray(bits):
						encoded += "\\0x"
						encoded += "%02x, " % code
						encoded += "\\0x%02x, " % struct.unpack("B", magic)[0]
						
						encoded2 +="0x"
						encoded2 += "%02x, " %code
						encoded2 += "0x%02x, " % struct.unpack("B", magic)[0]
					
                			print "\x1b[6;30;42mC format :\x1b[0m%s" % encoded
					print "\x1b[6;30;42mNasm format :\x1b[0m %s" %encoded2
				
					print "\x1b[6;30;42mLen of shellcode :\x1b[0m %d" % (len(bytearray(bits))*2)
				else:
					print "\x1b[0;30;41mYou must spesifie the byte, use -b \"\\0xAA\".\x1b[0m"
			else:
				print "\x1b[0;30;41mYou must spesifie the shellcode, use -s \"\\0xE9\\0x030\\0x44...\".\x1b[0m"
		else:
			print "\x1b[0;30;41mEncoder not found, use help to list all encoder.\x1b[0m"
	sys.exit(0)
if args.find:
	found = ""
	num = 0	
	if args.shellcode:
		bits = args.shellcode.replace("\\x", "").decode("hex")
		for x in range(1, 256):
			if x not in bytearray(bits):
				if x==255:
					found+="0x%02x" %x
					num+=1
				else:
					found += "0x%02x, " % x
					num+=1
		if num != 0:
			print "\x1b[6;30;43m%d byte(s) was found to use it\x1b[0m" % num
			print found
		else:
			print "Nothing was found"
	else:
		print "You must add a shellcode"
	sys.exit(0)


