import hashlib
str=input("Enter the string :- ")
result=hashlib.sha256(str.encode())
print("Hash Format of the string is",end="")
print(result.hexdigest())