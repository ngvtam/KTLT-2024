print("Nguyễn Văn Tâm 235752021610054")
def doc_file(fname):
    try:
        with open(fname, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"FileNotFoundError: Không tìm thấy tệp '{fname}'")
fname = "C:/Users/ACER/Documents/KỸ THUẬT LẬP TRÌNH/Bai thuc hanh 7/vd.txt"
print("Số dòng trong tệp là:", doc_file(fname))
