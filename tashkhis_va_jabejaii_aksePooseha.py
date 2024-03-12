import os
import shutil

# مسیر دایرکتوری حاوی پوشه‌ها
directory_with_folders = r"E:\ickala_new\backgroud_ok"

# مسیر دایرکتوری حاوی فایل‌ها
directory_with_files = r"E:\ickala_new\pictures"

# مسیر دایرکتوری مقصد برای جابجایی فایل‌ها
destination_directory = r"E:\ickala_new\New folder"

# لیست پوشه‌های موجود در دایرکتوری
folders = os.listdir(directory_with_folders)

# لیست فایل‌های موجود در دایرکتوری حاوی فایل‌ها
files = os.listdir(directory_with_files)


folders = [os.path.splitext(folder)[0] for folder in folders]

# لیست نام‌های فایل‌ها بدون پسوند
file_names = [os.path.splitext(file)[0] for file in files]

for file_name in file_names:
    # اگر نام فایل با نام یکی از پوشه‌ها مطابقت داشته باشد، آن فایل را به دایرکتوری مقصد منتقل کنید
    if file_name in folders:
        # مسیر کامل فایل اصلی
        file_path = os.path.join(directory_with_files, file_name + '.jpg')
        
        # مسیر کامل فایل مقصد
        destination_path = os.path.join(destination_directory, file_name + '.jpg')
        
        # جابجایی فایل
        shutil.move(file_path, destination_path)
        print(f"فایل {file_name} به مسیر {destination_path} منتقل شد.")
    else:
        print(f"فایل {file_name} با هیچ پوشه‌ای مطابقت نداشته و به دایرکتوری مقصد منتقل نشد.")
