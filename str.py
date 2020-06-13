'''
user entering a string
find the position of "str"
find the length of the entire string
find number of words
'''


def main():
    user_string = input("enter a string: ")
    x = find_length(user_string)
    y = find_location(user_string)
    z = find_number_of_words(user_string)

    print("The length of your string is:" , x , y, z )

def find_length(user):
    return len(user)


#find the location of "S" then check the next letter
#if next letter != "T" continue
#if next letter = "T" check the next letter of "R"
def find_location(user):
    
    if "str" in user:
        s = user.find("s")
        t = user.find("t")
        r = user.find("r")

        return "the position of 'str' is ", s,t,r

    return "does not contain str"


#reurns the word count 
def find_number_of_words(user):
    words = user.split(" ")
    word_count = len(words)
    return "The word count is:", word_count

main()