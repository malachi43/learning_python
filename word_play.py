


def print_all_lines_in_file(filename):
    fin = open(filename)
    for line in fin:
        print("line: ", line)

def print_lines_with_more_than_20_characters(filename):
    fin = open(filename)
    for line in fin:
        character_count = len(line.strip())
        if character_count > 20:
            print("[ word ] -> ", line.strip(), "  [ word_count ] -> ", len(line))


def print_line_with_no_e(filename):
    fin = open(filename)
    for line in fin:
        if(not line.__contains__("e")):
            print(line)


# check if word contain any of the forbidden letter in forbidden letters.
def avoids(word, forbidden_letters):
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True


print_line_with_no_e("words.txt")