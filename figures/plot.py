import matplotlib.pyplot as plt
import numpy
import seaborn


def main() -> None:
    seaborn.set_style('ticks', {'axes.grid': True})

    data = seaborn.load_dataset('penguins')

    handle = seaborn.pairplot(data, hue='species')
    handle.fig.set_size_inches(4, 4)
    handle.savefig('1-pairplot.pdf')
    handle.savefig('1-pairplot.svg')

    x = numpy.array(list('ABCDEF'))
    y = numpy.arange(10, 16)
   
    fig, ax = plt.subplots(1, 1)
    handle = seaborn.barplot(x=x, y=y, hue=x, ax=ax)
    handle.set(ylabel='Qualitative')
    fig.set_size_inches(4, 2)
    fig.savefig('2-barchart.pdf')
    fig.savefig('2-barchart.svg')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    data = seaborn.load_dataset('flights')
    data = data[data['month'].isin(months)]
    data.month = data.month.cat.remove_unused_categories()
    
    fig, ax = plt.subplots(1, 1)
    handle = seaborn.lineplot(
        data=data,
        x='year',
        y='passengers',
        hue='month',
        hue_order=months,
        style='month',
        dashes=True,
        markers=True,
        ax=ax,
    )
    fig.set_size_inches(4, 2)
    fig.savefig('3-linechart.pdf')
    fig.savefig('3-linechart.svg')


if __name__ == '__main__':
    main()

