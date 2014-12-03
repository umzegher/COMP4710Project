import ast
from collections import Counter

import apriorialg as ap
from heroes import HEROES

min_support = 0.001

matches = [ast.literal_eval(data) for data in open("dota2_details.txt", 'r').readlines()]

win_teams = [match['win'] for match in matches]
all_teams = win_teams + [match['lose'] for match in matches]

win_sets, win_support = ap.apriori(win_teams, min_support)
all_sets, all_support = ap.apriori(all_teams, min_support)

for i in range(len(win_sets)):
    counter = Counter({heroes: win_support[heroes] / (float(all_support[heroes])*2) * 100 for heroes in win_sets[i]})

    for hero_set in counter.most_common(10):
        hero_list = [HEROES[h] for h in [h for h in iter(hero_set[0])]]

        print ("%-" + str(len(hero_list)*15) + "s%.4f%%") % (", ".join(hero_list), hero_set[1])

    print
