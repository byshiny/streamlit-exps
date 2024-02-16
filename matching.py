import streamlit as st
import plotly.express as px
# launch streamlit


# min_matches = st.slider("Minimum number of matches", min_num_matches, max_num_matches, 10)
import random

rand = random.random()
print(rand)

# optimal matching strategy

#create a list of random numbers between 0 and 1 in a list

top_n = st.slider("Top N", 1, 50, 1, help="Which ")
num_people = st.slider("Number of people", 1, 1000, 100)
compatibility = [random.random() for i in range(num_people)]

noise_error = st.slider("Noise error(Gaussian)", 0.0, 1.0, 0.0)



#how do you determine the optimal strategy?
#you know that the optimal strategy 

num_rounds = st.slider("Number of simulations", 1, 10000, 100)

#we know that the right strategy is sample 1/3 of the time

#how can you explore other optimal strategies?

#What if you don't know the total number of matches? How would your strategy change then?

# number_to_sample = st.slider("Minimum number of matches", min_num_matches, max_num_matches, 10)

#create a slider that you choose between 0.0 and 1.0 in streamlist

#something in my analysis incorrect



def run_simulation(num_people, percent_to_sample):
    people_vals = [random.random() for i in range(num_people)]

    #number of people to sample
    if percent_to_sample == 0:
        raise Exception("percent_to_sample cannot be 0")
    num_to_sample = int(num_people * percent_to_sample)
    #get the top number from the sample

    #get the nth highest number 

    nth_best_person = sorted(people_vals, reverse=True)[top_n]
    top_sampled_person = max(people_vals[:num_to_sample])
    top_sampled_person_index = people_vals.index(top_sampled_person)

    # sample again with noise added to each element in people_vals
    noise = [random.gauss(0, noise_error) for i in range(num_people)]
    noisy_people_vals = [people_vals[i] + noise[i] for i in range(num_people)]

    noisy_top_sampled_person_idx = noisy_people_vals.index(max(noisy_people_vals[:num_to_sample]))
    noisy_top_sampled_person = noisy_people_vals[noisy_top_sampled_person_idx]


    people_remaining_actual = people_vals[num_to_sample:]



    people_remaining_noised = noisy_people_vals[num_to_sample:]

    #get the top value from the rest of the other people
    found_best_match = False
    next_best_chosen_person_idx = None

    for i in range(len(people_remaining_noised)):
        val = people_remaining_noised[i]
        #There's a bit of flaw in reasoning in here. Depending on the situation,
        # you would want to keep val and keep sampling, no? 
        if val > noisy_top_sampled_person:
            next_best_chosen_person_idx = i
            break
    

    found_mate = False
    if next_best_chosen_person_idx is not None:
        found_mate = True
    
    if next_best_chosen_person_idx is None:
        found_mate = False
        found_best_match = False

    else:
        next_best_chosen_person = people_remaining_actual[next_best_chosen_person_idx]

        if next_best_chosen_person >= nth_best_person:
            found_best_match = True
    

    return found_best_match, found_mate

percentage_to_sample = st.slider("Percentage to sample", 0.01, 1.0, 0.33)

def get_sim_success_percentage(num_sims_to_run, num_people, percentage_to_sample):
    
    found_best_match_counter = 0
    found_match_counter = 0
    for i in range(num_sims_to_run):

         # this is bad code could probably simplify this into a single liner
        found_best_match = False
        found_mate = False
        try :
            found_best_match, found_mate = run_simulation(num_people, percentage_to_sample)
        except Exception as e:
            print("error")
            print(e)

 
        if found_best_match:
            found_best_match_counter += 1
        if found_mate:
            found_match_counter += 1

 
    success_rate = found_best_match_counter / num_sims_to_run
    found_rate = found_match_counter / num_sims_to_run
    return success_rate, found_rate

#list numbers from 0 to 1 in 0.01 increments

#create a streamlit slider that ranges from 10 to 1000
divider = st.slider("Number of people", 10, 1000, 100)

nums_to_sample = [float(i) / 100 for i in range(100)]

# nums_to_sample = [0.1, 0.37, 0.5]

#number of people per experiment
num_people = 100

#how many simulates to run
num_sims_to_run = 1000

success_rate_and_found_rates = [get_sim_success_percentage(num_sims_to_run, num_people, p_sample) for p_sample in nums_to_sample]

#create an array of success rate 
success_rates = [x[0] for x in success_rate_and_found_rates]
found_rates = [x[1] for x in success_rate_and_found_rates]

# #plot success rate and found rates as a scatter plot with lines connecting them
fig = px.scatter()
#add a label to the figure 
fig.add_scatter(x=nums_to_sample, y=success_rates, mode="lines", name="Success Rate")
fig.add_scatter(x=nums_to_sample, y=found_rates, mode="lines", name="Found Rate")
st.plotly_chart(fig)
