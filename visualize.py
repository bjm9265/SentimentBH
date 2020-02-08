import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def pie_chart(pos_per, neg_per, neu_per, title, labels):

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Positive', 'Negative', 'Neutral'
    sizes = [pos_per, neg_per, neu_per]
    explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.style.use("classic")
    fig, ax = plt.subplots()
    # ax.set_facecolor("gray")
    ax.pie(sizes, explode=explode, colors=("forestgreen", "tomato", "slategray"), labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.savefig("newfig.png")
    return fig


def image_gen(val):

    percent = val + "%"

    main = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 130)
    message = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 90)
    img = Image.new('RGB', (600, 400), color=(255, 255, 255))
    img.save('test.png')
    d = ImageDraw.Draw(img)
    d.text((200, 150), percent, font=main, fill=(62, 201, 83))
    d.text((60, 300), percent, font=message, fill=(46, 51, 47))
    img.save('test.png')
