N = int(input("Enter the number of baskets: "))
w = int(input("Enter the weight of real coins: "))
d = int(input("Enter the weight difference of counterfeit coins: "))
P = int(input("Enter the total weight of selected coins: "))

sum = (N - 1) * N / 2
tmp = sum * w
ans = int((tmp - P) / d)

if ans > 0:
    print(ans)
else:
    print(N)