print("Nguyễn Văn Tâm 235752021610054")
try:
    input_file = open("C:/Users/ACER/Documents/KỸ THUẬT LẬP TRÌNH/Bai thuc hanh 7/vd.txt", "r", encoding='utf-8')
    for line in input_file:
        line = line.strip()  # Loại bỏ các ký tự xuống dòng ở cuối mỗi dòng
        reversed_line = line[::-1]
        print(reversed_line)
    input_file.close()
except FileNotFoundError:
    print("Không tìm thấy file: C:/Users/ACER/Documents/KỸ THUẬT LẬP TRÌNH/Bai thuc hanh 7 mẫu/vd.txt")

