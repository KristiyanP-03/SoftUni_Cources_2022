import qrcode

img = qrcode.make('https://fantaziitenaanabel.blogspot.com/')
img.save("D:/some_file.jpg")
print('done')
