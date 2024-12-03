num=10
fibonacci_seq=[0,1]
for x in range(2,num):
    next_fab=fibonacci_seq[x-1]+fibonacci_seq[x-2]
    fibonacci_seq.append(next_fab)
print(fibonacci_seq)