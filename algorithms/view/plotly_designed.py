import plotly.graph_objs as go
from plotly.subplots import make_subplots


def plotly_function(x_ingredients_embedded1, x_ingredients_embedded2, words, colors, sizes, labels, title):
    fig_plotly = make_subplots(rows=1, cols=2, subplot_titles=("PCA", "T-SNE"))

    if labels == "true":

        fig_plotly.add_trace(
            go.Scatter(
                x=x_ingredients_embedded1[:, 0],
                y=x_ingredients_embedded1[:, 1],
                mode="markers+text",
                text=words,
                textposition="bottom center",
                textfont=dict(
                    family="sans serif",
                    size=10,
                    color="black"
                ),
                marker=dict(
                    size=sizes,
                    sizemode='area',
                    sizeref=2.*max(sizes)/(40.**2),
                    sizemin=4,
                    color=colors,  # set color equal to a variable
                ),  # ,
                # alpha=0.5
                hoverinfo = "text"
            ),
            row=1, col=1
        )

        fig_plotly.add_trace(
            go.Scatter(
                x=x_ingredients_embedded2[:, 0],
                y=x_ingredients_embedded2[:, 1],
                mode="markers+text",
                text=words,
                textposition="bottom center",
                textfont=dict(
                    family="sans serif",
                    size=10,
                    color="black"
                ),
                marker=dict(
                    size=sizes,
                    sizemode='area',
                    sizeref=2.*max(sizes)/(40.**2),
                    sizemin=4,
                    color=colors,  # set color equal to a variable
                ),  # ,
                # alpha=0.5
                hoverinfo = "text"
            ),
            row=1, col=2
        )

    else:

        fig_plotly.add_trace(
            go.Scatter(
                x=x_ingredients_embedded1[:, 0],
                y=x_ingredients_embedded1[:, 1],
                mode="markers",
                text=words,
                marker=dict(
                    size=sizes,
                    sizemode='area',
                    sizeref=2.*max(sizes)/(40.**2),
                    sizemin=4,
                    color=colors,  # set color equal to a variable
                ),
                hoverinfo = "text"
            ),
            row=1, col=1
        )

        fig_plotly.add_trace(
            go.Scatter(
                x=x_ingredients_embedded2[:, 0],
                y=x_ingredients_embedded2[:, 1],
                mode="markers",
                text=words,
                marker=dict(
                    size=sizes,
                    sizemode='area',
                    sizeref=2.*max(sizes)/(40.**2),
                    sizemin=4,
                    color=colors,  # set color equal to a variable
                ),
                hoverinfo = "text"
            ),
            row=1, col=2
        )

    fig_plotly.update_layout(
        height=500,
        width=1000,
        title={
            "text": title,
        },
        showlegend=False)
    fig_plotly.show()

    # Explicit trust -> jupyter trust /path/to/notebook.ipynb (at the command-line)
