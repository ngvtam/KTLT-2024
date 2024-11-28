print("Nguyen Van Tam","\nMSSV: 235752021610054")
a,b=1,2
c=0
while b<=40:
    a,b=b,a+b
    print(a,end=" ")
    if a%2==0:
        c=c+a
print("Tong cua cac so chan trong day fibonanci la: ",c)
