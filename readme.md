# Machine Learning for Building a Food Recommendation System
[Jupyter Notebook](https://warcraft12321.github.io/HyperFoods) | [Report](https://github.com/warcraft12321/HyperFoods/blob/master/thesis/report.pdf) | [Poster](https://github.com/warcraft12321/HyperFoods/blob/master/thesis/poster.pdf)

### Introduction

Many factors influence individual’s health, such as physical exercise, sleep, nutrition, heredity and pollution. Being
nutrition one of the biggest modifiable factors in our lives, small changes can have a big impact. With the exponential
increase in the number of available food options, it is not possible to take them all into account anymore. The only way
to consider user taste preferences, maximize the number of healthy compounds and minimize the unhealthy ones in food,
is using (3D) recommendation systems.

### Objectives

The goal of this project was to use the largest publicly available collection of recipe data (Recipe1M+) to build a
recommendation system for ingredients and recipes. Train, evaluate and test a model able to predict cuisines from sets
of ingredients. Estimate the probability of negative recipe-drug interactions based on the predicted cuisine. Finally,
to build a web application as a step forward in building a 3D recommendation system.

### Results

A vectorial representation for every ingredient and recipe was generated using Word2Vec. An SVC model was trained to
return recipes’ cuisines from their set of ingredients. South Asian, East Asian and North American cuisines were
predicted with more than 73% accuracy. African, Southern European and Middle East cuisines contain the highest number
of cancer-beating molecules. Finally, it was developed a web application able to predict the ingredients from an image,
suggest new combinations and retrieve the cuisine the recipe belongs, along with a score for the expected number of
negative interactions with antineoplastic drugs (github.com/warcraft12321/HyperFoods).

<img id = "img" src="./website/img/site.png" alt="HyperFoods">

Figure 1 - Web App (run locally, web app exceeds Heroku memory limits): [https://hyperfoods.herokuapp.com/](https://hyperfoods.herokuapp.com/).

### Supervisors
[Kirill Veselkov](https://www.imperial.ac.uk/people/kirill.veselkov04) (Imperial College London) | [Michael Bronstein](https://www.imperial.ac.uk/people/m.bronstein) (Imperial College London)

Roadmap -> [Wiki](https://github.com/warcraft12321/HyperFoods/wiki)

[![DOI](https://zenodo.org/badge/245535944.svg)](https://zenodo.org/badge/latestdoi/245535944)