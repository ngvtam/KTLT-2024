print("Nguyen Van Tam","\nMSSV: 235752021610054")
import numpy as np
dtype =[('name','U20'),('height','f4'),('class','U10')]
a=np.array([
    ('Nguyen Van A',1.65,'10A'),
    ('Pham Thi B',1.55,'10B'),
    ('Tran Van C',1.66,'10C'),
    ('Vu Thi D',1.57,'10D')
],dtype=dtype)
print("Mang ban dau: ",a)
b=np.sort(a,order='height')
print('Mang da sap xep theo chieu cao: ',b)
