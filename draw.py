import time
import random

from PIL import Image, ImageFont, ImageColor, ImageDraw


def main():
    image_mode = "RGB"
    image_size = (640, 480)
    image_color = "#0000ff"
    font_size = 48
    font_color = "#00ffff"

    # Create a new virtual picture:
    # - given color palette (mode)
    # - given size (size)
    # - and given color (color)
    img = Image.new(mode=image_mode, size=image_size, color=image_color)

    # Download font and color for labeling
    font = ImageFont.truetype("MULLERBOLD.ttf", size=font_size)
    fill = ImageColor.getrgb(color=font_color)

    # Create an entry point to "drawing"
    # Any changes to the virtual picture are stored and managed here
    draw = ImageDraw.Draw(im=img, mode=img.mode)

    # Drawing is relative to the top left corner
    # Therefore, you need to calculate the size of the text block, taking into account the font size
    text = ["Success!", "Very long string", "Price: 5555 $"]
    sorted_text = sorted(text, key=lambda i: len(i), reverse=True)
    longest_line = sorted_text[0]
    print("We calculate the width of the block based on `{}`".format(longest_line))

    text_width, text_height = font.getsize(longest_line)
    text_height *= len(text)
    real_text = "\n".join(text)

    # Apply text so that it is exactly in the center of the image
    x = 1.0 * image_size[0] / 2 - 1.0 * text_width / 2
    y = 1.0 * image_size[1] / 2 - 1.0 * text_height / 2
    draw.text(xy=(x, y), text=real_text, fill=fill, font=font, align="center")

    # Save the resulting image to a file on your computer
    # (However, to send a picture over the network, it is not necessary to save to a file)
    filename = "result_{}_{}.png".format(
        int(time.time()), random.randint(1, 100))
    print("Save to file `{}`".format(filename))
    img.save(filename)


if __name__ == '__main__':
    main()
