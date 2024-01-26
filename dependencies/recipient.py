from PIL import Image, ImageDraw, ImageFont


def createImage(string1, string2, string3, string4):
    width, height = 1800, 550
    background_color = 'white'
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_size = 105
    font = ImageFont.truetype("./dependencies/font.ttf", font_size)

    text_color = 'black'

    text1_position = (5, 5)
    text2_position = (5, 115)
    text3_position = (5, 225)
    text4_position = (5, 335)

    draw.text(text1_position, string1+',', font=font, fill=text_color)
    draw.text(text2_position, string2+',', font=font, fill=text_color)
    draw.text(text3_position, string3+',', font=font, fill=text_color)
    draw.text(text4_position, string4, font=font, fill=text_color)
    image.save(f'./temp/{string3}.png')

