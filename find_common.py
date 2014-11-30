import ast
from collections import Counter

from heroes import HEROES

matches = [ast.literal_eval(data) for data in open("dota2_details.txt", 'r').readlines()]

win_counter = Counter()
all_counter = Counter()
for match in matches:
    win_counter.update(match['win'])
    all_counter.update(match['win'])
    all_counter.update(match['lose'])

counter = Counter({hero: win_counter.get(hero) / float(all_counter.get(hero)) for hero in HEROES.keys()})

for hero in counter.most_common(10):
    print HEROES[hero[0]], round(hero[1], 4)

