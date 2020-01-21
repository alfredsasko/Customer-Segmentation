# Identify Consumer Segments

Do you want to increase revenue and marketing ROI using customer segmentation? If yes, this is the project for you.

### Table of Contents
1. [Project Motivation](#motivation)
2. [Results](#results)
4. [Installation](#installation)
3. [File Descriptions](#files)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Project Motivation<a name="motivation"></a>

In this project, you will apply unsupervised learning techniques to identify segments of the population that form the core customer base for a mail-order sales company in Germany. These segments can then be used to direct marketing campaigns towards audiences that will have the highest expected rate of returns. 

The purpose of this project is to share with fellow sales, marketing professionals and data scientists how to approach customer segmentation to answer questions as:
 1. How many consumer segments are in whole market population?
 2. Which ones of these consumer segments represents our customer base?
 
 From a data science perspective it means:
 1. How to use principal component analysis to reduce dimensionality of consumer characterstics?
 2. How to use non-hierarchical clustering to decide to form and decide number of consumer segments?
 2. How to profile those consumer segments on existing customer base to improve targetting?
 
## Results<a name="results"></a>

The main findings of the code can be found at the notebook available [here](https://github.com/alfredsasko/Customer-Segmentation/blob/master/Indetify_Customer_Segments.ipynb).

## Installation <a name="installation"></a>

There are several necessary 3rd party libraries beyond the Anaconda distribution of Python which needs to be installed and imported to run code. These are:
 - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for parsing consumer characterstics definitions
 - [StatsModels](https://www.statsmodels.org/stable/index.html) to enable optimal sample size calculations for hypothesis testing
 - [rpy2](https://rpy2.readthedocs.io/en/latest/) to enable R functionalities to impute missing data
 - [tqdm](https://tqdm.github.io/) for displaying progress bar in time-consuming code fractions
 
## File Descriptions <a name="files"></a>

There is 1 notebook available here to showcase work related to the above questions.  Markdown cells were used to assist in walking through the thought process for individual steps.  

There are additional files:
 - `bigquery_.py` module supporting 
 
## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Google for the data.  @alexisbcook for a nice introduction to [Nested and Repeated Data](https://www.kaggle.com/alexisbcook/nested-and-repeated-data). Daqing Chen, Sai Laing Sain & Kun Guo for their technical article [Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining](https://link.springer.com/article/10.1057/dbm.2012.17).

