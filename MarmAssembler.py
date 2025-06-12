# Matthew McCaughan
# CPU PROJECT
# Project 2 Assembler


# HELPER FUNCTIONS FOR ASSEMBLER


# rule based code to translate instruction text into 2 bit equivalent
def identify(x):
    if x == "ADD":
        return "00"
    if x == "SUB":
        return "01"
    if x == "LDR":
        return "10"
    if x == "M0":
        return "00"
    if x == "M1":
        return "01"
    if x == "M2":
        return "10"
    if x == "M3":
        return "11"
    if x == "0":
        return "00"
    if x == "1":
        return "01"
    if x == "2":
        return "10"
    if x == "3":
        return "11"
    if x == "00":
        return "00"
    else:
        return x

# Converts binary to hex (4 bits to 1 binary)
# adapted from GeeksforGeeks
# https://www.geeksforgeeks.org/python-program-to-convert-binary-to-hexadecimal/
def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
      
    # counter to check group of 4
    count = 1
      
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
      
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
          
        # check if group of 4 completed
        if count % 4 == 0:
            
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
              
        # group of 4 is not completed
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
          
    # check if at end the group of 4 is not
    # completed
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
          
    # check at end the group of 4 is completed
    if count == 1:
        i = i-1
          
    # printing hexadecimal number
    # array in reverse order
    result = []
    while i >= 0:
        
        result.append(hexaDeciNum[i])
        i = i-1
    return result


print("*********************************************************************************************")
print("MATTHEW MCCAUGHAN")
print("CPU PROJECT FALL 2022")
print("M-ARM ASSEMBLER 1.0")
print("FOR USE IN ASSEMBLING CPU INSTRUCTION MEMORY")
print("--------------------")
print("ACCEPTED INSTRUCTION FORMATTING:")
print("LDR Md # 00")
print("ADD Md Ma Mb")
print("SUB Md Ma Mb")
print("--------------------")
print("INPUT FORMATTING:")
print("Please input instuctions one at a time per prompt, when done, please input 'n' when prompted")
print("Instructions are case sensitve (all caps)")
print("(y/n) inputs are lowercase")
print("!! Accepts up to 16 Instructions !!")
print("*********************************************************************************************")
print("Enter your instructions below:")

inslist = []
response = ""
counter = 1

while response != "n":
    print("Enter Instruction", counter, ":")
    instructions = input()
    if instructions == "quit":
        break
    x = instructions.split()
    inslist.append(x)
    response = input("Add another instruction? (y/n): ")
    counter = counter + 1

if response == "n":
    print("")
    print("--------------------")
    print("This is your program!")
    print("")

    for i in range(len(inslist)):
        print(inslist[i])
    print("")
    print("--------------------")
    response2 = input("Is this input correct? (y/n): ")
    if response2 != "n":
        pass
    else:
        print("")
        print("")
        print("Please re-run this program!")
        raise Exception("Not Happy With Program Exception :-(" )
    
binlist = []
for i in range(len(inslist)):
    for j in range(len(inslist[i])):
        a = (identify(inslist[i][j]))
        binlist.append(a)

subList = [binlist[n:n+4] for n in range(0, len(binlist), 4)]


for i in range(len(subList)):
    b = subList[i]
    b = "".join(b)
    subList[i] = b
               

for i in range(len(subList)):
    h = binToHexa(subList[i])
    h = "".join(h)
    subList[i] = h

with open('Instructions.txt','w') as f:
    f.write("v3.0 hex words addressed")
    f.write('\n')
    f.write("00: ")
    
    for line in subList:
        f.write(line)
        f.write(" ")

    for line in range(16 - len(subList)):
        f.write("00")
        f.write(" ")

print("")
print("Success! Text File Generated at 'Instructions.txt'")
print("Remember, Data Memory must be hardcoded!")
