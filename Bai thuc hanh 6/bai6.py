print("Nguyen Van Tam","\nMSSV: 235752021610054")
class StringManipulation:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        self.user_string = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())

# Tạo đối tượng của class và sử dụng các phương thức
string_obj = StringManipulation()
string_obj.get_String()     # Yêu cầu người dùng nhập một chuỗi
string_obj.print_String()   # In chuỗi đó bằng chữ in hoa

