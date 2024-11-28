print("Nguyen Van Tam","\nMSSV: 235752021610054")
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

# Tạo một đối tượng Circle với bán kính 2
aCircle = Circle(2)

# In diện tích của hình tròn
print(aCircle.area())


