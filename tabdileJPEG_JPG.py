import cv2
import os

# مسیر پوشه حاوی تصاویر
input_folder = r"E:\ickala_new\remove_watermark"
# مسیر پوشه برای ذخیره تصاویر تبدیل شده
output_folder = r"E:\ickala_new\jpg no watermark"

# اطمینان حاصل کنید که پوشه خروجی وجود دارد
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# لیست کردن تمام فایل‌های در پوشه ورودی
image_files = os.listdir(input_folder)

# حلقه اصلی بر روی تصاویر
for image_file in image_files:
    # اگر فایل از نوع JPEG باشد
    if image_file.endswith(".jpeg") or image_file.endswith(".jpg"):
        # مسیر کامل فایل ورودی
        input_path = os.path.join(input_folder, image_file)
        # مسیر کامل فایل خروجی (با پسوند جدید)
        output_path = os.path.join(output_folder, image_file.replace(".jpeg", ".jpg").replace(".jpg", ".jpg"))
        
        # خواندن تصویر
        image = cv2.imread(input_path)
        
        # نوشتن تصویر به فرمت JPEG
        cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        
        print(f"{image_file} تبدیل شد.")
