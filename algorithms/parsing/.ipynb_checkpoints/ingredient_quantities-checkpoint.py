# Retrieving units and quantities of each ingredient present in a given recipe.

import inflect
import re


def ingredient_quantities(recipe, new_ingredients_list, units_list_dict):

    # -------------------------------- Preprocessing Recipe Dataset

    id_ingredients = {}
    id_ingredients[recipe["id"]] = []
    
    j = 0

    for ingredient_text in recipe["ingredients"]:

        id_ingredients[recipe["id"]].append({"id": j, "ingredient": (ingredient_text["text"]).lower()})
        
        j = j + 1

    # -------------------------------- Extracting Ingredients

    '''
    ingredients_count = {}

    if ingredient_counting:

        for ingredient_vocab in new_ingredients_list:

            ingredients_count[ingredient_vocab] = 0
    '''
    
    # Dictionary with the ingredients (from the vocabulary of ingredients) and the number of occurrences in recipes.

    new_id_ingredients_tokenized_position = {}

    p = inflect.engine()

    new_id_ingredients_tokenized_position[recipe["id"]] = []
    
    k = 0

    for ingredient_text in id_ingredients[recipe["id"]]:

        for ingredient_vocab in new_ingredients_list:

            if (re.search(r"\b" + re.escape(ingredient_vocab) + r"\b", ingredient_text["ingredient"]) or re.search(r"\b" + p.plural(re.escape(ingredient_vocab)) + r"\b", ingredient_text["ingredient"])) is not None:

                new_id_ingredients_tokenized_position[recipe["id"]].append({"id": k, "ingredient": ingredient_vocab})
        k = k + 1
    '''
                if ingredient_counting:
                    ingredients_count[new_ingredients_list[j]] = ingredients_count[new_ingredients_list[j]] + 1
                    print(ingredients_count)
    '''
    # -------------------------------- Extracting Units and Quantities
    '''
    ingrs_quants_units = {}

    value = new_id_ingredients_tokenized_position[recipe["id"]]

    ingrs_quants_units[recipe["id"]] = []

    for value2 in value:

        for i in list(units_list_dict.keys()):

            if (re.search(r"\b" + re.escape(i) + r"\b", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"])) is not None:

                if re.search(r"[1-9][0-9][0-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": float(re.search(r"[1-9][0-9][0-9]", ((id_ingredients[recipe["id"]][value2["id"]])["ingredient"])).group()),"unit": i, "quantity (g)": float(re.search(r"[1-9][0-9][0-9]",((id_ingredients[recipe["id"]][value2["id"]])["ingredient"])).group()) * int(units_list_dict[i])})

                    break

                elif re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": int(((re.search(r"[1-9]/[1-9]",(id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[1]), "unit": i, "quantity (g)": (int(((re.search(r"[1-9]/[1-9]",(id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[1])) * int(units_list_dict[i])})

                    break

                elif re.search(r"[1-9][0-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": float(re.search(r"[0-9][0-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()), "unit": i, "quantity (g)": float(re.search(r"[0-9][0-9]",(id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()) * int(units_list_dict[i])})

                    break

                else:

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": float(units_list_dict[i]), "unit": i, "quantity (g)": int(units_list_dict[i])})

                    break

            elif i == len(list(units_list_dict.keys())) - 1:

                if re.search(r"[1-9][0-9][0-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": 200, "unit": value2["ingredient"], "quantity (g)": 200})

                elif re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[1]), "unit": value2["ingredient"],"quantity (g)": int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[0]) / int(((re.search(r"[1-9]/[1-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]).group()).split("/"))[1]) * 200})

                elif re.search(r"[1-9][0-9]", (id_ingredients[recipe["id"]][value2["id"]])["ingredient"]):

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": 200, "unit": value2["ingredient"], "quantity (g)": 200})

                else:

                    ingrs_quants_units[recipe["id"]].append({"ingredient": value2["ingredient"], "quantity": 200, "unit": value2["ingredient"], "quantity (g)": 200})
    '''
    #return ingrs_quants_units[recipe["id"]]
    
    return new_id_ingredients_tokenized_position

