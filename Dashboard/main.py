import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import Normalize

cmap = plt.colormaps["plasma"]
plt.rcParams['savefig.facecolor'] = "0.8"


def example_plot(ax, fontsize=12):
    x = [10, 12, 14, 16, 18, 20]
    y = [63, 55, 59, 70, 65, 75]

    ax.plot(x, y)

    ax.locator_params(nbins=3)
    ax.set_xlabel('Даты с 10 по 20 число', fontsize=fontsize)
    ax.set_ylabel('Температура С', fontsize=fontsize)
    ax.set_title('Температура в камере сушки', fontsize=fontsize)


def add_bar(ax):

    data = list(range(18, 36))

    data = [325, 300 , 400 , 350, 450]

    names = list(map(lambda x: str(x), list(range(10, 41, 10)))) # список строк

    names = ['10', '12', '14', '16', '18']

    print(names)
    # fig, ax = plt.subplots(figsize=(16, 10), facecolor='white', dpi=80)
    max_value_y = 475

    min_value_y = 250

    # ax.vlines(x=range(len(data)), ymin=min_value_y, ymax=max_value_y, color='firebrick', alpha=0.7, linewidth=20)

    # Annotate Text
    for i, cty in enumerate(data):
        ax.text(i, cty + 0.5, round(cty, 1), horizontalalignment='center')

    # Title, Label, Ticks and Ylim
    ax.set_title('Давление в гидравлической системе', fontdict={'size': 18})
    ax.set(ylabel='Давление bar', ylim=(min_value_y, max_value_y))
    ax.bar(names, data, color='royalblue',
            width=0.4)
    # plt.xticks(range(len(data)), names, horizontalalignment='right', fontsize=12, )

def main():
    plt.close('all')
    fig = plt.figure()

    ax1 = plt.subplot2grid((3, 3), (0, 0))
    ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
    ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)

    # ax5 = plt.subplot2grid((3, 3), (2, 1))

    example_plot(ax1)
    # example_plot(ax5)
    # example_plot(ax2)
    add_bar(ax3)


    fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(50, 75), cmap=cmap),
                 ax=ax1)

    ### начало блока анимации
    t = np.linspace(0, 3, 40)
    print(f"{t}")
    g = -9.81
    v0 = 12
    z = g * t ** 2 / 2 + v0 * t

    v02 = 5
    z2 = g * t ** 2 / 2 + v02 * t

    scat = ax2.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
    line2 = ax2.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
    ax2.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
    ax2.legend()

    def update(frame):
        # for each frame, update the data stored on each artist.
        x = t[:frame]
        y = z[:frame]
        # update the scatter plot:
        data = np.stack([x, y]).T
        scat.set_offsets(data)
        # update the line plot:
        line2.set_xdata(t[:frame])
        line2.set_ydata(z2[:frame])
        return (scat, line2)

    ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
    ### конец блока анимации

    plt.tight_layout()
    plt.show()


def plot_temprature():
    plt.close('all')
    x = [24, 25, 26, 27, 28, 29] # список из дат в формате строки
    y = [23, 22, 25, 27, 29, 30]
    x_lab = list(map(lambda x_: str(x_), x))
    plt.plot(x, y)
    plt.scatter(x, y, color='green')
    plt.xticks(ticks=x, labels=x_lab)
    plt.xlabel('something_x')
    plt.ylabel('something_y')
    plt.show()


def some_prediction():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import RadioButtons

    t = np.linspace(0, 3, 40)
    print(f"{t}")
    g0 = -9.81
    g1 = -9.81 * 0.95
    g2 = -9.81 * 0.86
    v0 = 12


    s0 = g0 * t ** 2 / 0.5 + v0 * t
    s1 = g1 * t ** 2 / 1 + v0 * t
    s2 = g2 * t ** 2 / 2 + v0 * t

    #
    # t = np.arange(0.0, 2.0, 0.01)
    # s0 = np.sin(2 * np.pi * t)
    # s1 = np.sin(4 * np.pi * t)
    # s2 = np.sin(8 * np.pi * t)

    fig, ax = plt.subplots()
    l, = ax.plot(t, s0, lw=2, color='red')

    ax.set(xlim=[0, 5], ylim=[0, 10], xlabel='Через сколько произойдет сбой', ylabel='Время работы ч')

    fig.subplots_adjust(left=0.3)

    axcolor = 'lightgoldenrodyellow'
    rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
    radio = RadioButtons(rax, ('Ве'
                               'ро', '2 Hz', '4 Hz'),
                         label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
                         radio_props={'s': [16, 32, 64]})

    def hzfunc(label):
        hzdict = {'Веро': s0, '2 Hz': s1, '4 Hz': s2}
        ydata = hzdict[label]
        l.set_ydata(ydata)
        fig.canvas.draw()

    radio.on_clicked(hzfunc)

    rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
    radio2 = RadioButtons(
        rax, ('red', 'blue', 'green'),
        label_props={'color': ['red', 'blue', 'green']},
        radio_props={
            'facecolor': ['red', 'blue', 'green'],
            'edgecolor': ['darkred', 'darkblue', 'darkgreen'],
        })

    def colorfunc(label):
        l.set_color(label)
        fig.canvas.draw()

    radio2.on_clicked(colorfunc)

    #rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
    #radio3 = RadioButtons(rax, ('-', '--', '-.', ':'))

    def stylefunc(label):
        l.set_linestyle(label)
        fig.canvas.draw()

    #radio3.on_clicked(stylefunc)

    plt.show()


if __name__ == '__main__':
    # circular_diagram()
    # plot_temprature()
    main()
    some_prediction()
    # example_plot()
    # add_bar()