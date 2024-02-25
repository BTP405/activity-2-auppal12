import matplotlib.pyplot as plt # Needed for plotting
import math # Needed for floor function
def createSnowfallFile(filename): 
    m_data = [10, 15, 45, 5, 20, 25]

    with open(filename, 'w') as file:               #'w' expects a string data
        for snowfall in m_data:
            file.write(str(snowfall) + '\n')        #we use str to convert the integer to string

def graphSnowfall(t):

    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file] # Read the data from the file and convert it to integers

    ranges = [0] * 5 # Create a list to store the counts for each range

    for snowfall in snowfall_data: # Count the number of occurrences in each range
        index = math.floor((snowfall - 1) / 10) # Determine the range for the snowfall
        ranges[index] += 1 # Increment the count for the appropriate range

    # Plot the bar chart
    x_labels = [f"{i*10 + 1}-{(i+1)*10}" for i in range(len(ranges))] # Create the labels for the x-axis
    plt.bar(x_labels, ranges, color='blue')
    plt.xlabel('Snowfall Range')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.savefig('snowfall_chart.png') # Save the chart to a file
    plt.show() # Display the chart

filename = 'snowfall_data.txt'

createSnowfallFile(filename)

graphSnowfall(filename)