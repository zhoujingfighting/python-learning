#!/usr/bin/python
"""
1:抓取网页数据
2:resize image,调整图片尺寸
"""
from PIL import Image
# 这里可以是绝对路径也可以是相对路径
image = Image.open("test.png")

# 打印图片的大小
print(f"Current size: {image.size}")

resized_image = image.resize((500,500))
resized_image.save("test1.png")