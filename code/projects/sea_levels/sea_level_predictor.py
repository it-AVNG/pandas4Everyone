import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    filepath = './epa-sea-level.csv'
    df = pd.read_csv(filepath)
    
    
    # Create scatter plot
    fig2= plt.figure()
    ax2 = fig2.add_subplot()
    years = df['Year']
    sealvl = df['CSIRO Adjusted Sea Level']
    ax2.scatter(years,sealvl,marker='o',label='Observed Data') 
    
    
    # Create first line of best fit
    res1 = linregress(years,sealvl)
    # Create second line of best fit
    recent_subset = df[df['Year']>1999]
    recent_year = recent_subset['Year']
    recent_sealevel = recent_subset['CSIRO Adjusted Sea Level']
    res2 = linregress(recent_year,recent_sealevel)
    
    
    # add new years
    beyond_year = np.array(range(2000, 2051))
    additional_year = np.array(range(2014,2051))
    years = pd.concat([years,pd.Series(additional_year)])
    
    # plot lines
    ax2.plot(years,res1.intercept + res1.slope*years,label='Best Fit (All Data)')
    ax2.plot(beyond_year,res2.intercept + res2.slope*beyond_year,label='Best Fit (recent Data)')
    
    
    # Add labels and title
    ax2.set_title("Rise in Sea Level")
    ax2.set_xlabel('Year')
    ax2.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()