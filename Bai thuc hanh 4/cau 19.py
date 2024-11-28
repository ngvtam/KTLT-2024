print("Nguyen Van Tam","\nMSSV: 235752021610054")
n=int(input('Nhap n: '))
print('Cac so nguyen to nho hon',n,'la: ')
for i in range(2,n+1):
    d=0
    for j in range(2,i):
        if i%j==0:
            d=1
    if d==0:
        print(i,end=' ')
        
