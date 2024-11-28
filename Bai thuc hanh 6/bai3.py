print("Nguyen Van Tam","\nMSSV: 235752021610054")
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng của các class con
aNam = Nam()
aNu = Nu()

# In kết quả của phương thức getGender cho mỗi đối tượng
print(aNam.getGender())  # Kết quả: Nam
print(aNu.getGender())   # Kết quả: Nữ

