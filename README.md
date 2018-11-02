n_APMC

The problem statement for the given task is as follows:

Challenge 1: Agriculture Commodities, Prices & Seasons
Aim: Your team is working on building a variety of insight packs to measure key trends in the
Agriculture sector in India. You are presented with a data set around Agriculture and your aim is
to understand trends in APMC (Agricultural produce market committee)/mandi price & quantity
arrival data for different commodities in Maharashtra.
Objective:
1. Test and filter outliers.
2. Understand price fluctuations accounting the seasonal effect
1. Detect seasonality type (multiplicative or additive) for each cluster of APMC and
commodities
2. De-seasonalise prices for each commodity and APMC according to the detected
seasonality type
3. Compare prices in APMC/Mandi with MSP(Minimum Support Price)- raw and
deseasonalised
4. Flag set of APMC/mandis and commodities with highest price fluctuation across different
commodities in each relevant season, and year.


I am listing the things I have learned during this task and the difficulties, I
faced.

Things Learned:
1) Firstly, I learned git and github from udacity course( Their teaching is quite
comprehensible). Many people will say just read the basic commands and then use it, but I 
think otherwise.
While, using git the many subtleties of git diff, git diff --staged, etc, should be known,
how commits are traversed in different branches they should be known. But, yeah it took 
time.

2) Outlier detection: I knew about some methods of determining outliers like calculating 
interquartile range and removing values outside Q1 - 1.5 * IQR and Q3 + 1.5 * IQR, boxplots,etc.
Those are parametric methods they work when the distribution is normal, or it can be transformed
to normal,also here the distribution was filled with prices of different crops, so as such 
these parametric methods couldn't be applied. Discovered new methods such as z-score(similar
parametric method). Tried linear regression, think it can work. There are others also,
density based distance based.

3)Time Series Analysis: I didn't know any timeseries analysis before this task, so this 
task helped me to acquire some knowledge on timeseries analysis. I even figured it 
out late on Sunday(28th October) that it was time series, from seasonality stuff.
Learned alot from scipy ,pydata conferences , stats.exchange, machinelearningmastery.com,
cross validated, medium and many others.


Difficulties faced : 
1) While using git, if you want to see the differences between commits or between staging
area and working directory ( or staging area and commits), jupyter notebook display is 
annoying hard to understand, since both cell outputs and json(html whatever) format is 
loaded.
2) Outlier detection was a pretty difficult thing for me , because of lesser experience.
3) Time series concepts need time to understand and implement.

Still I tried hard enough
