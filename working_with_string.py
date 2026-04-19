

def find(word,letter,index):
    if index >= len(word):
        return -1
    current_index = index
    while current_index < len(word):
        if word[current_index] == letter:
            return current_index
        current_index = current_index + 1
    return -1


def countLetter(word,letter,index):
    if index >= len(word):
        return 0
    current_index = index
    counter = 0
    while current_index < len(word):
        if word[current_index] == letter:
            counter = counter + 1
        current_index = current_index + 1
    return counter



word = "banana"
upperWord = word.upper()
print("upperWord: ", upperWord)
print("find index of 'n' in banana: ", word.find("n"))
print("find index of 'n' in banana starting from index 3: ", word.find("n",3))


def is_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)


is_both("malachi","chibuike")
 
def rotate_word(word, rotate_number):
    word = word.lower()
    rotated_word = ""
    for char in word:
        num = ( ord(char) + rotate_number ) % 123
        print("num: ", num)
        rotated_word = rotated_word + chr(num)

    return rotated_word


word = "znynpuv"
print("rotated '" + word + "' to: ", rotate_word(word,-13))