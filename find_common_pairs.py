import ast
from collections import Counter

from heroes import HEROES

matches = [ast.literal_eval(data) for data in open("dota2_details.txt", 'r').readlines()]

win_dictionary = {}
all_dictionary = {}

for match in matches:
    match['win'].sort()
    match['lose'].sort()
    i = 0
    while i < 5:
        j = i+1
        while j < 5:
            
            if (match['win'][i], match['win'][j]) in win_dictionary:
                win_dictionary[ match['win'][i], match['win'][j] ] += 1
            else:
                win_dictionary[ match['win'][i], match['win'][j] ] = 1
                
            if (match['win'][i], match['win'][j]) in all_dictionary:
                all_dictionary[ match['win'][i], match['win'][j] ] += 1
            else:
                all_dictionary[ match['win'][i], match['win'][j] ] = 1
                
            if (match['lose'][i], match['lose'][j]) in all_dictionary:
                all_dictionary[ match['lose'][i], match['lose'][j] ] += 1
            else:
                all_dictionary[ match['lose'][i], match['lose'][j] ] = 1
            
            j+=1
        i+=1
        
counter = Counter()
for key in win_dictionary.keys():
    if all_dictionary[key] >= 50:
        counter.update({ key: win_dictionary[key]/float(all_dictionary[key]) })
    
for hero in counter.most_common(10):
    print "%-20s%-20s %d/%d = %f"%( HEROES[hero[0][0]], HEROES[hero[0][1]], win_dictionary[hero[0]], all_dictionary[hero[0]], round(hero[1], 4))

