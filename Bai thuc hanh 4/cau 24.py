print("Nguyen Van Tam","\nMSSV: 235752021610054")
n=input('Nhap chuoi: ')
h,t=0,0
for a in n:
    if a.isupper():
        h+=1
    elif a.islower():
        t+=1
print('Chuoi co ',h,'chu hoa')
print('Chuoi co ',t,'chu thuong')
