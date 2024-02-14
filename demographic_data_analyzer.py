import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_filt = df['sex']=='Male'

    average_age_men = round(df.loc[male_filt, 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.query('education == "Bachelors"').shape[0]/df.shape[0]*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high_edu = ['Bachelors', 'Masters', 'Doctorate']
    he_filt = df['education'].isin(high_edu)
    higher_education = df[he_filt]
    lower_education = df[~he_filt]

    # percentage with salary >50K
    higher_education_rich = round(df[he_filt].query('salary == ">50K"').shape[0]/higher_education.shape[0]*100,1)
    lower_education_rich = round(df[~he_filt].query('salary == ">50K"').shape[0]/lower_education.shape[0]*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hpw_filt = df['hours-per-week'] == 1
    rich_filt = df['salary'] == '>50K'

    num_min_workers = df[hpw_filt].shape[0]

    rich_percentage = round(df[hpw_filt&rich_filt].shape[0]/num_min_workers*100, 1)

    # What country has the highest percentage of people that earn >50K?

    total_people = df.value_counts('native-country')
    rich_people = df[rich_filt].value_counts('native-country')

    rich_share = pd.DataFrame(rich_people/total_people*100).sort_values('count', ascending=False)

    highest_earning_country = rich_share.index[0]
        
    highest_earning_country_percentage = round(rich_share.loc[highest_earning_country, 'count'],1)

    # Identify the most popular occupation for those who earn >50K in India.
    in_filt = df['native-country'] == 'India'

    top_IN_occupation = df[in_filt].value_counts('occupation').index[0]

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
