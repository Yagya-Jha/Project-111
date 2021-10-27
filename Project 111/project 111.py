import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df["claps"].tolist()

population_mean = st.mean(data)
population_standard_devaiation = st.stdev(data)

print('Mean of total Population = ', population_mean)
print('Standard deviation of whole data:- ', population_standard_devaiation)


print('\n')

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        r_index = random.randint(0, len(data)-1)
        value = data[r_index]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

def showfig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["claps"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range (0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    showfig(mean_list)

    # Finding The Standard deviation Starting and Ending Values
    first_std_deviation_start, first_std_deviation_end = population_mean -population_standard_devaiation, population_mean + population_standard_devaiation
    second_std_deviation_start, second_std_deviation_end = population_mean - (2* population_standard_devaiation), population_mean + (2*population_standard_devaiation)
    third_std_deviation_start, third_std_deviation_end = population_mean - (3* population_standard_devaiation), population_mean + (3*population_standard_devaiation)
    print('\n')
    print('Standard Deviation 1 = ', first_std_deviation_start, first_std_deviation_end)
    print('Standard Deviation 2 = ', second_std_deviation_start, second_std_deviation_end)
    print('Standard Deviation 3 = ', third_std_deviation_start, third_std_deviation_end)

    # Plotting the graph with traces
    fig = ff.create_distplot([mean_list], ["claps"], show_hist=False)
    fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 0.17], mode = "lines", name = "Mean"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode = "lines", name = "1_std_start"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode = "lines", name = "1_std_end"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode = "lines", name = "2_std_start"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode = "lines", name = "2_std_end"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode = "lines", name = "3_std_start"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_start], y=[0, 0.17],mode = "lines", name = "3_std_end"))

    sample_mean = st.mean(mean_list)
    print('Mean of Sample Data is: ', sample_mean)
    fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.17], mode = "lines", name = "sample_mean"))
    fig.show()

    if sample_mean > population_mean:
        print("Intervention is successful")

    z_score = (population_mean - sample_mean)/population_standard_devaiation
    print("Z score of data = ", z_score)

setup()