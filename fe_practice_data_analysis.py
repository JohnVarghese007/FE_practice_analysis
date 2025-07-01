"""
Author : John Varghese
Date : 6/28/2025
This is yet another attempt to analyze and visualize real-world data using `pandas`, `NumPy`, and `Matplotlib`.
The data used in this project is from an excel sheet that I made to track my practice test scores while preparing for my university's Foundation Exam for my major.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#extract original dataframe
original_df = pd.read_excel(r"algosForML\FE_practice_analysis\ProgressTracking.xlsx",header=None)

#### Note ###
# here we notice that the table of relevant values is off-center #
# upon printing original_df, we will see that in this data set, the table with relevant values only starts at (1,1) #
# The next three lines of code is to ensure that our data frame only has relevant rows and columns #

raw_data_df= original_df.iloc[1:,1:]
raw_data_df.columns = raw_data_df.iloc[0] #reassign columns

#get the cleaned data frame
clean_df = raw_data_df[1:].reset_index(drop=True) 

#further clean df by removing rows with invalid Pass/Fail values
clean_df = clean_df[clean_df['Pass/Fail'].isin(['P', 'F','p','f','Pass','Fail'])]

#make lists of days, scores and passing lines
daysArr = [x for x in range(1,len(clean_df)+1)]
passingLines = clean_df['Passing Line'].tolist()
scores = clean_df['Score'].tolist()

#Optional: print these 3 arrays to ensure that data is accurate

# All output text from this file be printed to a file named 'output__file.txt'
with open(r"algosForML\FE_practice_analysis\output_file.txt","w") as file:
    file.write("LISTS:\n")
    file.write(f"--List of Days: {daysArr}\n")
    file.write(f"--List of Passing lines: {passingLines}\n")
    file.write(f"--List of scores: {scores}\n\n")

#plotting practice line graph with results
plt.figure(facecolor='lightyellow')
plt.plot(daysArr,scores,'o-', color = 'red',label = 'Scores')
plt.plot(daysArr,passingLines,'o-',color = 'green',label = 'Passing Line')
plt.title(f'Foundation Exam Practice Progress across time (t = {len(daysArr)} days)')
plt.xlabel('Days (x)')
plt.ylabel('Scores (y)')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(r"algosForML\FE_practice_analysis\fe_practice_line_chart.png")


#convert scores to numpy array
scores = np.array(scores)

#getting required values
average = np.mean(scores)
median = np.median(scores)
sDev = np.std(scores)
variance = np.var(scores)
modeRes = stats.mode(passingLines,axis = None)

#printing some summary statistics in output file
with open(r"algosForML\FE_practice_analysis\output_file.txt","a") as file:
    file.write("\nSUMMARY STATISTICS\n")
    file.write(f"--Average score: {average}\n")
    file.write(f"--Median score: {median}\n")
    file.write(f"--Standard deviation: {sDev}\n")
    file.write(f"--Variance: {variance}\n")
    file.write(f"--Most common passing line: {modeRes.mode}\n")

#displaying plot
plt.show()

## PIE CHART SHOWING PASS/FAIL PERCENTAGE
pass_count = 0
fail_count = 0

# Loop through the 'Pass/Fail' column
for val in clean_df['Pass/Fail']:
    val_str = str(val).strip().lower() #converts to lowercase
    if val_str.startswith('p'):  # 'p', 'pass', etc.
        pass_count += 1
    else: 
        fail_count += 1

# Create dictionary for plotting
pass_fail_counts = {'Pass': pass_count, 'Fail': fail_count}
plt.figure(figsize=(6,6), facecolor='lightyellow')
plt.pie(pass_fail_counts.values(), labels=pass_fail_counts.keys(),
        autopct='%1.1f%%', colors=['green', 'red'], startangle=90)
plt.title('Pass vs Fail Rate')
plt.tight_layout()
plt.savefig(r"algosForML\FE_practice_analysis\pass_fail_pie_chart.png")
plt.show()

## MANUAL IMPLEMENTATION OF LINEAR REGRESSION ##
# I PRINT OUT THE VALUES GIVEN BY NP.POLYFIT() AT THE END FOR COMPARISON #

x_vals = np.array(daysArr)
y_vals = np.array(scores)
#y = mx+c
y_predicted = 0
m = 0
c = 0
epochs = 5000
learning_rate = 0.005
num_lines = len(y_vals)
mse_history = []
#loop for training
for i in range(epochs):
    y_predicted = m*x_vals +c
    
    #appending MSE history
    mse_history.append(np.mean((y_vals - y_predicted)**2))

    #find gradients of MSE loss function for m and c
    grad_m = (-2/num_lines)*np.sum(x_vals*(y_vals - y_predicted))
    grad_c = (-2/num_lines)*np.sum((y_vals - y_predicted))

    #gradient descent
    m-=learning_rate * grad_m
    c-= learning_rate * grad_c

#printing some insights based on m value
with open(r"algosForML\FE_practice_analysis\output_file.txt","a") as file:
    file.write(f"\nInsights based on slope (m value):\n")
    if m > 0:
        file.write(f"--Your practice scores show an upward trend! \n--slope: {m}\n")
    elif m < 0:
        file.write(f"--Your practice scores show a downward trend! \n--slope: {m}\n")
    else:
        file.write(f"--Your scores largely show no improvement! \n--slope: {m}\n")
    

#plotting true values
plt.figure(facecolor='lightyellow')
plt.plot(x_vals,y_vals,'o',color = 'blue', label = 'Scores')
#plotting trendline
plt.plot(x_vals,m*x_vals+c,color = 'red', label = 'Regression Line')

#add labels, legends and show the plot
plt.xlabel('Days (x)')
plt.ylabel('Scores (y)')
plt.legend()
plt.title('Linear Regression')
plt.grid(True)
plt.tight_layout()
plt.savefig(r"algosForML\FE_practice_analysis\fe_practice_linear_regression.png")
plt.show()

m_actual, c_actual = np.polyfit(x_vals, y_vals, 1)
# Comparing slope and y-intercept values with  results from np.polyfit()  for comparison #
with open(r"algosForML\FE_practice_analysis\output_file.txt","a") as file:
    file.write(f"\nVerifying accuracy of model with np.polyfit()\n")
    file.write(f"--Expected slope according to manual implementation of linear regression for the scores: {m}, intercept: {c}\n")
    file.write(f"--Expected slope according to polyfit: {m_actual}, intercept: {c_actual}\n")

# plotting MSE over epochs
plt.figure(facecolor='lightyellow')
plt.plot(np.arange(0,epochs,1),mse_history,color = 'red', label = 'MSE')
plt.xlabel('Epochs(x)')
plt.ylabel('MSE (y)')
plt.legend()
plt.title(f'Mean Squared Error over Epochs (n={epochs})')
plt.grid(True)
plt.tight_layout()
plt.savefig(r"algosForML\FE_practice_analysis\fe_practice_mse_vs_epochs.png")
plt.show()