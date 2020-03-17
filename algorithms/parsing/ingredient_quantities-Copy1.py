# Retrieving units and quantities of each ingredient present in a given recipe.

import re

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def ingredient_quantities(ingredient_sentence, ingredients_vocab, units_vocab):
    
    output = []

    # -------------------------------- Preprocessing Recipe Dataset

    stop_words = set(stopwords.words('english'))
    punctuationAndNumbers = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    intab = punctuationAndNumbers
    outtab = "_" * len(punctuationAndNumbers)
    trantab = str.maketrans(intab, outtab)

    lemmatizer = WordNetLemmatizer()

    word_tokens = word_tokenize(ingredient_sentence)

    modified_ingredient_sentence = [lemmatizer.lemmatize(w.translate(trantab).replace("_", "").lower()) for w in word_tokens if w not in stop_words]
    
    modified_modified_ingredient_sentence = modified_ingredient_sentence
    
    print(modified_ingredient_sentence)
    
    for keyy, ingredient_tokenized_text in enumerate(modified_ingredient_sentence):
        
        #while("" in ingredient_tokenized_text) :
            
            #modified_modified_ingredient_sentence[keyy].remove("")
    
    # -------------------------------- Extracting Ingredients, Quantities and Units
    
    for word_ingredient_vocab in ingredients_vocab:
        
        if word_ingredient_vocab in modified_modified_ingredient_sentence:
    
            for unit in units_vocab:
        
                if unit in modified_modified_ingredient_sentence and len(modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(unit) - 1]) == 2 and re.search(r"[1-5][2-9]", modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(unit) - 1]) and modified_modified_ingredient_sentence.index(unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):
                            
                    output.add({"ingredient": word_ingredient_vocab, "quantity": re.search(r"[1-5][2-9]", modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(unit) - 1]), "units": unit})       
                
    return output

