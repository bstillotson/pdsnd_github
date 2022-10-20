import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
      city = input('Please select one of the following cities; chicago, new york city, or washington:').lower()
      if city not in CITY_DATA:
        print('Please select a city from the list.')
      else:
        break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("Please enter a month from january to june or select 'all'").lower()
      month_list = ['january','february','march','april','may','june']
      if month not in month_list and month != 'all':
        print('Please select a correct month')
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("Please enter a day of the week (Monday to Sunday) or 'all' to select all days.").lower()
      day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
      if day not in day_list and month != 'all':
        print('Please select a correct day')
      else:
        break

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

    #Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert Start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Pull out month and day of week from Start Time in new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month (if needed)
    if month != 'all':
        month_index = ['january','february','march','april','may','june']
        month = month_index.index(month) + 1

        #filter month for new dataframe
        df = df[df['month'] == month]

    #Filter day of week if needed
    if day != 'all':
        #filter by day of week for new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def display_raw_data(df):
    # """Displays 5 rows of data if user wants information, continue displaying 5 rows as user as user continues to ask for information, and finally stop when user says no or no more data available"""


    #https://www.geeksforgeeks.org/pandas-set_option-function-in-python/ used this to help understand pulling multiple lines and maxing rows
    i = 0
    data_request = input('Would you like to display 5 rows of data? yes/no:').lower()
    pd.set_option("display.max_columns",None)

    while True:
        if data_request == 'no':
            break
        elif data_request == 'yes':
            print(df[i:i+5])
            data_request = input('Would you like to display the next 5 rows of data? yes/no:').lower()
            i +=5
        else:
            data_request = input('Incorrect input, please select yes/no:').lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most common month is ', common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most common day is ', common_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour is ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station is ', common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print('Most common end station is ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    common_start_end_station = (df['Start Station'] + ', ' + df['End Station']).mode()[0]
    print('Most common start-end station combination is ', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel = df['Trip Duration'].sum()
    print('Total tavel time:', total_travel, ' seconds')

    # TO DO: display mean travel time

    mean_travel = df['Trip Duration'].mean()
    print('Average tavel time:', mean_travel, ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_user_types = df['User Type'].value_counts()
    print(count_user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_genders = df['Gender'].value_counts()
        print(count_genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest Birth Year is ', earliest_year)
        newest_year = int(df['Birth Year'].max())
        print('Newest Birth Year is ', newest_year)
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year is ', common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
