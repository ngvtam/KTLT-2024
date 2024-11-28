print("Nguyen Van Tam","\nMSSV: 235752021610054")
def doc_file(fname):
    try:
        with open(fname, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"FileNotFoundError: Không tìm thấy tệp '{fname}'")
fname = "C:/Users/LOQ/Documents/HK1/Thực hành KTLT/Python TH_B7/vd.txt"
print("Số dòng trong tệp là:", doc_file(fname))
