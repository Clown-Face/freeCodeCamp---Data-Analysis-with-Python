import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,8))
    plt.scatter(x,y)


    # Create first line of best fit
    res1=linregress(x,y)
    m = res1.slope
    b = res1.intercept
    x1 = pd.Series(d for d in range(1880,2051))
    y1 = b + m*x1
    plt.plot(x1,y1,'r')


    # Create second line of best fit
    d1 = df[df['Year']>=2000]
    x_new  = d1['Year']
    y_new = d1['CSIRO Adjusted Sea Level']
    res2 = linregress(x_new,y_new)
    m1 = res2.slope
    b1 = res2.intercept
    x2 = pd.Series(d for d in range(2000,2051))
    plt.plot(x2, b1+m1*x2, 'g')


    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()