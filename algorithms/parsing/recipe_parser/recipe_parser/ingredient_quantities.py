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
    # -------------------------------- Preprocessing Ingredients Vocabulary

    ingredients_vocab.sort(key=order, reverse=True)

    # -------------------------------- Preprocessing Recipe Dataset

    modified_ingredient_sentence = ingredient_sentence

    for word_ingredient_vocab in ingredients_vocab:

        if word_ingredient_vocab in ingredient_sentence and len(word_ingredient_vocab.split(" ")) > 1:
            modified_ingredient_sentence = modified_ingredient_sentence.replace(word_ingredient_vocab,
                                                                                word_ingredient_vocab.replace(" ", "ç"))

    modified_ingredient_sentence = [
        lemmatizer.lemmatize(w.translate(trantab).replace("_", "").replace("ç", " ").lower()) for w in
        word_tokenize(modified_ingredient_sentence)]

    modified_ingredient_sentence2 = [w for w in modified_ingredient_sentence if
                                     w in ingredients_vocab or w in units_vocab or isfraction(w) or w.isnumeric()]

    modified_modified_ingredient_sentence = modified_ingredient_sentence2

    while ("" in modified_modified_ingredient_sentence):
        modified_modified_ingredient_sentence.remove("")

    # -------------------------------- Extracting Ingredients, Quantities and Units

    output = []

    for position, word_ingredient_vocab in enumerate(ingredients_vocab):

        if word_ingredient_vocab in modified_modified_ingredient_sentence:

            for unit in units_vocab:

                if unit in modified_modified_ingredient_sentence and modified_modified_ingredient_sentence[
                    modified_modified_ingredient_sentence.index(
                            unit) - 1].isnumeric() and modified_modified_ingredient_sentence.index(
                        unit) - 2 > -1 and isfraction(modified_modified_ingredient_sentence[
                                                          modified_modified_ingredient_sentence.index(
                                                                  unit) - 2]) and modified_modified_ingredient_sentence.index(
                        unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):

                    fraction = modified_modified_ingredient_sentence[
                        modified_modified_ingredient_sentence.index(unit) - 2].split("/")

                    output.append({"ingredient": word_ingredient_vocab, "quantity": float(
                        modified_modified_ingredient_sentence[
                            modified_modified_ingredient_sentence.index(unit) - 1]) * float(fraction[0]) / float(
                        fraction[1]), "units": unit})

                    break

                elif unit in modified_modified_ingredient_sentence and isfraction(modified_modified_ingredient_sentence[
                                                                                      modified_modified_ingredient_sentence.index(
                                                                                              unit) - 1]) and modified_modified_ingredient_sentence.index(
                        unit) - 2 > -1 and modified_modified_ingredient_sentence[
                    modified_modified_ingredient_sentence.index(
                            unit) - 2].isnumeric() and modified_modified_ingredient_sentence.index(
                        unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):

                    fraction = modified_modified_ingredient_sentence[
                        modified_modified_ingredient_sentence.index(unit) - 1].split("/")

                    output.append({"ingredient": word_ingredient_vocab, "quantity": float(
                        modified_modified_ingredient_sentence[
                            modified_modified_ingredient_sentence.index(unit) - 2]) * float(fraction[0]) / float(
                        fraction[1]), "units": unit})

                    break

                elif unit in modified_modified_ingredient_sentence and modified_modified_ingredient_sentence[
                    modified_modified_ingredient_sentence.index(
                            unit) - 1].isnumeric() and modified_modified_ingredient_sentence.index(
                        unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):

                    output.append({"ingredient": word_ingredient_vocab, "quantity": float(
                        modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(unit) - 1]),
                                   "units": unit})

                    break

                elif unit in modified_modified_ingredient_sentence and modified_modified_ingredient_sentence[
                    modified_modified_ingredient_sentence.index(
                            unit) - 1].isnumeric() and modified_modified_ingredient_sentence.index(unit) - 2 > - 1 and \
                        modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(
                                unit) - 2].isnumeric() and modified_modified_ingredient_sentence.index(
                        unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):

                    output.append({"ingredient": word_ingredient_vocab, "quantity": float(
                        modified_modified_ingredient_sentence[
                            modified_modified_ingredient_sentence.index(unit) - 1]) * float(
                        modified_modified_ingredient_sentence[modified_modified_ingredient_sentence.index(unit) - 2]),
                                   "units": unit})

                    break

                elif unit in modified_modified_ingredient_sentence and isfraction(modified_modified_ingredient_sentence[
                                                                                      modified_modified_ingredient_sentence.index(
                                                                                              unit) - 1]) and modified_modified_ingredient_sentence.index(
                        unit) < modified_modified_ingredient_sentence.index(word_ingredient_vocab):

                    fraction = modified_modified_ingredient_sentence[
                        modified_modified_ingredient_sentence.index(unit) - 1].split("/")

                    output.append(
                        {"ingredient": word_ingredient_vocab, "quantity": float(fraction[0]) / float(fraction[1]),
                         "units": unit})

                    break

                elif modified_modified_ingredient_sentence[
                    modified_modified_ingredient_sentence.index(word_ingredient_vocab) - 1].isnumeric():

                    output.append({"ingredient": word_ingredient_vocab, "quantity": float(
                        modified_modified_ingredient_sentence[
                            modified_modified_ingredient_sentence.index(word_ingredient_vocab) - 1]), "units": None})

                    break

                elif position == len(modified_modified_ingredient_sentence) - 1:

                    output.append({"ingredient": word_ingredient_vocab, "quantity": 1, "units": None})

                    break

    return output