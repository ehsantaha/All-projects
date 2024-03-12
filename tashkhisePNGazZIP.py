import os
import shutil

def move_png_images(source_dir, destination_dir):
    # ایجاد دایرکتوری مقصد اگر وجود ندارد
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # اسکن کردن فایل‌ها در دایرکتوری مبدا
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        # چک کردن آیا فایل یک عکس PNG است
        if os.path.isfile(source_file) and filename.lower().endswith('.png'):
            # مسیر فایل عکس در دایرکتوری مقصد
            destination_file = os.path.join(destination_dir, filename)
            # کپی کردن فایل عکس به دایرکتوری مقصد
            shutil.copy(source_file, destination_file)
            # حذف فایل مبدا
            os.remove(source_file)

# مسیر فولدر مبدا
source_folder = r'C:\\Users\\ehsan\\Downloads'
# مسیر دایرکتوری مقصد
destination_folder = r'E:\\ickala_new\\backgroud_ok'

# فراخوانی تابع برای جابجایی عکس‌های PNG
move_png_images(source_folder, destination_folder)
