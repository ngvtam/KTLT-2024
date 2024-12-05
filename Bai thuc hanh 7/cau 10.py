print("Nguyễn Văn Tâm 235752021610054")
def find_longest_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        max_length = max(len(word) for word in words)
        longest_words = [word for word in words if len(word) == max_length]
    
    print("Các từ dài nhất:", longest_words)

# Ví dụ sử dụng
find_longest_words('file.txt')  # Thay 'file.txt' bằng tên file của bạn
