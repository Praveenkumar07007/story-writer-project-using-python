#PYTHON PROJECT

"""Our task is to generate a random story every time the user
runs the program. I will first store the parts of the stories in diffrent
lists, then the Random module can be used to select the random parts of the
story from diffrent lists"""

""" A story is made up of collection of sentences here we use
use random phrases to build sentences."""

#Here we use random module which is already built in module in python.

# First we import random module

import random

#Then we assign a list in the variable and put the elements of the story in the diffrent list.

when = ['A few years ago', 'Yesterday','Last night', 'A long time ago']


Adjective = ["rich","greed","harsh","grubby"]
# here we use Adjective

friends = ['Praveen', 'Manas','Aayush', 'Binod']
# Here we use proper noun

age=['who seemed to be in late 20s','who seemed very old and feeble']

residence = ['Bihar', 'Uttar pradesh', 'Kolkata', 'Punjab']

city_name=["chicago","New york","New delhi","sydney"]

sports_noun = ["ball","helmet","bat","scoreboard"]


noun = ["people","map","music","dog","ball","cat"]



Action_verb = ["run","fall","cry","swim","jump"]

proper_noun = ["desert","forest","store","waterfall"]

food=["ice cream","panipuri","apple","banana"]

Drink = ["coke","water","tea","coffee"]

went = ['cinema','university', 'school', 'laundry']

    
happend = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book']


"""Now we have all the lists with diffrent situations then we randomly select
one item of every list and make a story of it.


with the help of random.choice() select an item from each list and concatenate
the selected items to generate sentences for the story."""

#random.choice() is a function in random module which randomly select a list element from list.

print(random.choice(when) + ', ' +"me and my "+ random.choice(Adjective)+" friend " +random.choice(friends)+" "+random.choice(age)+
      ' that lived in ' +random.choice(residence)+"."+ 'decided to go the'+" " +random.choice(sports_noun)+" "+'game in'+" "
      + random.choice(city_name)+"."+"We really wanted to see the" +" "+random.choice(noun)+" "+" play the "+random.choice(noun)+"."+
      "so,we"+" "+random.choice(Action_verb)+" "+"our"+" "+random.choice(noun)+" "+"down to the"+" "+random.choice(proper_noun)+" "
      +" and bought some foods"+"."+" We got into the game and it was a lot of fun."+" We ate some "+random.choice(food)
      +" and drank some "+random.choice(Drink)+" finally we go to the "+random.choice(went)+" and "+random.choice(happend)+".")

print("I hope you enjoyed this project.")
