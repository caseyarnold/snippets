"""
Simple program that convers text into mocking format suitable for social media
I.e. What do you mean -> wHaT dO yOu MeAn
"""
def mocking_text(text):
    new_string = ""
    lowercase = True

    for letter in text:
            if lowercase:
                new_string += letter.lower()
                lowercase = False
            else:
                new_string += letter.upper()
                lowercase = True

    return new_string

#print(mocking_text(input('> ')))
