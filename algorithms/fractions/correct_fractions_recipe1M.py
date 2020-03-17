

def corrector (recipes_data):

    # ---------------------------- Deleting Empty Instructions and Ingredients ----------------------------

    modified_recipes_data = recipes_data

    for key, recipe in enumerate(recipes_data):

        if key%50000 == 0:

            print("check")

        for key2, ingredient in enumerate(recipe["ingredients"]):

            if not ingredient["text"].translate({ord(ii): None for ii in (string.punctuation + "0123456789")}):

                modified_recipes_data[key]["ingredients"].remove(recipes_data[key]["ingredients"][key2])

            if "tea bag" in ingredient["text"]:

                modified_recipes_data[key]["ingredients"].replace("tea bag", "teabag")

        for key3, instruction in enumerate(recipe["instructions"]):

            if not instruction["text"].translate({ord(ii): None for ii in (string.punctuation + "0123456789")}):

                modified_recipes_data[key]["instructions"].remove(recipes_data[key]["instructions"][key3])

            if "tea bag" in instruction["text"]:

                modified_recipes_data[key]["instructions"].replace("tea bag", "teabag") 

    # ---------------------------- Deleting Empty Recipes ----------------------------

    modified_modified_recipes_data = modified_recipes_data

    for key, recipe in enumerate(modified_recipes_data):

        if key%50000 == 0:

            print("check")

        if recipe["ingredients"] or recipe["instructions"]:

            continue

        else:

            print("error")
            print(recipe)
            modified_modified_recipes_data.remove(modified_recipes_data[key])

    # ---------------------------- Manually Deleted Non-Eatable Recipe ----------------------------

    # {"ingredients": [{"text": "1 cup camomile tea"}, {"text": "water, as required"}], 
    # "url": "http://www.food.com/recipe/chamomile-hair-shine-for-blonde-hair-107822", 
    # "partition": "train", "title": "Chamomile Hair Shine for Blonde Hair", 
    # "id": "1082586cc6", "instructions": [{"text": "Prepare chamomile tea and keep it aside to cool."},
    # {"text": "Shampoo your hair as usual and lightly condition it."}, {"text": "Pour chamomile tea over it."}, 
    # {"text": "Work into hair from scalp to ends."}, {"text": "Quickly rinse under cool water."}, 
    # {"text": "Towel dry gently."}, {"text": "Three good tips for hair are:."}, {"text": "1."}, 
    # {"text": "Never use HOT water to wash your hair."}, {"text": "2."}, {"text": "Never be rough with your hair."}, 
    # {"text": "Be gentle when you dry it."}, {"text": "3."}, {"text": "Always use woodden/rubber wide tooth combs to
    # comb your hair."}]}

    # ---------------------------- Correcting Fractions in Food.com Recipes (Part 1) ----------------------------

    recipes_data_joint = {}

    for key, recipe in enumerate(modified_modified_recipes_data):

        if key%50000 == 0:

            print("check")

        recipes_data_joint[recipe["id"]] = []

        for ingredient_text in recipe["ingredients"]:

            recipes_data_joint[recipe["id"]].append(ingredient_text["text"])

    # ---------------------------- Correcting Fractions in Food.com Recipes (Part 2) ----------------------------

    stop_words = set(stopwords.words('english'))
    punctuationAndNumbers = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    intab = punctuationAndNumbers
    outtab = "_" * len(punctuationAndNumbers)
    trantab = str.maketrans(intab, outtab)

    lemmatizer = WordNetLemmatizer()

    def auxx (idd, ingredient):

        result_final = []

        for one_ingredient in ingredient:

            word_tokens = word_tokenize(one_ingredient)

            result_final.append([lemmatizer.lemmatize(w.translate(trantab).replace("_", "").lower()) for w in word_tokens if w not in stop_words])

        return result_final

    num_cores = multiprocessing.cpu_count()

    listy = Parallel(n_jobs=num_cores)(delayed(auxx)(idd, ingredient) for idd, ingredient in recipes_data_joint.items())

    # ---------------------------- Correcting Fractions in Food.com Recipes (Part 3) ----------------------------

    final_dict = {}

    i = 0

    for idd, ingredient in recipes_data_joint.items():

        final_dict[i] = listy[i]

        i = i + 1

    modified_final_dict = final_dict

    for i, ingredient in final_dict.items():

        for keyy, ingredient_tokenized_text in enumerate(ingredient):

            while("" in ingredient_tokenized_text) :

                modified_final_dict[i][keyy].remove("")

    # ---------------------------- Correcting Fractions in Food.com Recipes (Part 4) ----------------------------

    units_list_final_filtered = [line.rstrip('\n') for line in open('./vocabulary/units_list_final_filtered_lemmatized_correct_fractions.txt')]

    modified_modified_modified_recipes_data = modified_modified_recipes_data

    recipes_locations = []

    for key, recipe in enumerate(modified_modified_recipes_data):

        if ".food.com" in recipe["url"]:

            recipes_locations.append(key)

    location_and_number = []

    for i in recipes_locations:

        for keyyyy, ingredient in enumerate(modified_final_dict[i]): # Each recipe has all the ingredients' text merged.

            for unit in units_list_final_filtered:

                if unit in ingredient and len(ingredient[ingredient.index(unit) - 1]) == 2 and re.search(r"[1-5][2-9]", ingredient[ingredient.index(unit) - 1]):

                    if ingredient[ingredient.index(unit)] == "ounce":

                        continue

                    else:

                        location_and_number.append([i, keyyyy, ingredient[ingredient.index(unit) - 1], unit])

    dict_possible_wrong_recipes = {}

    for listt in location_and_number:

        dict_possible_wrong_recipes[listt[0]] = {}
        dict_possible_wrong_recipes[listt[0]]["positions"] = []
        dict_possible_wrong_recipes[listt[0]]["numbers"] = []

    for listt2 in location_and_number:

        dict_possible_wrong_recipes[listt2[0]]["positions"].append(listt2[1])
        dict_possible_wrong_recipes[listt2[0]]["numbers"].append(listt2[2])

    for recipe_number in list(dict_possible_wrong_recipes.keys()):

        for ingredient_number_position, ingredient_number in enumerate(dict_possible_wrong_recipes[recipe_number]["positions"]):

            replaced_number = dict_possible_wrong_recipes[recipe_number]["numbers"][ingredient_number_position]

            modified_modified_modified_recipes_data[recipe_number]["ingredients"][ingredient_number]["text"] = modified_modified_modified_recipes_data[recipe_number]["ingredients"][ingredient_number]["text"].replace(replaced_number, replaced_number[0] + "/" + replaced_number[1])

    # ---------------------------- Correcting Fractions in Food.com Recipes (Part 5) ----------------------------

    # Exporting Corrected Recipe Dataset

    with open('./data/recipe1M+/noEmptyIngredientsOrInstructions/noEmpty(IngredientOrInstruction)Recipes/fractionsCorrected/modified_modified_modified_recipes_data2.json', 'w') as json_file:

        json.dump(modified_modified_recipes_data, json_file)
        
    return modified_modified_recipes_data