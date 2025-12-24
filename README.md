<h1>Data Visualization & Cleaning Dashboard</h1> 

A simple Python Streamlit-based dashboard for visualizing, cleaning, and analyzing CSV datasets interactively.

<h2>Features</h2>
<ul>
<li>Upload CSV files</li>
<li>Interactive data visualization</li>
<ul>
  <li>Bar Chart</li>
  <li>Line Chart</li>
  <li>Scatter Plot</li>
  <li>Pie Chart</li>
</ul>
<li>Missing value analysis</li>
<li>Data cleaning options (drop / fill missing values)</li
<li>Download cleaned dataset</li>
<li>Multi-page dashboard layout</li>
</ul>

<h2>Requirements</h2> 
<ul>
<li>Python 3.8+</li>
<li>Streamlit</li>
<li>Pandas</li>
<li>Matplotlib</li>
</ul>

<h2>Getting Started</h2>

1️. Clone the repository or download the project folder

2️. Install dependencies

pip install -r requirements.txt

3️. Run the application

streamlit run app.py

<h2>File Structure</h2>
<ul>
<li>Home.py</li> 
<li>Data_Overview.py</li>
<li>Data_Visualizer.py</li> 
<li>Data_Cleaning.py</li> 
<li>Data_Analysis.py</li>
</ul>

<h2>How to Use</h2>

1. Launch the application using streamlit run app.py

2. Navigate to Data Overview from the sidebar

3. Upload a CSV dataset

4. Explore visualizations in the Visualizations page

5. Clean missing values in the Data Cleaning page

6. Analyze numeric data

7. Download the cleaned dataset

<h2>How Data Cleaning Works</h2>

The dashboard provides multiple strategies to handle missing data:
<ul>
<li>Drop Rows: Removes rows containing missing values</li>
<li>Fill with Mean: Replaces missing numeric values with column mean</li>
<li>Fill with Median: Replaces missing numeric values with column median</li>
</ul>