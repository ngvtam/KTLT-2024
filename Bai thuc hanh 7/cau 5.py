print("Nguyen Van Tam","\nMSSV: 235752021610054")
def file_read(fname):
    try:
        with open(fname, "w") as myfile:
            myfile.write("Some content")
    except OSError as e:
        print(f"OSError: {e}")


file_read("C:/Users/LOQ/Documents/HK1/Thực hành KTLT/Python TH_B7/vd.txt")
