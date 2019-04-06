import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june", "all"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]


def get_filters():
    """
  Asks user to specify a city, month, and day to analyze.

  Returns:
      (str) city - name of the city to analyze
      (str) month - name of the month to filter by, or "all" to apply no month filter
      (str) day - name of the day of week to filter by, or "all" to apply no day filter
  """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = " "
    while True:
        city = input(
            '\nWould you like to see bikeshare data for Chicago, New York City or Washington? \n>').lower()
        if city not in cities:
            print('\nWe do not have data for "{}".\nPlease choose from Chicago, New York City or Washington.'.format(city))
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    month = " "
    while True:
        month = input(
            '\nPlease indicate a month, from January to June, that you would like to filter the data by or enter all for all months: ').lower()
        if month not in months:
            print('\nWe do not have data for "{}".\nPlease choose a month from January to June or enter all.'.format(month))
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = " "
    while True:
        day = input(
            '\nPlease specify a day of the week that you would like to filter the data by or enter all for all days: ').lower()
        if day not in days:
            print('\nWe do not have data for "{}". \nPlease choose a different day or enter all.'.format(day))
            continue
        else:
            break

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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most Common Month: {}'.format(common_month))
    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('Most Common Day: {}'.format(common_day))
    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: {}'.format(common_start_station))
    print('Number of Times Start Station Used: {}\n'.format(
        df['Start Station'].value_counts()[common_start_station]))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: {}'.format(common_end_station))
    print('Number of Times End Station Used: {}\n'.format(
        df['End Station'].value_counts()[common_end_station]))

    # display most frequent combination of start station and end station trip
    total_trip = df['Start Station'] + ' - ' + df['End Station']
    most_frequent_stations = total_trip.mode()[0]
    print('Most Frequent Combination of Start & End Stations: {}'.format(most_frequent_stations))
    print('Number of Most Frequent Trips: {}'.format(
        total_trip.value_counts()[most_frequent_stations]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {}'.format(total_travel_time))
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time: {}'.format(average_travel_time))
    # display shortest travel time
    shortest_travel_time = df['Trip Duration'].min()
    print('Shortest Travel Time: {}'.format(shortest_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Number of User Types: \n{}\n'.format(user_types))
    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
    except KeyError:
        print('Gender information not avaliable. \nStatistics cannot be displayed.\n')
    else:
        print('Count of Gender Types: \n{}\n.'.format(gender_count))
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
    except KeyError:
        print('Birth information not available. \nStatistics cannot be displayed.\n')
    else:
        print('Earliest Birth Year: {}'.format(earliest_birth_year))
        print('Most Recent Birth Year: {}'.format(recent_birth_year))
        print('Most Common Birth Year: {}'.format(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_data(df):
    """Displays raw data for Bikeshare users."""
    user_data = input(
        'n\Would you like to see five lines of raw data? Enter Yes or No.\n').lower()
    if user_data == 'yes':
        print('\nPlease wait while we gather the raw data...\n')
        start_time = time.time()
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input(
                'n\Would you like to see an additional five lines of raw data. Enter Yes or No.\n').lower()
            if more_data != 'yes':
                break
            else:
                continue
                print("n\This took %s seconds." % (time.time() - start_time))
                print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        print('\nThank you for querying Bikeshare data. Have a great day!\n')


if __name__ == "__main__":
    main()
