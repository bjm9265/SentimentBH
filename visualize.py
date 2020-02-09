import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

green = (62, 201, 83)
red = (194, 52, 33)


def pie_chart(pos_per, neg_per, neu_per, title, labels):

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Positive', 'Negative', 'Neutral'
    sizes = [pos_per, neg_per, neu_per]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.style.use("sixfourtynine")
    fig, ax = plt.subplots()
    ax.edgecolor= "orange"
    ax.pie(sizes, explode=explode, colors=("forestgreen", "tomato", "slategray"),  autopct='%1.1f%%',
           shadow=True, startangle=-180)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.savefig("newfig.png")
    return fig


def image_gen(val):

    percent = str(val) + "%"
    msg = "of people say pizza is their favorite food"  # 42 character message

    backcolor = (36, 45, 48)
    maincolor = red
    msgcolor = (255, 255, 255)

    if os.name == 'nt':
        main = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 130)
        message = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 32)

        img = Image.new('RGB', (600, 300), color=backcolor)
        d = ImageDraw.Draw(img)
        d.text((200, 50), percent, font=main, fill=maincolor)
        d.text((40, 200), msg, font=message, fill=msgcolor)
        img.save('test.png')
