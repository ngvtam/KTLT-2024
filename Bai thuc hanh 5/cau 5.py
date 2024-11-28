print("Nguyen Van Tam","\nMSSV: 235752021610054")
from my_module import sap_xep,lon_nhat,nho_nhat
def main():
    n=int(input("Nhap so luong phan tu: "))
    danh_sach=[]
    for i in range(n):
        gia_tri=float(input(f'Nhap gia tri phan tu thu {i+1}: '))
        danh_sach.append(gia_tri)
    danhsach = sap_xep(danh_sach)
    lonnhat=lon_nhat(danh_sach)
    nhonhat=nho_nhat(danh_sach)
    print("danh sach sawps xep: ", danhsach)
    print("Phan tu lon nhat: ", lonnhat)
    print("Phan tu nho nhat: ", nhonhat)
if __name__=="__main__":
    main()
       
