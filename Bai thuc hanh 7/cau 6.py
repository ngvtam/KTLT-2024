print("Nguyen Van Tam","\nMSSV: 235752021610054")
def file_read_from_tail(fname, lines):
    bufsize = 8192
    with open(fname, 'rb') as f:
        fsize = f.seek(0, 2)
        f.seek(0, 0)
        block = f.read(bufsize)
        lines_found = block.count(b'\n')
        while lines_found < lines and fsize > 0:
            f.seek(max(fsize - bufsize, 0))
            block = f.read(min(bufsize, fsize))
            lines_found += block.count(b'\n')
            fsize -= bufsize
        f.seek(0, 0)
        lines_list = block.decode().splitlines()[-lines:]
    for line in lines_list:
        print(line)
file_read_from_tail('C:/Users/LOQ/Documents/HK1/Thực hành KTLT/Python TH_B7/vd.txt', 2)

