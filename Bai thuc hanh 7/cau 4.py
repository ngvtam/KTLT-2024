print("Nguyen Van Tam","\nMSSV: 235752021610054")
def file_read_from_head(fname,nline):
    from itertools import islice
    with open (fname) as f:
        for line in islice(f,nline):
            print(line)
file_read_from_head("C:/Users/LOQ/Documents/HK1/Thực hành KTLT/Python TH_B7/vd.txt",2)
