#Poker simulator

from random import *
import matplotlib.pyplot as plt
import numpy as np

win_loss_percentage = 0

def hands_until_win(winning_player, num_players):
    rand_int = randint(1,num_players)
    hands = 1
    while(rand_int != winning_player):
        rand_int = randint(1, num_players)
        hands += 1
    return hands

def simulation_by_trials():
    # This simulates by the number of trials until you wi
    # For a trial = 10, it would run 10 experiments keeping trak
    # of how many hands it took until you win.
    # Let's say that each hand round takes 5 minutes.
    # And a session of poker is 4 hours
    # That is 48 hands. Hmm. Seems low.
    winning_player = 1
    num_players = 5
    trials = 10
    hands_taken_to_win = [0]*100
    for i in range(trials):
        hands = hands_until_win(winning_player, num_players)
        #need to cap it at 1000
        #print(hands)
        hands_taken_to_win[hands] +=1
    #print(hands_taken_to_win)
        



def simulation_by_num_hands(winning_player, num_players, num_hands):
    won_yet = False
    #This is to print out an error
    last_win = 'erk'
    distance_between_wins_counter = [0]*num_hands
    cum_win_rate = [0]*num_hands
    cum_distance_between_wins = [0]*num_hands
    hands_since_last_win = [0] * num_hands
    total_distance_between_wins = 0
    wins = 0
    for i in range(num_hands):
        winner = randint(1, num_players)
        if winner == winning_player:
            if(won_yet == False):
                won_yet = True
                last_win = i
                distance_between_wins_counter[i] += 1
            else:
                distance_between_wins = i - last_win
                total_distance_between_wins += distance_between_wins
                last_win = i
                distance_between_wins_counter[distance_between_wins] += 1
                hands_since_last_win[i] = distance_between_wins
            wins += 1
        if(wins > 0):
            cum_distance_between_wins[i] = total_distance_between_wins / wins
            
        cum_win_rate[i] = (float(1) * wins) / (i+1)
    return distance_between_wins_counter, cum_win_rate, cum_distance_between_wins, hands_since_last_win

#need to research how to dynamically generate graphs. 
winning_player = 1
num_players = 5
num_hands = 10000

#distance between wins - histogram of distance between each win
#cumulative win rate - I don't need an exlanation for this
#cum_distance_between_wins - average distance between every win. 

distance_between_wins, cum_win_rate, cum_distance_between_wins, hands_since_last_win  = simulation_by_num_hands(winning_player, num_players, num_hands)

import matplotlib.pyplot as plt
plt.style.use('ggplot')

x_pos = [i for i, _ in enumerate(distance_between_wins)]

max_range_idx = num_hands
for i in range(len(distance_between_wins)-1, -1, -1):
    if distance_between_wins[i] > 0:
        max_range_idx = i + 1 #add one to include the last idx
        break

#Graph of distance between hands. 
# distance_between_wins_subrange = distance_between_wins[0: max_range_idx]
# x_pos_subrange = x_pos[0:max_range_idx]
# plt.bar(x_pos_subrange, distance_between_wins_subrange, color='blue')
# plt.xlabel("Turns Between Wins")
# plt.ylabel("Wins")
# plt.title("Wins vs. Turns Between Wins")
# plt.xticks(x_pos_subrange, x_pos_subrange)
# plt.show()

#Graph of cumulative win rates
# print(cum_win_rate[-1])
# plt.bar(x_pos, cum_win_rate, color='red')
# plt.xlabel("Current Turn")
# plt.ylabel("Cum Win Percentage")
# plt.title("Cum Probability Distribution")
# plt.xticks(x_pos, x_pos)
# plt.show()

#Graph of average distance between wins
# plt.bar(x_pos, cum_distance_between_wins, color='purple')
# plt.xlabel("Current Turn")
# plt.ylabel("Cum Average Wins Between Turn")
# plt.title("Cum Average Wins Between Turn")
# plt.xticks(x_pos, x_pos)
# plt.show()

# plt.bar(x_pos, hands_since_last_win, color='purple')
# plt.xlabel("Trial")
# plt.ylabel("Distance since last win")
# plt.title("Hands Between Each Win")
# plt.xticks(x_pos, x_pos)
# plt.show()





# l = plt.plot(t1, f(t1), 'ro')
# plt.setp(l, markersize=30)
# plt.setp(l, markerfacecolor='C0')

# plt.show()