num=int(input("Please Enter Number"))
num_abs=num
add=0
while num_abs>0:
    add=add+num_abs%10
    num_abs//=10
print(f"Sum of numbers upto {num} is {add}")