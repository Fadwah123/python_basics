def rec_sum(n):
    if n==1:
        return 1
    else:
        return n + rec_sum(n-1)
num=int(input("Enter a number:"))
output=rec_sum(num)
print(f"Sum from 1 to {num} is:{output}")
