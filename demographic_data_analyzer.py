import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (bachelors_count/total_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    advanced_education_df = df[df['education'].isin(advanced_education)]
    advanced_education_count = len(df[df['education'].isin(advanced_education)])
    lower_education_df = df[~df['education'].isin(advanced_education)]
    lower_education_count = len(df[~df['education'].isin(advanced_education)])
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advanced_education_count
    lower_education = lower_education_count

    # percentage with salary >50K
    higher_education_rich = (len(advanced_education_df[advanced_education_df['salary'] == '>50K']) / advanced_education_count) * 100
    lower_education_rich = (len(lower_education_df[lower_education_df['salary'] == '>50K'])/lower_education_count) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_workers)
    num_min_workers_high_income = len(min_workers[min_workers['salary'] == '>50K'])

    rich_percentage = (num_min_workers_high_income/num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    total_people_per_country = df['native-country'].value_counts()
    high_income_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_high_income_per_country = (high_income_per_country / total_people_per_country) * 100
    country_with_highest_percentage = percentage_high_income_per_country.idxmax()
    
    highest_earning_country = country_with_highest_percentage
    highest_earning_country_percentage = percentage_high_income_per_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    top_IN_occupation = india_high_income['occupation'].mode().iloc[0]

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
        'race_count': round(race_count, 1),
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': round(min_work_hours, 1),
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
