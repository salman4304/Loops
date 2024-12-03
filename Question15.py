num=int(input("Please Enter Number"))
odd_sum=0
even_sum=0
for x in range(1,num+1):
    if x%2!=0:
        odd_sum=odd_sum+x
    else:
        even_sum=even_sum+x
print(f"Even numbers sum upto {num} is {even_sum}")
print(f"Odd numbers sum upto {num} is {odd_sum}")