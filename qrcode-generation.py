"""
不能给文件起一个与现有模块相同的名字
"""

import qrcode
def generateQR(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="white")
    img.save("test.png")

generateQR("https://github.com/zhoujingfighting")

    
