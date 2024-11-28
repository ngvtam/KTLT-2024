print("Nguyen Van Tam","\nMSSV: 235752021610054")
import math;
print("ax^2 + bx + c = 0")
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
c=float(input("Nhap c: "))
d=(b**2)-(4*a*c)
if d>0:
    e=math.sqrt(d)
    x1=(-b + e)/(2*a)
    x2=(-b - e)/(2*a)
    print("Phuong trinh co 2 nghiem: ")
    print("x1= ",x1,"\nx2= ",x2)
elif d==0:
    print("Phuong trinh co nghiem kep: ")
    print("x= ",-b/(2*a))
else:
    print("Phuong trinh vo nghiem")

