print("Nguyen Van Tam","\nMSSV: 235752021610054")
class Reverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Dữ liệu vào
input_text = 'hello .py'

# Tạo đối tượng Reverser và đảo ngược chuỗi
reverser = Reverser(input_text)
result = reverser.reverse_words()

# In kết quả
print(f"Đầu vào: '{input_text}'")
print(f"Đầu ra: '{result}'")
