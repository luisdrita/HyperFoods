# Recipe Parser

## Description
Python module that retrieves ingredients, quantities and respective units after input one line of the recipe.

## Usage
Install package using PyPI.

```console
pip install recipe_parser
```
Importing module.

```python
from ingredient_quantities import ingredient_quantities
```
Executing function that retrieves ingredients, quantities and units.

```python
output = ingredient_quantities(ingredient_sentence, ingredients_vocab, units_vocab)
```

`ingredient_sentence` is a string which corresponds to a line of a recipe containing, ideally, 1 ingredient, 1/2 numbers for the quantity and 1 unit. Although, the algorithm is able to handle slight variations of this one.

`ingredients_vocab` is the vocabulary of ingredients (list format) present in the recipe dataset. They should be lemmatized and stopwords not present. 

`units_vocab` is the vocabulary of units (list format) present in the recipe dataset. Algorithm does not support units with more than 1 word.

`output` is a list of dictionaries with the following format: {"ingredient": ingredient, "quantity": quantity, "unit": unit}. Same lenght as the number of ingredients detected in the string using the suitable vocabulary.

Algorithm optimized to be used in [Recipe1M+ dataset](http://pic2recipe.csail.mit.edu/). Optimized vocabularies bellow:

[ingredients_vocab.txt](https://github.com/warcraft12321/HyperFoods/tree/master/vocabulary/ingr_vocab_optimized.txt) | [units_vocab.txt](https://github.com/warcraft12321/HyperFoods/tree/master/vocabulary/units_list_final_filtered_lemmatized.txt)

Additionally, it was also created a conversion table that converts kitchen metric units (teaspoon, tablespoon...), and its semantic variants, to grams. Always taking into account a standardized volume -> mass conversion of the water as reference:

[units_list_final_filtered_lemmatized.csv](https://github.com/warcraft12321/HyperFoods/tree/master/vocabulary/units_list_final_filtered_lemmatized.csv)

## More

### HyperFoods Project

The aim of the project was to develop the algorithms and retrieve the ingredients, quantities and units from the Recipe1M+ dataset of recipes. Query API from FoodData Central to extract nutritional information for each ingredient/recipe. Label each recipe from Recipe1M+ dataset to a cuisine after training an SVM model in a dataset where this information was known. Calculate the number of anticancer molecules present in each recipe and present an ordered list including the ones with the higher value. Cluster ingredients and recipes in terms of their similarity, considering how often 2 ingredients appear together in the dataset.

### Supervision Team

[Kirill Veselkov](https://www.imperial.ac.uk/people/kirill.veselkov04) (Imperial College London) | [Michael Bronstein](https://www.imperial.ac.uk/people/m.bronstein) (Imperial College London)

Roadmap -> [Wiki](https://github.com/warcraft12321/HyperFoods/wiki)

[![DOI](https://zenodo.org/badge/217769774.svg)](https://zenodo.org/badge/latestdoi/217769774)


