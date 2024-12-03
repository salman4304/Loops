num=int(input("Please Enter an Integer Number"))
num_abs=abs(num)
count=0
while num_abs>0:
    num_abs=num_abs//10
    count=count+1
print(f"Number of digits in {num} are {count}")
