# Foundation Exam Practice Tracking

This is yet another attempt to analyze and visualize real-world data using `pandas`, `NumPy`, `SciPy` and `Matplotlib`.
The data used in this project is from an excel sheet that I made to track my practice test scores while preparing for my university's Foundation Exam for my major.

## 📊 Features/Points of Focus
- Extracting data from excel sheet to create a DataFrame
- Re-adjust DataFrame to account for the fact that the table of values in the excel sheet is off-center (i.e doesnt start at (0,0))
- Data cleaning to some small extent - removing exam data with invalid (Pass/Fail) status 
- Visualize scores and passing lines across timeline using a line chart (matplotlb)
- File handling (writing/appending output data to a file)
- Printing some relevant summary statistics and general insights
- Manual Implementation of Linear Regression using Gradient Descent with Visualization using matplotlib
- Comparing training results to values given by np.polyfit() to ensure accuracy of slope and intercept values generated.
- Saves both plots to `.png` files

## 🗂️ Files

- `fe_practice_data_analysis.py` — Main Python script
- `fe_practice_line_chart.png` — Line chart generated using Matplotlib.pyplot
- `fe_practice_line_chart.png` — Linear regression plot using Matplotlib.pyplot
- `ProgressTracking.xlsx` — Data source
- `output_file.txt` — Output saved to a `.txt` file

## 📦 Requirements

- Python latest version
- Libraries:
  - pandas (main focus)
  - numpy
  - matplotlib
  - scipy (only for mode calculation)

Install requirements (if needed):

```bash
pip install pandas numpy matplotlib