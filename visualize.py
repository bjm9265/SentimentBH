import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import os

green = (62, 201, 83)
red = (194, 52, 33)


# pos_per : int - Positive Percentage
# neg_per : int - Negative Percentage
# neu_per : int - Neutral Percentage
# title : str - title of the piechart
# labels : tuple of str - IN THE ORDER OF positive, negative, neutral
def piechart_gen(pos_per, neg_per, neu_per, title, labels):

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Positive', 'Negative', 'Neutral'
    sizes = [pos_per, neg_per, neu_per]
    explode = (0, 0, 0)  # Set one of there to .1 to make it "pop" out of the

    plt.style.use("sixfourtynine")
    fig, ax = plt.subplots()
    ax.edgecolor= "orange"
    ax.pie(sizes, explode=explode, colors=("forestgreen", "tomato", "slategray"),  autopct='%1.1f%%',
           shadow=True, startangle=-180)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.savefig("out\pie_chart.png")
    return fig


# raw_percent : int - Not a string, needs to have % sign appended
# blurb : string - The message to accompany the percentage shown
def snapshot_gen(raw_percent, blurb):

    percent = str(raw_percent) + "%"
    blurb = "of people say pizza is their favorite food"  # 42 character message

    bcolor = (36, 45, 48)  # Color of the background (gray-ish)
    percolor = red  # The color of the percentage (configurable)
    blurbcolor = (255, 255, 255)  # Color of the blurb (white)

    # Only create snapshots on Windows machines, as the path for Macs is different (and they don't have Calibri)
    if os.name == 'nt':
        # Load the fonts and set the size
        main = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 130)
        blurbfont = ImageFont.truetype('C:\Windows\Fonts\Calibri.ttf', 32)
        # Creates a new color image, sets the resolution, draws background
        img = Image.new('RGB', (600, 300), color=bcolor)
        # Draws the text specifying the percentage, then the blurb
        d = ImageDraw.Draw(img)
        d.text((200, 50), percent, font=main, fill=percolor)
        d.text((40, 200), blurb, font=blurbfont, fill=blurbcolor)
        img.save('out\snapshot.png')
