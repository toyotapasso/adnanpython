vars = 'hello world! 123'
num=0
ch=0
sp=0

for var in vars:
    if var.isdigit():
        num=num+1
    elif var.isalpha():
        ch=ch+1
    else:
        sp=sp+1
print("DIGITS  = "+str(num))
print("LETTERS ="+ str(ch))
print("SPECIAL ="+ str(sp))




