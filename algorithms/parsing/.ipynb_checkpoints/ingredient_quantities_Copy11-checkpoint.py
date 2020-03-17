# Retrieving ingredients, quantities and units for each ingredient present in a given recipe.

# -------------------------------- Importing Packages

import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# -------------------------------- Implementing Auxiliar Functions

def isfraction(s):
    values = s.split('/')
    return len(values) == 2 and all(i.isdigit() for i in values)

def detectIngredientInOutput(s, ingredient):
    
    for ingredient_list in s:
        
        if ingredient in ingredient_list["ingredient"]:
                
            return True
        
    return False

def order(e):
    return len(e)

# -------------------------------- Defining Constants

stop_words = set(stopwords.words('english'))
intab = '''!()-[]{};:'"\,<>?@#$%^&*_~'''
outtab = "_" * len(intab)
trantab = str.maketrans(intab, outtab)

lemmatizer = WordNetLemmatizer()

# -------------------------------- Function Retrieving Ingredients, Quantities and Units

def ingredient_quantities(ingredient_sentence, ingredients_vocab, units_vocab):
    
   output = []

    # -------------------------------- Preprocessing Recipe Dataset
    
    modified_ingredient_sentence = " ".join([lemmatizer.lemmatize(w.translate(trantab).replace("_", "").lower()) for w in ingredient_sentence.split(" ") if w not in stop_words])  
                        
    for word_ingredient_vocab in ingredients_vocab:
        
        if len(word_ingredient_vocab.split(" ")) > 1 and word_ingredient_vocab in modified_ingredient_sentence:
                        
            modified_ingredient_sentence = modified_ingredient_sentence.replace(word_ingredient_vocab, word_ingredient_vocab.replace(" ", "ç"))
            
    modified_ingredient_sentence = modified_ingredient_sentence.split(" ")
                            
    modified_ingredient_sentence2 = [w for w in modified_ingredient_sentence if w in ingredients_vocab or w in units_vocab or isfraction(w) or w.isnumeric()]
        
    modified_modified_ingredient_sentence = modified_ingredient_sentence2
    
    # print(modified_ingredient_sentence)
        
    while("" in modified_modified_ingredient_sentence):
            
        modified_modified_ingredient_sentence.remove("")
        
    # print(modified_modified_ingredient_sentence)
    
    # -------------------------------- Extracting Ingredients, Quantities and Units
    
    for position, word_ingredient_vocab in enumerate(ingredients_vocab): # Iteration over all the ingredients present in the vocaulary input by the user.
                
        if word_ingredient_vocab in modified_modified_ingredient_sentence:
            
            ingredientPosition = modified_modified_ingredient_sentence.index(word_ingredient_vocab)
    
            for unit_index, unit in enumerate(units_vocab):
            
                if unit in modified_modified_ingredient_sentence:
                
                    isIngredientAfterUnit = modified_modified_ingredient_sentence.index(unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab)
                    unitPosition = modified_modified_ingredient_sentence.index(unit)             
            
                    # Integer number immediately before the unit and a fraction before the previous. 

                    if unitPosition - 2 > -1 and modified_modified_ingredient_sentence[unitPosition - 1].isnumeric() and isfraction(modified_modified_ingredient_sentence[unitPosition - 2]) and isIngredientAfterUnit:

                        fraction = modified_modified_ingredient_sentence[unitPosition - 2].split("/")

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[unitPosition - 1]) * float(fraction[0]) / float(fraction[1]), "units": unit})      

                        break

                    # Number immediately before the unit.

                    elif unitPosition - 2 > -1 and isfraction(modified_modified_ingredient_sentence[unitPosition - 1]) and modified_modified_ingredient_sentence[unitPosition - 2].isnumeric() and isIngredientAfterUnit:

                        fraction = modified_modified_ingredient_sentence[unitPosition - 1].split("/")

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[unitPosition - 2]) * float(fraction[0])/float(fraction[1]), "units": unit})

                        break

                    elif unitPosition - 1 > -1 and modified_modified_ingredient_sentence[unitPosition - 1].isnumeric() and isIngredientAfterUnit:

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[unitPosition - 1]), "units": unit})      

                        break

                    elif unitPosition - 2 > - 1 and modified_modified_ingredient_sentence[unitPosition - 1].isnumeric() and modified_modified_ingredient_sentence[unitPosition - 2].isnumeric() and isIngredientAfterUnit:

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[unitPosition - 1]) * float(modified_modified_ingredient_sentence[unitPosition - 2]), "units": unit})      

                        break

                    elif unitPosition - 1 > -1 and isfraction(modified_modified_ingredient_sentence[unitPosition - 1]) and isIngredientAfterUnit:

                        fraction = modified_modified_ingredient_sentence[unitPosition - 1].split("/")

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(fraction[0])/float(fraction[1]), "units": unit})

                        break
                        
                elif unit_index == len(units_vocab) - 1:                  

                    if ingredientPosition - 1 > - 1 and modified_modified_ingredient_sentence[ingredientPosition - 1].isnumeric():

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[ingredientPosition - 1]), "units": None})

                        break

                    elif ingredientPosition - 2 > - 1 and modified_modified_ingredient_sentence[ingredientPosition - 2].isnumeric():

                        output.append({"ingredient": word_ingredient_vocab, "quantity": float(modified_modified_ingredient_sentence[ingredientPosition - 2]), "units": None})

                        break

                    else:

                        output.append({"ingredient": word_ingredient_vocab, "quantity": 1.0, "units": None})

                        break
                    
    return output