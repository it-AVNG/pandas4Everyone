import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    file_path = 'C:/Users/Admin/Documents/testlab/pandas4E/code/projects/demographic_projects/adult_data.csv'
    df = pd.read_csv(file_path,na_values=['?','-','Null','None'])
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = (
        df['race'].reset_index()
        .groupby('race').count()
        .squeeze()
    )

    # What is the average age of men?
    men_age_df = df[df['sex'] == 'Male'][['age','sex']]

    average_age_men = round(men_age_df['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    total_pax = df['sex'].count()
    bac_num = (df[df['education'] == 'Bachelors']['sex'].count())
    
    percentage_bachelors = round((bac_num*100/total_pax),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_df= (df[
    df['education']
    .isin(['Bachelors','Masters','Doctorate'])
    ])
    lower_education_df = (df[
    ~df['education']
    .isin(['Bachelors','Masters','Doctorate'])
    ])
    
    w_highedu_over50k = higher_education_df[higher_education_df['salary']== '>50K'].sex.count()
    wo_highedu_over50k =lower_education_df[lower_education_df['salary']=='>50K'].sex.count()
    
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = None
    # lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(
        (w_highedu_over50k * 100 / higher_education_df.sex.count()),1
        )
    lower_education_rich = round(
        (wo_highedu_over50k*100 / lower_education_df.sex.count()),1
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # num_min_workers = None

    # rich_percentage = None
    num_min_workers = df[df['hours-per-week'] == 1].sex.count()
    rich_pax = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].sex.count()
    rich_percentage = rich_pax*100/num_min_workers    

    # What country has the highest percentage of people that earn >50K?
    # Country population
    people_by_country = (
        df.groupby('native-country')['salary'].count()
        .reset_index()
        .set_index('native-country')
        .rename(columns={'salary':'num_of_people'})
                        )
    # rich people
    rich_pax = (df[df['salary']=='>50K']
                .groupby('native-country')
                ['salary'].count()
                .reset_index()
                .set_index('native-country')
                .rename(columns={'salary':'rich_people'}))    
    # merge 2 above data frame
    people_earning = pd.merge(people_by_country,rich_pax,left_index=True, right_index=True)
    # calculate percentage
    people_earning['rich_percentage'] = people_earning['rich_people'] / people_earning['num_of_people']    
    
    
    highest_earning_country = people_earning.sort_values('rich_percentage',ascending=False).head(1).index[0]
    highest_earning_country_percentage = round((people_earning.loc[highest_earning_country].rich_percentage *100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_sorted = (df[(df['native-country']=='India') & (df['salary']=='>50K')]
                    .groupby('occupation').count()
                    ['salary'].reset_index()
                    .sort_values('salary',ascending=False))
    top_IN_occupation = india_sorted.iloc[0]['occupation']

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()
