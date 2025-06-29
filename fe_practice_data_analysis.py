"""
Author : John Varghese
Date : 6/28/2025
This is yet another attempt to analyze and visualize real-world data using `pandas`, `NumPy`, and `Matplotlib`.
The data used in this project is from an excel sheet that I made to track my practice test scores while preparing for my university's Foundation Exam for my major.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
print("LISTS:")
print(f"List of Days: {daysArr}")
print(f"List of Passing lines: {passingLines}")
print(f"List of scores: {scores}")

#plotting practice line graph with results
plt.figure(facecolor='lightyellow')
plt.plot(daysArr,scores,'o-', color = 'red',label = 'Scores')
plt.plot(daysArr,passingLines,'o-',color = 'green',label = 'Passing Line')
plt.title('Foundation Exam Practice Progress across time (t = 16 days)')
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
mode = max(set(passingLines),key = passingLines.count)

#printing some summary statistics
print("\nSUMMARY STATISTICS")
print(f"Average score: {average}")
print(f"Median score: {median}")
print(f"Standard deviation: {sDev}")
print(f"Variance: {variance}")
print(f"Most common passing line: {mode}")

#displaying plot
plt.show()