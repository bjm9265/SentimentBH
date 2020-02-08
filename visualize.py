import matplotlib.pyplot as plt


def pie_chart(pos_per, neg_per, title):

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Positive', 'Negative'
    sizes = [pos_per, neg_per]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.savefig("newfig.png")
    return fig
