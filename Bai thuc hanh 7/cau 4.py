print("Nguyễn Văn Tâm 235752021610054")
def file_read_from_head(fname,nline):
    from itertools import islice
    with open (fname) as f:
        for line in islice(f,nline):
            print(line)
file_read_from_head("C:/Users/ACER/Documents/KỸ THUẬT LẬP TRÌNH/Bai thuc hanh 7/vd.txt",2)
