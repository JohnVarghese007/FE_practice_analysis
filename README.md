# Foundation Exam Practice Tracking

This is yet another attempt to analyze and visualize real-world data using `pandas`, `NumPy`, and `Matplotlib`.
The data used in this project is from an excel sheet that I made to track my practice test scores while preparing for my university's Foundation Exam for my major.

## 📊 Features/Points of Focus
- Extracting data from excel sheet to create a DataFrame
- Redjust DataFrame to account for the fact that the table of values in the excel sheet is off-center (i.e doesnt start at (0,0))
- Data cleaning to some small extent - removing exam data with invalid (Pass/Fail) status 
- Visualizes scores and passing lines across timeline using a line chart
- Printing some relevant summary statistics
- Saves the figure to a `.png` file

## 🗂️ Files

- `fe_practice_data_analysis.py` — Main Python script
- `fe_practice_line_chart.png` — Line chart generated using Matplotlib.pyplot
- `ProgressTracking.xlsx` — Data source

## 📦 Requirements

- Python latest version
- Libraries:
  - pandas (main focus)
  - numpy
  - matplotlib

Install requirements (if needed):

```bash
pip install pandas numpy matplotlib