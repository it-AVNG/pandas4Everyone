import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#preprocessed function
@np.vectorize
def check_health(value):
    if value > 25.0 :
        return 1
    else:
        return 0

@np.vectorize
def normalize(value):
    if value == 1:
        return 0
    else :
        return 1

def bmi_cal(height,weight):
    # convert from cm to meter
    height_meter = height/100
    bmi = weight / (height_meter**2)
    
    return bmi


# Import data
file_path = 'C:/Users/Admin/Documents/testlab/pandas4E/code/projects/visualizer/medical_examination.csv'
df = pd.read_csv(file_path)

# improve quality of life
df['height'] = df['height'].astype('float64')
bmi_serie = pd.Series(bmi_cal(height=df['height'],weight=df['weight']))
df['bmi_value'] = bmi_serie


# Add 'overweight' column
df['overweight']=check_health(df['bmi_value'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc']=df['gluc'].apply(normalize)
df['cholesterol'] = df['cholesterol'].apply(normalize)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(
            id_vars=['cardio','bmi_value'],
            var_name='variable',
            value_vars=['cholesterol','gluc','smoke','alco','active','overweight']
            )


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    res_df = df_cat.groupby(['variable','value','cardio']).count().reset_index()
    res_df = res_df.rename(columns={'bmi_value':'total'})
    
    
    # set the category for cat plot
    res_df.cardio=res_df.cardio.astype(str)
    res_df.value=res_df.value.astype(str)
    

    # Draw the catplot with 'sns.catplot()'
    plot =sns.catplot(
        data=res_df,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
        )
    # Get the figure for the output
    fig = plot.fig

    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_clean = (
                df[(df['ap_lo']<= df['ap_hi']) 
                    & (df['height'] >= df['height'].quantile(0.025))
                    & (df['height'] <= df['height'].quantile(0.975))
                    & (df['weight'] >= df['weight'].quantile(0.025))
                    & (df['weight'] <= df['weight'].quantile(0.975))
                    ]  
                .drop(columns=['bmi_value'])
                )

    # Calculate the correlation matrix
    corr = df_clean.corr()

    # Generate a mask for the upper triangle
    matrix = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    
    sns.heatmap(corr,
            mask=matrix,
            center=0.0,
            fmt=".1f",
            annot=corr,
            linewidth=.5,
            ax=ax,
            vmin=-0.25, vmax=0.25)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

