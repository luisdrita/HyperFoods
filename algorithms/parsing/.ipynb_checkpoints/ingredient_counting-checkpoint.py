import inflect
import re


def ingredient_quantities(recipes_data, id_ingredients, ingredients_list):

    new_ingredients_list = []  # List of ingredients from the vocabulary with spaces instead of underscores.

    for i in range(0, len(ingredients_list)):

        if "_" in ingredients_list[i]:
            new_ingredients_list.append(ingredients_list[i].replace("_", " "))
            continue

        new_ingredients_list.append(ingredients_list[i])  # In case there is no _

    ingredients_count = {} # Dictionary with the ingredients (from the vocabulary of ingredients) and the number of occurrences in recipes.

    for j in range(0, len(new_ingredients_list)):
        ingredients_count[new_ingredients_list[j]] = 0

    p = inflect.engine()

    for i in range(0, len(id_ingredients)):

        for j in range(0, len(new_ingredients_list)):

            for k in range(0, len(id_ingredients[recipes_data[i]["id"]])):

                if (re.search(r"\b" + re.escape(new_ingredients_list[j]) + r"\b",
                              (id_ingredients[recipes_data[i]["id"]][k])["ingredient"]) or re.search(
                        r"\b" + p.plural(re.escape(new_ingredients_list[j])) + r"\b",
                        (id_ingredients[recipes_data[i]["id"]][k])["ingredient"])) is not None:
                    ingredients_count[new_ingredients_list[j]] = ingredients_count[new_ingredients_list[j]] + 1