number=int(input("Please Enter Number"))
Entered_num=number
fact=1
if number>0:
    while number >0:
     fact=fact*number
     number=number-1
    print(f"Factorial of {Entered_num} is {fact}")
elif number==0:
 print(f"Fictorial of {Entered_num} is {fact}")
else:
 print("There is no factorial of Negative Number")