#Danh sách để lưu các công việc
tast = []
def add_task(task_name):
"""thêm một công việc mới vào danh sách."""
tasks.append(task_name)
print(f"Đã thêm công việc:'{task_name}'")
#___Điểm bắt đầu của chương trình___
if __name__=="__main__":
print("Chào mừng đến với ứng dụng To do List!")
add_task("Học bài Git và GitHub")
add_task("Làm bài thực hành ở nhà")