print("Nguyễn Văn Tâm 235752021610054")
def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("Danh sách đã được ghi vào tệp.")

# Ví dụ sử dụng
data = ['Item 1', 'Item 2', 'Item 3']
write_list_to_file('file.txt', data)  # Thay 'file.txt' bằng tên file bạn muốn ghi
