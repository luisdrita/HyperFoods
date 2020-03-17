def get_nutritional_content(new_ingredients_list):

    # ---------------------------- Get 10 FoodData Central IDs for Each Ingredient from Vocab ----------------------------
    
    # For each ingredient present in the vocabulary (new_ingredients_list), it was retrieved the top 10 most similar results present in FoodData Central database. For the first element, the database was queried with the name of the ingredient plus the keyword "raw". In case there was present with such a description, this will contitute the first from the list of 10 and the other 9 will be a result of searching simply by the name of the ingredient. If there is no raw version available, then the top 10 searches of the ingredient name are returned.

    # Checking for the presence of ingredient_fdcIds.json file
    if os.path.exists('./vocabulary/ingredient_fdcIds.json'):

        f = open('./vocabulary/ingredient_fdcIds.json')
        ingredient_fdcIds = (json.load(f))
        f.close()

    else: 

        ingredient_fdcIds = {}

        for value in new_ingredients_list:

            ingredient_fdcIds[value] = {}
            ingredient_fdcIds[value]["fdcIds"] = []
            ingredient_fdcIds[value]["descriptions"] = []
            
            # Setting parameters for connecting to the database
            API_Key = "BslmyYzNnRTysPWT3DDQfNv5lrmfgbmYby3SVsHw"
            URL = "https://api.nal.usda.gov/fdc/v1/search?api_key=" + API_Key
            PARAMS2 = {'generalSearchInput': value + " raw"}
            
            # Database connection
            r2 = requests.get(url = URL, params = PARAMS2)
            
            # Extracting data in json format 
            data2 = r2.json()

            raw = False

            # Adding raw keyword to vocabulary
            if "foods" in data2 and value + " raw" in (data2["foods"][0]["description"]).lower().replace(",", ""):

                raw_id = data2["foods"][0]["fdcId"]
                raw_description = data2["foods"][0]["description"]

                ingredient_fdcIds[value]["fdcIds"].append(raw_id)
                ingredient_fdcIds[value]["descriptions"].append(raw_description)

                raw = True

            # Defining a params dict for the parameters to be sent to the API 
            PARAMS = {'generalSearchInput': value} 

            # Sending get request and saving the response as response object 
            r = requests.get(url = URL, params = PARAMS)

            # Extracting data in json format 
            data = r.json() 

            # Checking whether raw ingredient is present 
            if "foods" in data:

                numberMatches = len(data["foods"])

                if numberMatches > 10 and raw == True:
                    
                    numberMatches = 9
                    
                elif numberMatches > 10 and raw == False:
                    
                    numberMatches = 10

                for i in range(numberMatches):

                    ingredient_fdcIds[value]["fdcIds"].append(data["foods"][i]["fdcId"])
                    ingredient_fdcIds[value]["descriptions"].append(data["foods"][i]["description"])

    # ---------------------------- Get All Vocab Nutritional Info for 1st FDCID ----------------------------
    
    # Retrieving nutritional information for each ingredient present in the vocabulary (new_ingredients_list). First "fdcId" from each dictionary (ingredient_fdcIds) entry was used.

    # Checking for the presence of ingredient_nutritionalInfo.json file
    if os.path.exists('./vocabulary/ingredient_nutritionalInfo.json'):

        f = open('./vocabulary/ingredient_nutritionalInfo.json')
        ingredient_nutritionalInfo = json.load(f)
        f.close()

    else:

        ingredient_nutritionalInfo = {}

        # Getting nutritional information for the first "fdcId" from the list of 10
        for key, value in ingredient_fdcIds.items():

            if value["fdcIds"]:

                URL = "https://api.nal.usda.gov/fdc/v1/" + str(value["fdcIds"][0]) + "?api_key=" + API_Key

                # Sending get request and saving the response as response object 
                r = requests.get(url = URL)

                ingredient_nutritionalInfo[key] = {}
                ingredient_nutritionalInfo[key]["fdcId"] = value["fdcIds"][0]
                ingredient_nutritionalInfo[key]["description"] = value["descriptions"][0]
                ingredient_nutritionalInfo[key]["nutrients"] = {}

                for foodNutrient in r.json()["foodNutrients"]:

                    if "amount" in foodNutrient.keys():

                        ingredient_nutritionalInfo[key]["nutrients"][foodNutrient["nutrient"]["name"]] = [foodNutrient["amount"], foodNutrient["nutrient"]["unitName"]]

                    else:

                        ingredient_nutritionalInfo[key]["nutrients"][foodNutrient["nutrient"]["name"]] = "NA"

            else:

                ingredient_nutritionalInfo[key] = {}

    # ---------------------------- Correcting Units in JSON with Nutritional Info for 1st FDCID ----------------------------
    
    # Converting weights of each of the compounds present in the ingredients to standardized units: milligrams -> grams, micrograms -> grams and kilojoules -> kilocalories. In the case of Vitamin A, Vitamin C, Vitamin D and Vitamin E: International Units (IU) -> grams.

    # Checking for the presence of ingredient_nutritionalInfo_corrected.json file
    if os.path.exists('./vocabulary/ingredient_nutritionalInfo_corrected.json'):

        f = open('./vocabulary/ingredient_nutritionalInfo_corrected.json')
        ingredient_nutritionalInfo_modified = (json.load(f))# [0:100]
        f.close()

    else:

        ingredient_nutritionalInfo_modified = ingredient_nutritionalInfo

        # Ingredient's compounds units conversion
        for nutrient, dictionary in ingredient_nutritionalInfo.items():

            if "nutrients" in dictionary:

                for molecule, quantity in dictionary["nutrients"].items():

                    if quantity != "NA":

                        if quantity[1] == "mg":

                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]/1000
                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

                        elif quantity[1] == "\u00b5g":

                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]/1000000
                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

                        elif quantity[1] == "kJ":

                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]/4.182
                            ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'kcal'

                        elif quantity[1] == "IU":

                            if "Vitamin A" in molecule:

                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]*0.45/1000000
                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

                            elif "Vitamin C" in molecule:

                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]*50/1000000
                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

                            elif "Vitamin D" in molecule:

                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]*40/1000000
                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

                            elif "Vitamin E" in molecule:

                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][0] = quantity[0]*0.8/1000
                                ingredient_nutritionalInfo_modified[nutrient]["nutrients"][molecule][1] = 'g'

    # ---------------------------- Get Vocab Medium Sizes Searching Top 5 FDCIDs  ----------------------------
    
    # The algorithm starts by looking for each fdcId, in the foodPortions, for the keyword "portionDescription". If it does not exist, this means there is no description of a possible average weight in the dataase for this ingredient. In case it exists, the algorithm looks for the keywords "medium" and "Quantity not specified" following this specific order. After, in case this search is not succesful, it searches for the name of the ingredient in "portionDescription" field. If no quantities are available, the medium size of the ingredient is returned NA and no information is made available to the user.

    f = open('./vocabulary/ingredient_fdcIds.json')
    ingredient_fdcIds = (json.load(f))
    f.close()

    ingredient_mediumSize = {}

    for key, value in ingredient_fdcIds.items():

        aux = True

        for id_key, fdcId in enumerate(value["fdcIds"][0:5]): # Top 5 fdcIds were used to look in the FoodData Central for average weigths for each one of the ingredients.

            if not aux:
                break

            URL = "https://api.nal.usda.gov/fdc/v1/" + str(fdcId) + "?api_key=" + API_Key

            # Sending get request and saving the response as response object 
            r = requests.get(url = URL)

            foodPortions = r.json()["foodPortions"]
            i = 0
            first_cycle = True
            second_cycle = False
            third_cycle = False

            while i < len(foodPortions):

                if "portionDescription" in foodPortions[i]:

                    if "medium" in foodPortions[i]["portionDescription"] and first_cycle:

                        ingredient_mediumSize[key] = {"fdcId": fdcId, "description": value["descriptions"][id_key], "weight": foodPortions[i]["gramWeight"]}
                        aux = False
                        break

                    elif i == len(foodPortions) - 1 and first_cycle:
                        i = -1
                        first_cycle = False
                        second_cycle = True
                        third_cycle = False

                    elif "Quantity not specified" in foodPortions[i]["portionDescription"] and second_cycle:

                        ingredient_mediumSize[key] = {"fdcId": fdcId, "description": value["descriptions"][id_key], "weight": foodPortions[i]["gramWeight"]}
                        aux = False
                        break

                    elif i == len(foodPortions) - 1 and second_cycle:
                        i = -1
                        first_cycle = False
                        second_cycle = False
                        third_cycle = True

                    elif key in foodPortions[i]["portionDescription"] and third_cycle:

                        ingredient_mediumSize[key] = {"fdcId": fdcId, "description": value["descriptions"][id_key], "weight": foodPortions[i]["gramWeight"]}
                        aux = False
                        break

                    elif i == len(foodPortions) - 1 and third_cycle:
                        i = -1 
                        ingredient_mediumSize[key] = {"fdcId": "NA", "description": "NA", "weight": "NA"}
                        first_cycle = False
                        second_cycle = False
                        third_cycle = False
                        break
                else:

                    break

                i = i + 1

    # ---------------------------- Save JSON File with Medium Size Info ----------------------------

    with open('./vocabulary/nutritional_data/ingredient_mediumSize_lemmatized_stopwords.json', 'w') as json_file:
        json.dump(ingredient_mediumSize, json_file)