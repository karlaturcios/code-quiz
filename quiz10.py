# A list of replacement words to be passed in to the quiz function.
blanks  = ["__1__", "__2__", "__3__", "__4__"]
blnks = ""
# A list of answers to replace blanks
answers  = ["world", "python", "print", "html", "function", "variables", "none"]

# the questions
easyquestion = '''Hello __1__!'  In __2__ this is particularly easy; all you have to do is type in: __3__ "Hello __1__!" Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser, but it's a step in learning __2__ syntax, and that's really its purpose.'''

mediumquestion = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

hardquestion = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''

# Asks the player to set difficulty levels
print "Please select a game difficulty by typing it in!"
level = raw_input("Possible choices include easy, medium, and hard.")

# Checks if a word in blanks is a substring
def word_in_blanks(word, blanks):
    for blnks in blanks:
        if blnks in word:
            return blnks
    return None

# Checks if a word in answers is a substring of the word passed in. may not use
def word_in_answers(word, answers):
    for ans in word_in_answers:
        if ans in word:
            return ans
    return None

# replaces blank with userinput in question
def replace_blank(question, user_input):
    blnks = user_input
    return question

# Loops through the quiz
# for a blnk in question loop trhough this request for input
# assign a variable to the blank
# use that variable to loop thought the request for the question what should be substituted for
# replace the variable in question
# print how the question now reads with replacement
# send in the question with the replacement again through the quiz
def quiz(question, blanks):
    tries = 4
    replaced = []
    question = question.split()
    for word in question:
        replacement = word_in_blanks(word, blanks)
        if replacement != None:
            user_input = raw_input("What should be substituted for " + replacement + " ? ")
            if user_input in answers:
                print user_input + " is correct!"
                word = word.replace(replacement, user_input)
                replaced.append(word)
            else:
                while tries != 0:
                    print "That isn't the correct answer!  Let's try again, You have ",tries," trys left!"
                    tries = tries - 1
                    user_input = raw_input("What should be substituted for " + replacement + " ? ")
                else:
                    print "You've failed too many straight guesses!  Game over!"
                    return
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced




#sets questions for level chosen

if level == 'easy':
    # tell users what level they are
    print "You've chosen " + level + " !" + "You will get 5 guesses per problem"
    print "The current paragraph reads: " + easyquestion
    print quiz(easyquestion, blanks)
elif level == 'medium':
         print "You've chosen " + level + " !" + "You will get 5 guesses per problem"
         print "The current paragraph reads: " + mediumquestion
         print quiz(mediumquestion, blanks)
else:
    level == 'hard'
    print "You've chosen " + level + " !" + "You will get 5 guesses per problem"
    print "The current paragraph reads: " + hardquestion
    print quiz(hardquestion, blanks)
