print("Nguyen Van Tam","\nMSSV: 235752021610054")
n=input('Nhap vao danh sach: ')
n=n.replace(",","")
a=list(n)
for b in a :
    c=int(b)
    if c%2!=0:
        print(c,end=',')

