from PIL import Image, ImageFont, ImageDraw
img = Image.open("image/1.jpg")

ft=ImageFont.truetype("arial.ttf",150)
text= "bonjour"
img_draw = ImageDraw.Draw(img)
img_draw.text((300,300),text,font=ft,fill=(255, 255, 255, 255))
img.show()
