import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
filepath ='C:/Users/Admin/Documents/testlab/pandas4E/code/projects/view_counts/fcc-forum-pageviews.csv'
df = pd.read_csv(filepath,parse_dates=['date'],index_col='date')

# Clean data
df = df[(df.value >= df.value.quantile(0.025))& (df.value <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    sns.lineplot(data=df,x='date',y='value',ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.set_figwidth(15)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year']= pd.DatetimeIndex(df_bar.date).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.date).month
    group_plot = df_bar.groupby(['month','year']).mean().reset_index()
    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # set month name
    group_plot['month']= pd.to_datetime(group_plot['month'],format='%m').dt.month_name()
    # Draw bar plot
    fig,ax = plt.subplots()
    sns.barplot(
    data = group_plot,
    x='year',
    y='value',
    hue='month',
    palette='viridis',
    errorbar=None,
    hue_order=Months,
    ax=ax
    )
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    #set months order
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig,(ax1,ax2) = plt.subplots(1,2)

    sns.boxplot(
    data = df_box,
    x='year',
    y='value',
    ax=ax1
    )
    sns.boxplot(
    data = df_box,
    x='month',
    y='value',
    order=Months,
    ax=ax2
    )
    
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Month')
    ax1.set_ylabel('Page Views')
    ax2.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    
    fig.set_figwidth(20)
    fig.tight_layout = True




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
