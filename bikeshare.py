import datetime
import pandas as pd
import numpy as np
import csv

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to see data from: Chicago, New York, or Washington?\n")
        if city in ['chicago','new york','washington']:
            break
        else:
            print('There is no data for this city\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month: January, February, March, April, May, June, or all?\n")
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print('There is no data for this month\n')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day of the week would you like to see? Please enter integer (0 = sunday, 7 = all)\n")
        if day in ['0','1','2','3','4','5','6','7']:
            break
        else:
            print('This is not a valid day\n')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'chicago':
        df =pd.read_csv('chicago.csv')
    elif city == 'new york':
        df =pd.read_csv('new_york_city.csv')
    elif city == 'washington':
        df =pd.read_csv('washington.csv')
    else:
        df= test

    #Load data into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Take month/day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name


    #Filter by month (if applicable)
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    #Filter by day (if applicable)
    if day != 'none':
        df = df[df['weekday'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = datetime.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print('The most common month is:', popular_month)

    # TO DO: display the most common day of week
    popular_weekday = df['weekday'].mode()
    print('The most common day of the week is:', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is:', popular_hour)

    print("\nThis took %s seconds." % (datetime.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = datetime.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()
    print('The most common start station is:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()
    print('The most common end station is:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = df.groupby['Start Station', 'End Station'].mode()
    print('The most popular combination of Start/End station is:', popular_combo)

    print("\nThis took %s seconds." % (datetime.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = datetime.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (datetime.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = datetime.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (datetime.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
