from pprint import pprint
from characters import characters
from houses import houses



#Find every character with name starting with 'a' then return total number of characters
def char_sort(characters):
    index = 0
    letter = input("Welcome to the Game of Thrones character list! Please type the first letter that all names in the list will start with. ").upper()
    for character in characters:
        if character['name'][0] == letter:
            pprint(character['name'])
            index += 1
    pprint(f"There are {index} characters whose name begins with the letter {letter}.")
        
char_sort(characters)

#Returns number of characters who have died thus far
def dead_counter(characters):
    index = 0
    for character in characters:
        if character['died'] != "":
            index += 1
    pprint(f"Sound the horns of burial! Currently, {index} of the characters that have been introduced in Game of Thrones are dead now. Womp womp.") 

dead_counter(characters)

#Returns character in series with greatest number of titles
def most_titles(characters):
    title_list = []
    for character in characters:
        if character["titles"][0] != '':
            title_number = len(character["titles"])
            title_list.append(title_number)
            if title_number >= (max(title_list)):
                character_name = character['name']
                titles = character["titles"] 
                pprint(f"The character with the most titles in the GoT universe is {character_name}, whose titles are {titles}.")

most_titles(characters)

#Returns number of Valyrians
def valyrian_count(characters):
    index = 0
    for character in characters:
        if character["culture"] == "Valyrian":
            index += 1
    print(f"There are {index} Valyrians in the GoT Universe.")

valyrian_count(characters)

#Uses api to return name of actor who plays character who goes by alias
def hot_pie(characters):
    for character in characters:
        if character["aliases"] == "Hot Pie":
            print(character["playedBy"])

hot_pie(characters)

#Returns number of character that appear in the books but not the HBO series
def no_show(characters):
    index = 0
    for character in characters:
        if character["tvSeries"] == ['']:
            index += 1
    print(f"There are {index} characters that appear in the books, but not in any season of the TV show.")

no_show(characters)

#Prints name of every member of the Targaryen family
def targaryen_family(characters):
    for character in characters:
        if 'Targaryen' in character["name"]:
            print(character["name"])

targaryen_family(characters)

#Returns number of members in each house. Unfinished.
"""def house_members(characters):
    histogram = {}
    for character in characters:
        for house in houses:
            histogram.update({character["name"]: houses.values()})
            print(histogram)"""

# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))