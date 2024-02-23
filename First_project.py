#!/usr/bin/env python
# coding: utf-8

# Hello Muhammad!
# 
# My name is Dmitry.  I'm glad to review your work today.
# I will mark your mistakes and give you some hints how it is possible to fix them. We are getting ready for real job, where your team leader/senior colleague will do exactly the same. Don't worry and study with pleasure! 
# 
# Below you will find my comments - **please do not move, modify or delete them**.
# 
# You can find my comments in green, yellow or red boxes like this:
# 
# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Success. Everything is done succesfully.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Remarks. Some recommendations.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Needs fixing. The block requires some corrections. Work can't be accepted with the red comments.
# </div>
# 
# You can answer me by using this:
# 
# <div class="alert alert-block alert-info">
# <b>Student answer.</b> <a class="tocSkip"></a>
# 
# Text here.
# </div>

# ## Basic Python - Project <a id='intro'></a>

# ## Introduction <a id='intro'></a>
# In this project, you will work with data from the entertainment industry. You will study a dataset with records on movies and shows. The research will focus on the "Golden Age" of television, which began in 1999 with the release of *The Sopranos* and is still ongoing.
# 
# The aim of this project is to investigate how the number of votes a title receives impacts its ratings. The assumption is that highly-rated shows (we will focus on TV shows, ignoring movies) released during the "Golden Age" of television also have the most votes.
# 
# ### Stages 
# Data on movies and shows is stored in the `/datasets/movies_and_shows.csv` file. There is no information about the quality of the data, so you will need to explore it before doing the analysis.
# 
# First, you'll evaluate the quality of the data and see whether its issues are significant. Then, during data preprocessing, you will try to account for the most critical problems.
#  
# Your project will consist of three stages:
#  1. Data overview
#  2. Data preprocessing
#  3. Data analysis

# ## Stage 1. Data overview <a id='data_review'></a>
# 
# Open and explore the data.

# You'll need `pandas`, so import it.

# In[1]:


# importing pandas
import pandas as pd


# Read the `movies_and_shows.csv` file from the `datasets` folder and save it in the `df` variable:

# In[2]:


# reading the files and storing them to df
df = pd.read_csv('/datasets/movies_and_shows.csv')


# Print the first 10 table rows:

# In[3]:


# obtaining the first 10 rows from the df table
# hint: you can use head() and tail() in Jupyter Notebook without wrapping them into print()
df.head(10)


# Obtain the general information about the table with one command:

# In[4]:


# obtaining general information about the data in df
df.info()


# The table contains nine columns. The majority store the same data type: object. The only exceptions are `'release Year'` (int64 type), `'imdb sc0re'` (float64 type) and `'imdb v0tes'` (float64 type). Scores and votes will be used in our analysis, so it's important to verify that they are present in the dataframe in the appropriate numeric format. Three columns (`'TITLE'`, `'imdb sc0re'` and `'imdb v0tes'`) have missing values.
# 
# According to the documentation:
# - `'name'` — actor/director's name and last name
# - `'Character'` — character played (for actors)
# - `'r0le '` — the person's contribution to the title (it can be in the capacity of either actor or director)
# - `'TITLE '` — title of the movie (show)
# - `'  Type'` — show or movie
# - `'release Year'` — year when movie (show) was released
# - `'genres'` — list of genres under which the movie (show) falls
# - `'imdb sc0re'` — score on IMDb
# - `'imdb v0tes'` — votes on IMDb
# 
# We can see three issues with the column names:
# 1. Some names are uppercase, while others are lowercase.
# 2. There are names containing whitespace.
# 3. A few column names have digit '0' instead of letter 'o'. 
# 

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Great start!
# </div>

# ### Conclusions <a id='data_review_conclusions'></a> 
# 
# Each row in the table stores data about a movie or show. The columns can be divided into two categories: the first is about the roles held by different people who worked on the movie or show (role, name of the actor or director, and character if the row is about an actor); the second category is information about the movie or show itself (title, release year, genre, imdb figures).
# 
# It's clear that there is sufficient data to do the analysis and evaluate our assumption. However, to move forward, we need to preprocess the data.

# ## Stage 2. Data preprocessing <a id='data_preprocessing'></a>
# Correct the formatting in the column headers and deal with the missing values. Then, check whether there are duplicates in the data.

# In[5]:


# the list of column names in the df table
df = df.reindex(sorted(df.columns), axis=1)
print(df.columns)


# Change the column names according to the rules of good style:
# * If the name has several words, use snake_case
# * All characters must be lowercase
# * Remove whitespace
# * Replace zero with letter 'o'

# In[6]:


# renaming columns
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('0', 'o').str.replace('_n', 'n').str.replace('__', '')
print(df.columns)


# Check the result. Print the names of the columns once more:

# In[7]:


# checking result: the list of column names
print(df.columns)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Correct.
#     
# Pro tip: we can use df.rename() also.
# </div>

# ### Missing values <a id='missing_values'></a>
# First, find the number of missing values in the table. To do so, combine two `pandas` methods:

# In[8]:


# calculating missing values
missing_values = df.isnull()
missing_values_count = missing_values.sum()
print(missing_values_count)


# Not all missing values affect the research: the single missing value in `'title'` is not critical. The missing values in columns `'imdb_score'` and `'imdb_votes'` represent around 6% of all records (4,609 and 4,726, respectively, of the total 85,579). This could potentially affect our research. To avoid this issue, we will drop rows with missing values in the `'imdb_score'` and `'imdb_votes'` columns.

# In[9]:


# dropping rows where columns with title, scores and votes have missing values
df.dropna(subset=['title', 'imdb_score','imdb_votes'], inplace=True)


# Make sure the table doesn't contain any more missing values. Count the missing values again.

# In[10]:


# counting missing values
new_missing = df.isnull()
new_count = new_missing.sum()
print(new_count)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# </div>

# ### Duplicates <a id='duplicates'></a>
# Find the number of duplicate rows in the table using one command:

# In[11]:


# counting duplicate rows
duplicate_count = df.duplicated().sum()
print(duplicate_count)


# Review the duplicate rows to determine if removing them would distort our dataset.

# In[12]:


# Produce table with duplicates (with original rows included) and review last 5 rows
duplicate_df = df[df.duplicated(keep='last')]
first_5_rows = duplicate_df.head(5)
print(first_5_rows)


# <div class="alert alert-block alert-warning">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# It's better to use df.head() to increase readability.
# </div>

# There are two clear duplicates in the printed rows. We can safely remove them.
# Call the `pandas` method for getting rid of duplicate rows:

# In[13]:


# removing duplicate rows
df.drop_duplicates(inplace=True)


# Check for duplicate rows once more to make sure you have removed all of them:

# In[14]:


# checking for duplicates
duplicates = df[df.duplicated()]
if duplicates.empty:
    print('no duplicates found')
else:
    print('data still have duplicates, and the duplicates are:')
    


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Uh oh! Something went wrong — let's take a look!
#     
# We still have duplicates. df.drop_duplicates() performs NOT inplace operation. We need to set inplace=True or reassign df.
#     
# We can check duplicates with df.duplicated().sum() also.
# </div>

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Good job.
# </div>

# Now get rid of implicit duplicates in the `'type'` column. For example, the string `'SHOW'` can be written in different ways. These kinds of errors will also affect the result.

# Print a list of unique `'type'` names, sorted in alphabetical order. To do so:
# * Retrieve the intended dataframe column 
# * Apply a sorting method to it
# * For the sorted column, call the method that will return all unique column values

# In[15]:


# viewing unique type names
types_sort = df['type']
sorted_types = types_sort.sort_values()
unique_types = sorted_types.unique()
print(unique_types)


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Please elaborate error in this cell.
#     
# Also, do not forget to rerun whole project before sending!
# </div>

# Look through the list to find implicit duplicates of `'show'` (`'movie'` duplicates will be ignored since the assumption is about shows). These could be names written incorrectly or alternative names of the same genre.
# 
# You will see the following implicit duplicates:
# * `'shows'`
# * `'SHOW'`
# * `'tv show'`
# * `'tv shows'`
# * `'tv series'`
# * `'tv'`
# 
# To get rid of them, declare the function `replace_wrong_show()` with two parameters: 
# * `wrong_shows_list=` — the list of duplicates
# * `correct_show=` — the string with the correct value
# 
# The function should correct the names in the `'type'` column from the `df` table (i.e., replace each value from the `wrong_shows_list` list with the value in `correct_show`).

# In[16]:


# function for replacing implicit duplicates
def replace_wrong_show(df, wrong_shows_list, correct_show):
    for wrong_show in wrong_shows_list:
        df['type']= df['type'].replace(wrong_show, correct_show)
    return df
wrong_shows_list = ['shows', 'SHOW', 'tv show', 'tv shows', 'tv series', 'tv']
correct_show = 'SHOW'
df = replace_wrong_show(df, wrong_shows_list, correct_show)
print(df)


# Call `replace_wrong_show()` and pass it arguments so that it clears implicit duplicates and replaces them with `SHOW`:

# In[17]:


# removing implicit duplicates
def replace_wrong_movie(df, wrong_movies_list, correct_movie):
    for wrong_movie in wrong_movies_list:
        df['type']= df['type'].replace(wrong_movie, correct_movie)
    return df
wrong_movies_list = ['movies', 'the movie']
correct_movie = 'MOVIE'
df = replace_wrong_movie(df, wrong_movies_list, correct_movie)
print(df)


# Make sure the duplicate names are removed. Print the list of unique values from the `'type'` column:

# In[18]:


# viewing unique genre names
cleaned_names = df['name'].drop_duplicates()
uni_types = df['type']
sor_types = uni_types.unique()
print(sor_types)


# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Well done!
# </div>

# ### Conclusions <a id='data_preprocessing_conclusions'></a>
# We detected three issues with the data:
# 
# - Incorrect header styles
# - Missing values
# - Duplicate rows and implicit duplicates
# 
# The headers have been cleaned up to make processing the table simpler.
# 
# All rows with missing values have been removed. 
# 
# The absence of duplicates will make the results more precise and easier to understand.
# 
# Now we can move on to our analysis of the prepared data.

# ## Stage 3. Data analysis <a id='hypotheses'></a>

# Based on the previous project stages, you can now define how the assumption will be checked. Calculate the average amount of votes for each score (this data is available in the `imdb_score` and `imdb_votes` columns), and then check how these averages relate to each other. If the averages for shows with the highest scores are bigger than those for shows with lower scores, the assumption appears to be true.
# 
# Based on this, complete the following steps:
# 
# - Filter the dataframe to only include shows released in 1999 or later.
# - Group scores into buckets by rounding the values of the appropriate column (a set of 1-10 integers will help us make the outcome of our calculations more evident without damaging the quality of our research).
# - Identify outliers among scores based on their number of votes, and exclude scores with few votes.
# - Calculate the average votes for each score and check whether the assumption matches the results.

# To filter the dataframe and only include shows released in 1999 or later, you will take two steps. First, keep only titles published in 1999 or later in our dataframe. Then, filter the table to only contain shows (movies will be removed).

# In[19]:


# using conditional indexing modify df so it has only titles released after 1999 (with 1999 included)
# give the slice of dataframe new name
data_after = df['release_year']>= 1999
after_1999 = df[data_after]
after_1999_name = 'titles_released_after_1999'
print(after_1999)


# In[20]:


# repeat conditional indexing so df has only shows (movies are removed as result)
after_1999_shows = df[(df['type']=='SHOW')&(df['release_year']>=1999)]
print(after_1999_shows)


# <div class="alert alert-block alert-danger">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# <s>Something needs to be changed, but don't worry, you've got this.
#     
# We got empty dataframe because we do not have type "show", we have "SHOW".
#     
# Also, we need to work with after_1999_shows in next cells.
# </div>

# The scores that are to be grouped should be rounded. For instance, titles with scores like 7.8, 8.1, and 8.3 will all be placed in the same bucket with a score of 8.

# In[21]:


# rounding column with scores

#checking the outcome with tail()
after_1999_shows['new_score'] = df['imdb_score'].round()

print(after_1999_shows)


# It is now time to identify outliers based on the number of votes.

# In[22]:


# Use groupby() for scores and count all unique values in each group, print the result
unique_count = after_1999_shows.groupby('imdb_votes')['new_score'].nunique()
print(unique_count)


# Based on the aggregation performed, it is evident that scores 2 (24 voted shows), 3 (27 voted shows), and 10 (only 8 voted shows) are outliers. There isn't enough data for these scores for the average number of votes to be meaningful.

# To obtain the mean numbers of votes for the selected scores (we identified a range of 4-9 as acceptable), use conditional filtering and grouping.

# In[23]:


# filter dataframe using two conditions (scores to be in the range 4-9)
filtered_df = after_1999_shows[(after_1999_shows['new_score'] >= 4)&(after_1999_shows['new_score'] <=9)]

# group scores and corresponding average number of votes, reset index and print the result
final_df = filtered_df.groupby('new_score')['imdb_votes'].mean().reset_index()
print(final_df)


# Now for the final step! Round the column with the averages, rename both columns, and print the dataframe in descending order.

# In[24]:


# round column with averages
final_df['imdb_votes'] = final_df['imdb_votes'].round()

# rename columns
movies_shows = final_df.rename(columns={'new_score': 'scores', 'imdb_votes': 'avg_votes'})

# print dataframe in descending order

print(movies_shows.sort_values(by='scores', ascending=False))


# The assumption macthes the analysis: the shows with the top 3 scores have the most amounts of votes.

# <div class="alert alert-block alert-success">
# <b>Reviewer's comment</b> <a class="tocSkip"></a>
# 
# Excellent!
# </div>

# ## Conclusion <a id='hypotheses'></a>

# The research done confirms that highly-rated shows released during the "Golden Age" of television also have the most votes. While shows with score 4 have more votes than ones with scores 5 and 6, the top three (scores 7-9) have the largest number. The data studied represents around 94% of the original set, so we can be confident in our findings.

# <div class="alert alert-block alert-warning">
# <b>Overall reviewer's comment</b> <a class="tocSkip"></a>
# 
# Thank you so much for submitting your project!
# 
# I've found some tiny mistakes in your project. They'll be easy to fix. Please check my comments.
#     
# Every issue with our code is a chance for us to learn something new =)
# 
# </div>

# <div class="alert alert-block alert-warning">
# <b>Overall reviewer's comment v2</b> <a class="tocSkip"></a>
# 
# I'm happy to see you've made a few corrections to your work. 
# 
# However, Stage 3 still needs a bit of work. Please check my comments.
#     
# One more time and you'll have it!
# 
# </div>

# <div class="alert alert-block alert-success">
# <b>Overall reviewer's comment v3</b> <a class="tocSkip"></a>
# 
# Great improvement! 
# 
# I'm glad to say that your project has been accepted and you can go to the next sprint.
# 
# </div>

# In[ ]:




