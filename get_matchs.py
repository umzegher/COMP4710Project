#!/usr/bin/python

import json
import urllib2
import time

API_KEY = "071AA5E4FB2CDDE32E7DC7638AC884DD"
URL = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistoryBySequenceNum/V001/?key=%s&start_at_match_seq_num=%s"

seq_num = "942557688"

total_count = 0
valid_count = 0
abandon_count = 0
bad_mode_count = 0

while True:
    try:
        matches = json.load(urllib2.urlopen(URL % (API_KEY, seq_num)))['result']['matches']
    except urllib2.URLError:
        print "URLError waiting 30 seconds"
        time.sleep(30)
        continue
    
    seq_num = matches[-1]['match_seq_num']+1
    
    for match in matches:
        total_count += 1
        
        # Only allow All Pick and Captain's Mode matches
        if match['game_mode'] in (1, 2):
            # Exclude abandoned matches
            abandon = False
            for player in match['players']:
                if 'leaver_status' not in player or player['leaver_status'] != 0:
                    abandon = True
                    break

            if not abandon:
                valid_count += 1
                radiant = []
                dire = []
                
                for player in match['players']:
                    if player['player_slot'] >> 7:
                        dire.append(player['hero_id'])
                    else:
                        radiant.append(player['hero_id'])
                
                if match['radiant_win']:
                    match_short = {'win': radiant, 'lose': dire}
                else:
                    match_short = {'win': dire, 'lose': radiant}
                
                with open("dota2_details.txt", 'a') as file:
                    file.write("%s\n" % str(match_short))
            else:
                abandon_count += 1
        else:
            bad_mode_count += 1

    print "Total: %d  Valid: %d  Abandon: %d  Bad mode: %d" % (total_count, valid_count, abandon_count, bad_mode_count)
    time.sleep(1) # Limit requests to 1 per second so we don't exceed API limits
