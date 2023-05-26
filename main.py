# Name: Dong Sy Nhat Thanh
# ID: GCS210033
# Class: GCS1003A

#Just for in case: remember to comment to one of 2 codes below to run the other one

#////////////1////////////
name = input("Type your name:")
age = int(input("Type your age:"))
entrance= int(input("Type your entrance:"))

year = 2023-entrance

def get_information(name,age,entrance):
    print("My name is", name, ", I am", age, "years old", ", I am", entrance, "year student at Greenwich" ) 

get_information(name, age, entrance)



#////////////2////////////
#input information
text = input("Enter your text here: ")
order = int(input("Enter your order here: "))
word_replace = input("Enter your word replace here: ")

#text change
def change_word(text, order, word_replace):
    text[order] = word_replace
    return ' '.join(text).split()

#original text
original_text = text.split()
original_text_count = len(original_text)
print("Original text length: ", original_text_count)

#replace text 
modified_text = change_word(original_text, order, word_replace)
modified_count_text = len(modified_text)
print("Text after replace: ", modified_text)
print("Text length after replace: ", modified_count_text)