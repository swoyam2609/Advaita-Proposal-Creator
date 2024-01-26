from PIL import Image, ImageDraw, ImageFont


def create_and_save_image(string1, string2, string3):
    width, height = 1800, 430
    background_color = 'white'
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_size = 100
    font = ImageFont.truetype("./Roboto-Medium.ttf", font_size)

    text_color = 'black'

    text1_position = (5, 5)
    text2_position = (5, 105)
    text3_position = (5, 205)

    draw.text(text1_position, string1, font=font, fill=text_color)
    draw.text(text2_position, string2, font=font, fill=text_color)
    draw.text(text3_position, string3, font=font, fill=text_color)
    image.save(f'./temp/{string3}.png')

create_and_save_image("Shri Manoj Kumar Pattnaik", "Chief Executive Officer", "Odisha Computer Application Center")
