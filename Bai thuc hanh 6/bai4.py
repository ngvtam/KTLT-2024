print("Nguyen Van Tam","\nMSSV: 235752021610054")
class RomanToInteger:
    def __init__(self, roman):
        self.roman = roman
        self.roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convert(self):
        num = 0
        prev_value = 0
        for char in reversed(self.roman):
            value = self.roman_dict[char]
            if value < prev_value:
                num -= value
            else:
                num += value
            prev_value = value
        return num

# Tạo đối tượng RomanToInteger và chuyển đổi số La Mã
roman_number = "XIV"
converter = RomanToInteger(roman_number)
result = converter.convert()
print(f"Số La Mã {roman_number} chuyển đổi thành {result}")

