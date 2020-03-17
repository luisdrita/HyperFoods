import seaborn as sns
from matplotlib import pyplot
import pandas as pd

# To use Seaborn,  data has to be in a Pandas DataFrame and it must take the form of what Hadley Whickam
# calls “tidy” data. It means the dataframe should be structured such that each column is a variable and
# each row is an observation.


def seaborn_function(x_ingredients_embedded1, x_ingredients_embedded2, words, colors, sizes):
    # Load the example mpg dataset
    data1 = pd.DataFrame({'x1': x_ingredients_embedded1[:, 0], 'y1': x_ingredients_embedded1[:, 1], 'group': words})
    data2 = pd.DataFrame({'x2': x_ingredients_embedded2[:, 0], 'y2': x_ingredients_embedded2[:, 1], 'group': words})

    pyplot.figure(figsize=(24, 12), dpi=500)

    pyplot.subplot(121)
    ax1 = sns.scatterplot(x="x1", y="y1", data=data1, size=sizes, alpha=0.5, hue=colors,
                          hue_norm=(0, 7))

    ax1.set_title("PCA")

    pyplot.subplot(122)
    ax2 = sns.scatterplot(x="x2", y="y2", data=data2, size=sizes, alpha=0.5, hue=colors,
                          hue_norm=(0, 7))
    ax2.set_title("T-SNE")

    # add annotations one by one with a loop
    for line in range(0, data1.shape[0]):
        ax1.text(data1.x1[line], data1.y1[line], data1.group[line], horizontalalignment='left', size=10, color='black',
                 weight='light')

        ax2.text(data2.x2[line], data2.y2[line], data2.group[line], horizontalalignment='left', size=10, color='black',
                 weight='light')

    # pyplot.title('add title here')


'''
def seaborn_function(x_ingredients_embedded1, x_ingredients_embedded2, words, colors, sizes):

    dim1 = []
    dim2 = []

    for i in range(0, len(x_ingredients_embedded1[:, 0])):
        dim1.append('PCA')
        dim2.append('T-SNE')

    # Load the example mpg dataset
    data1 = pd.DataFrame({'x1': x_ingredients_embedded1[:, 0], 'y1': x_ingredients_embedded1[:, 1], 'group': words, 'dimension': dim1})
    data2 = pd.DataFrame({'x1': x_ingredients_embedded2[:, 0], 'y1': x_ingredients_embedded2[:, 1], 'group': words, 'dimension': dim2})

    data = pd.DataFrame(
        {'x1': x_ingredients_embedded1[:, 0], 'x2': x_ingredients_embedded2[:, 0], 'y1': x_ingredients_embedded1[:, 1], 'y2': x_ingredients_embedded2[:, 1], 'group': words})

    # -----------------------

    sns.set(style="ticks")

    tips = pd.concat([data1, data2], ignore_index=True)

    print(tips)

    g = sns.FacetGrid(tips, col="dimension", height=10, aspect=1)
    g.map(pyplot.scatter, "x1", "y1", alpha=.7)
    g.add_legend()

    g = sns.PairGrid(data, y_vars=["y1", "y2"], x_vars=["x1", "x1"], height=4)

'''
