print("Nguyễn Văn Tâm 235752021610054")
def file_read(fname):
    try:
        with open(fname, "w") as myfile:
            myfile.write("Some content")
    except OSError as e:
        print(f"OSError: {e}")


file_read("C:/Users/ACER/Documents/KỸ THUẬT LẬP TRÌNH/Bai thuc hanh 7/vd.txt")
