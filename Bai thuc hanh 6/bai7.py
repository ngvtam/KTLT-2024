print("Nguyen Van Tam","\nMSSV: 235752021610054")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def circumference(self):
        return 2 * 3.14159 * self.radius

# Tạo đối tượng Circle với bán kính 5
circle = Circle(5)

# Tính diện tích và chu vi của hình tròn
print(f"Diện tích hình tròn: {circle.area()}")
print(f"Chu vi hình tròn: {circle.circumference()}")

