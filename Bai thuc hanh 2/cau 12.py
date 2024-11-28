print("Nguyen Van Tam","\nMSSV: 235752021610054")
import re
a=input("Nhap mat khau: ")
if len(a)<6 or len(a)>12:
    print("Mat khau phai lon hon 6 ki tu va nho hon 12 ki tu")
else:
    if not re.search("[0-9]",a):
        print("Mat khau phai chua it nhat 1 chu so")
    elif not re.search("[A-Z]",a):
        print("Mat khau phai chua it nhat 1 ki tu hoa")
    elif not re.search("[a-z]",a):
        print("Mat khau phai chua it nhat 1 ki tu thuong")
    elif not re.search("[!@#$%^&?]",a):
        print("Mat khau phai chua ki tu dac biet")
    else:
        print("Xac nhan lai mat khau: ",a)

