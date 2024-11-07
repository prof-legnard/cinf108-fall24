# Lab 6 - Exploring data with Pandas and Python

This lab is meant to test your critical thinking ability, creativity, as well as force you think outside the box of following directions in order to solve a problem or find insights in a dataset. You will be graded on your ability to find insight from ddata, present it,
as well as your ability to work with Python, and the pandas data-analysis library.  You may want to review and use the Demo Jupyter Notebook from the Lecture Notes section on Brightspace as a starting point.

### Step 1. Get the Data (2 points)
- Find a public dataset to do your analysis on. Make sure it's a manageable # of rows, or only one file if you're not comfortable with reading in more than one into one dataframe.
- Create a jupyter notebook file called `lastname_firstname_lab6.ipybnb`
- Use pandas to read the dataset (either from a file on your computer or from a public endpoing) into a `Dataframe`.

#### Sources you can use to find data
Use the following to find a dataset that looks interesting, you are not limited to these sites and may find your own. 
**Please provide a link to the dataset regardless of which source you use. I'd like to be able to load it in and follow along when I grade your submission.**
**Do not use the Iris dataset, I want to see you working with a different source of data and creating analytical insights off of them.**
- Public Datasets provided by the government: https://catalog.data.gov/dataset?q=&sort=views_recent+desc
- Kaggle Datasets: https://www.kaggle.com/datasets
- Google's Dataset search engine: https://datasetsearch.research.google.com/

### Step 2. Data Exploration (5 points)
Once you have a dataframe loaded into a variable `df` or `my_df`, let's take a look at what the dataset is composed of and what it looks like.
- [describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) the data, show what fields it's composed of
- display the [shape](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) of your dataframe
- show the first or last 5 records of your dataset, or provide a sample
- calculate the average and median value for two numerical columns of interest in your dataset.

### Step 3  Cleaning the data (no points, but may be required to graph your data properly)
Your dataset may be missing values, have nulls in certain places, or have text data in a column that should be all numbers or numerical values. 
- Use methods like `.dropna`, `.fillna` to get rid of empty or null values.
- Use advanced text processing methods like `split`, `strip`, or even regular expressions to clean up numerical fields that may have strings in them. Review the lecture notes on  Advanced String processing, and review [this guide](https://realpython.com/python-data-cleaning-numpy-pandas/) on cleaning data in Python

### Step 4 Discover Insights (5 points)

Comb throught the pandas documentation to find at least 2 trends in your data. What do I mean by trends? If you refer back to the Iris dataset we practiced with in class, we graphed things like sepal length vs petal length.

A good starting point will be to look at the correlation between columns (variables) in your dataset. Create a heatmap using seaborn or matplotlib. You may need to create a new dataframe with _only_ the numerical columns.

### Graph your data (10 points)
Of your two findings or relationships you found between two data points, graph your findings. You may use, [matplotlib](https://matplotlib.org/stable/plot_types/index.html), or [seaborn](https://seaborn.pydata.org/). Review some of the documentation and example graphs to find the right way to represent your findings.

**Provide graph titles, labels for your X and Y axis, and a legend or labels of subcategory of data you graph.**

Ex. The iris datset - What is the overall trend of sepal length vs. petal length? (line graph or bar graph)
Ex2. Dataset containing NYC taxi and ride-share data - What is the total number of rides for each taxi type for each month represented in the dataset? (line graph or bar graph)
Ex3. A box and whisker plot showing statistics for home sales for different types of properties (condo, multi-family, residential, etc..)

The sky is the limit here, but make sure you are documentating what you are analysing as well as your findings. If you are having trouble figuring out how to identify trends, send me an email or Slack message with a link to your dataset and we can find things for you to graph.


### Step 5. Presenting and organizing your findings (3 points)
All cells utilizing Python should have a markdown cell with a heading and optionally, a description of the code below it. Go back and clean up all of your code cells, remove commented out code you don't need, and add markdown cells above them with headers:

## like this

# or this

#### or this

For an introduction on markdown headings, look at the source code for this file, [and review this guide on Markdown Basics](https://www.markdownguide.org/basic-syntax/).

