print("Nguyễn Văn Tâm 235752021610054")
def copy_file_content(source_file, destination_file):
    # Mở file nguồn với encoding 'utf-8'
    with open(source_file, 'r', encoding='utf-8') as src:
        content = src.read()
    # Mở file đích với encoding 'utf-8'
    with open(destination_file, 'w', encoding='utf-8') as dest:
        dest.write(content)
    print("Nội dung đã được sao chép.")

# Ví dụ sử dụng
copy_file_content('source.txt', 'destination.txt')  # Đảm bảo 'source.txt' đã tồn tại
