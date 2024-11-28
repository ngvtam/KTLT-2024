print("Nguyen Van Tam","\nMSSV: 235752021610054")
n=int(input('Nhap so: '))
for x in range(1,n):
    b=0
    for a in range(1,n):
        if x%a==0:
            b=a+b
    if b>x:
        print('Các số có ước lớn hơn chính nó là:',x)
