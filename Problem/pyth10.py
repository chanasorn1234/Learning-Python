x = int(input())
m,n,p =0,0,0
while (x>=1000):
    x -= 1000
    m += 1
while (x>=500):
    x -= 500
    n += 1
while (x>=100):
    x -= 100
    p += 1

print("1000 *",m)
print("500 *",n)
print("100 *",p)