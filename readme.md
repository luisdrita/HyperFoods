# MRes Biomedical Research
[warcraft12321.github.io/HyperFoods](https://warcraft12321.github.io/HyperFoods)

## HyperFoods

### Objectives

The aim of the project was to develop the algorithms and retrieve the ingredients, quantities and cooking processes from the Recipe1M+ dataset of recipes. Query API from FoodData Central to extract caloric information for each ingredient/recipe. To add flavour molecule information to each ingredient/recipe using FlavorDB. Label each recipe from Recipe1M+ dataset to a cuisine after training an SVM model in a dataset where this information was known. Calculate the number of anticancer molecules present in each recipe and present an ordered list including the ones with the higher value.  Cluster ingredients and recipes in terms of their similarity, considering how often 2 ingredients appear together in the dataset.
Finally, to build a web application that retrieves complete recipes from images, suggests new healthier ones based on the previous and that recommends new ingredients in substitution to the originals.

### Recipe Retrieval w/ Higher Number Anti-Cancer Molecules

Each recipe had all the ingredients concatenated in single string. It was used the ingredients vocabulary of the dataset
to filter what were and what weren't ingredient names in each string. Finally, it was calculated the sum of the number
of anti-cancer molecules present in each recipe using the table food_compound.csv. A DataFrame object was created so that
it not ony shows us the ID of each recipe, but also the number of anti-cancer molecules, along with an URL to the recipe's
location online.

### Benchmark Facebook Recipe Retrieval Algorithm

It was created a dictionary object (id_url.json) that matches recipes IDs (layer1.json) with the URLs of images available in layer2.json. While
some recipes do not contain images, others contain more than 1. This matching between different files was possible once layer2.json
also contain the recipe ID present in layer1.json.

Then, by manipulating Facebook's algorithm and its repository, the recipe retrieval algorithm is able to convert the JSON file id_url.json into
an array of strings of URLs. Along with this, it creates a parallel array of strings of the IDs of the recipes, so that in each position there is
correspondence between ID in this object with an image URL in the previous.

Finally, Facebook's algorithm was run and the ingredients list for each image URL was obtained. The number of correct elements over the total
number of elements in the ground-truth recipe gives us the accuracy of the algorithm. The ingredients present in each ground-truth recipe
were retrieved using the method above - "Recipe Retrieval w/ Higher Number Anti-Cancer Molecules".

### Data Visualization

- [Matplotlib](https://matplotlib.org/);
- [Plotly](https://chart-studio.plot.ly/feed/#/);
- [Seaborn](https://seaborn.pydata.org/).

### Unsupervised Learning

- [Louvain](https://github.com/taynaud/python-louvain);
- [Infomap](https://pypi.org/project/infomap/);
- [Density-Based Spatial Clustering of Applications with Noise](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html);
- [Mean Shift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html).

### Supervised Learning

- [Support Vector Machine](https://scikit-learn.org/stable/modules/svm.html)
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### Model Validation

- [Stratified K-Fold Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Leave One Out Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html)

### Benchmark

- [Intersection over Union / Jaccard Index](https://en.wikipedia.org/wiki/Jaccard_index);
- [F1 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html).

### Supervisors
[Kirill Veselkov](https://www.imperial.ac.uk/people/kirill.veselkov04) (Imperial College London) | [Michael Bronstein](https://www.imperial.ac.uk/people/m.bronstein) (Imperial College London)

Roadmap -> [Wiki](https://github.com/warcraft12321/HyperFoods/wiki)

[![DOI](https://zenodo.org/badge/217769774.svg)](https://zenodo.org/badge/latestdoi/217769774)
