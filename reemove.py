import os

folder_path = r"E:\ickala_new\pictures"
# پیدا کردن تمامی فایل‌های عکس در پوشه
image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# تقسیم لیست عکس‌ها به گروه‌های 500 تایی
for i in range(0, len(image_files), 3):
    images = image_files[i:i+3]

input_paths = ' '.join(['"{}"'.format(os.path.join(folder_path, image_file)) for image_file in images])
        

print(input_paths)