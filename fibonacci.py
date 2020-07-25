a = 1
b = 0

for i in range(0, 89):
    c = a + b
    a=b
    b=c
    print(c)
    
print(c)
