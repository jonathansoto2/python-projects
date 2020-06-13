# In-Class Assignment 3
# Username Generator
# Boston Cartwright, Dallin Kimber, Jonathan Sexy Soto,

'''
 Generate a username for the user with the length of the 
 string attached to the end. The username will be
 the LastName with the initials of the first and middle
 attached to the end and then length.
'''

# main entrance of program
def main():
    # get names
    names = get_users_names()    

    # generate username
    username = generate_username(names)                                

    # print username
    print(username)

# gets the users first, middle, and last name
# returns dictionary with names
# {
#   'first': jonathan,
#   'middle': sexy,
#   'last': soto    
# }
def get_users_names():
    first_name = input("What's your first name? ")
    middle_name = input("What's your middle name? ")
    last_name = input("What's your last name? ")

    if len(first_name) > 25 or len(middle_name) > 25 or len(last_name) > 25:
        print("Invalid names.")
        return get_users_names()

    return {
        'first'  : first_name,
        'middle' : middle_name,
        'last' :   last_name
    }
        
# gets the user names and appends the first and middle initial to the last name 
# with the length at the end
def generate_username(names):
    length = len(names['first']) + len(names['middle']) + len(names['last'])

    username = str.format("@{}{}{}{}",
        names['last'], names['first'][0], names['middle'][0], length)
    return username
    


main()