#Functions DRY = Don't Repeat Yourself
"""
def say_hi(name = 'Dean', nickname = "puppy"):  # Default value
    #Doc string, function says hi ¿what does this function do or why does it exist?
    print("hi {}! {}".format(name, nickname))


say_hi()
say_hi("Sam", "moose")
help(say_hi)  # type q to exit the help screen

# even = par odd = impar
"""

# Exercise 1

def get_word(word_type):
    """Get a word from a user and return that word."""
    if word_type == 'adjetive':
        is_a_an = 'an'
    else:
        is_a_an = 'a'
    return input("Enter a word that is {0} {1}: ".format(is_a_an, word_type))

def fill_in_the_blanks(noun, verb, adjective):
    """Fills in the blanks and returns a completed story."""
    story = "In this course you will learn how to {1}.  It’s so easy even a {0} can do it.  Trust me, it will be very {2}.".format(noun, verb, adjective)
    return story

def display_story(story):
    """Displays a story."""
    print(story)
    
def create_story():
    """Creates a story by capturing the input and displaying a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjetive = get_word('adjetive')
    display_story(fill_in_the_blanks(noun,verb,adjetive))


create_story()

    
