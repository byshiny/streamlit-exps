import streamlit as st
import plotly.express as px
#What I want to do for today

# Learn Svelte
# Create that simulation for matching AGAIN
# Translate every word to Korean. Maybe flashcards
# Translate a good Russian movie to English with pictures


# min_matches = st.slider("Minimum number of matches", min_num_matches, max_num_matches, 10)
import random

rand = random.random()
print(rand)

# optimal matching strategy

#create a list of random numbers between 0 and 1 in a list

num_people = 100
compatibility = [random.random() for i in range(num_people)]

#how do you determine the optimal strategy?
#you know that the optimal strategy 

num_rounds = 1000

#we know that the right strategy is sample 1/3 of the time

#how can you explore other optimal strategies?

#What if you don't know the total number of matches? How would your strategy change then?

# number_to_sample = st.slider("Minimum number of matches", min_num_matches, max_num_matches, 10)

#create a slider that you choose between 0.0 and 1.0 in streamlist



def run_simulation(num_people, percant_to_sample):
    people_vals = [random.random() for i in range(num_people)]

    #select the highest number from the list 
    top_val = max(people_vals)

    #number of people to sample
    num_to_sample = int(num_people * percant_to_sample)

    #get the top number from the sample
    top_sample = max(people_vals[:num_to_sample])

    #get the top value from the rest of the other people
    top_rest = max(people_vals[num_to_sample:])

    found_best_match = top_rest > top_sample

    return found_best_match


percentage_to_sample = st.slider("Percentage to sample", 0.0, 1.0, 0.33)


def get_sim_success_percentage(num_sims_to_run, percentage_to_sample):
    
    found_match_counter = 0
    for i in range(num_sims_to_run):
        found_best_match = run_simulation(num_people, percentage_to_sample)

        if found_best_match:
            # print("Found best match")
            found_match_counter += 1
        # else:
            # print("Did not find best match")

    success_rate = found_match_counter / num_sims_to_run
    return success_rate

#list numbers from 0 to 1 in 0.01 increments

nums_to_sample = [i / 100 for i in range(100)]

num_sims_to_run = 1000

success_rates = [get_sim_success_percentage(num_sims_to_run, p_sample) for p_sample in nums_to_sample]
print("herro")
#plot success rates over percentage to sample
print(success_rates)
fig = px.bar(success_rates)
st.plotly_chart(fig)
