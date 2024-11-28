print("Nguyen Van Tam","\nMSSV: 235752021610054")
class Hinhchunhat(object):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dientich(self):
        return self.chieu_dai * self.chieu_rong

# Tạo một đối tượng Hinhchunhat với chiều dài và chiều rộng cụ thể
hcn = Hinhchunhat(5, 3)

# In diện tích của hình chữ nhật
print(hcn.dientich())

