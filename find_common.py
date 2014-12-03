import ast
from collections import Counter

import apriorialg as ap
from heroes import HEROES

min_support = 0.01

matches = [ast.literal_eval(data) for data in open("dota2_details.txt", 'r').readlines()]

win_teams = [match['win'] for match in matches]
all_teams = win_teams + [match['lose'] for match in matches]

win_sets, win_support = ap.apriori(win_teams, min_support)
all_sets, all_support = ap.apriori(all_teams, min_support/10)

for i in range(len(win_sets)):
    counter = Counter({heroes: win_support[heroes] / float(all_support[heroes]) for heroes in win_sets[i]})
    
    for hero_set in counter.most_common(10):
        print ", ".join([HEROES[h] for h in [h for h in iter(hero_set[0])]]), win_support[hero_set[0]], "/", all_support[hero_set[0]], "=", round(hero_set[1], 4)
    
    print
