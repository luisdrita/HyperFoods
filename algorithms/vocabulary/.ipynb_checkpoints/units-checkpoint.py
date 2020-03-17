import inflect # Importing module to obtain the plural of a string.

p = inflect.engine()

units_list_temp = set() # hey = [0, 4, 1, 4, 9] set(hey) -> {0, 1, 4, 9}

# get_units function retrieves the words that are next to every number or fraction in a given ingredient's text field.
def get_units(ingredient_text_input, number_input): 
    
    split_ingredient_list2 = ingredient_text_input.replace("/", " ").replace("-", " ").translate({ord(ii): None for ii in string.punctuation.replace(".", "")}).lower().split(" ")
    
    for number_input_it in number_input:
        
        for iji in range(len(split_ingredient_list2) - 1):
                                            
            if split_ingredient_list2[iji] == number_input_it and re.search(r"[0-9]", split_ingredient_list2[iji + 1]) is None and re.search(r".\b", split_ingredient_list2[iji + 1]) is None:
                            
                units_list_temp.add(split_ingredient_list2[iji + 1])
                break
                
# create_unit_vocab function receives recipes_data and ingredients_list and prints in a text document all potential units present in Recipe1M+ ordered alphabetically. 
def create_unit_vocab(recipes_data, ingredients_list):
    
    lemmatizer = WordNetLemmatizer()
    food = wordnet.synset('food.n.02') # Using python NLTK wordnet to retrive an additional list of foods. 

    for original_recipes_data_it in recipes_data: # Iterating over Recipe1M+ dataset.

        for ingredient_it in original_recipes_data_it["ingredients"]: # Iterating over Recipe1M+ dataset.

            number_array = re.findall(r"\d", ingredient_it["text"]) # Returning all digit matches present in each ingredient text field.

            if number_array: # In case digits were identified, get_units function is executed and potential units retrieved.

                get_units(ingredient_it["text"], number_array) # Executing function that retrieves units next to the digits detected in the ingredients text.

    units_list = list(units_list_temp) # Converting set to list to be able to sort it alphabetically.
    units_list.sort() # Ordering units list.

    lineList = units_list

    final_units = []

    for unit in lineList:

        for index, ingredients_list_it in enumerate(ingredients_list):

            if unit == ingredients_list_it or unit == p.plural(ingredients_list_it): # Excluding potential units which name is present in the ingredients' vocabulary, whether in the singular or plural form.

                break

            elif index == len(ingredients_list) - 1: # In case the unit is not present, then it is added to a new list containing a filtered list of units.

                final_units.append(unit)

    lines = final_units

    filtered_stopwords = [word for word in lines if word not in stopwords.words('english')] # Stopwords removed from units list.
    filtered_verbs_adjectives_adverbs = []

    for w in filtered_stopwords: # Verbs, adjectives, adverbs and colors removed from units list.
        if wordnet.synsets(w) and wordnet.synsets(w)[0].pos() != "v" and wordnet.synsets(w)[0].pos() != "a" and wordnet.synsets(w)[0].pos() != "r" and w not in webcolors.CSS3_NAMES_TO_HEX and w not in list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()])):
            filtered_verbs_adjectives_adverbs.append(w)
        elif wordnet.synsets(w) == []:
            filtered_verbs_adjectives_adverbs.append(w)

    units = [lemmatizer.lemmatize(unit) for unit in filtered_verbs_adjectives_adverbs]
    units_modified = sorted(list(set(units)))

    # Save final list of units into a txt file. Misclassified units were manually removed after.
    with open('./vocabulary/units_list_final_filtered_lemmatized.txt', 'w') as f:
        
        for key, item in enumerate(units_modified):
            
            if item != "" and item != "<end>" and item != "<pad>" and key < len(units_modified) - 1:
                f.write("%s\n" % item)

            elif item != "":
                f.write("%s" % item)
                
    return units_modified