num=[2,3,5,6,8]
num_search=7
for x in range(len(num)):
    if num_search==num[x]:
        print(f"{num_search} is found")
        break
else:
 print(f"{num_search} is not found")