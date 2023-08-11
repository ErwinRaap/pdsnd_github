import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
<<<<<<< HEAD
    Asks user to specify a city, month, and day to analyze and filter the data.
||||||| parent of 673aa32 (Updating function documentation)
    Asks user to specify a city, month, and day to analyze.
=======
	No inputs are needed. Results are used for other functions.
	
    Asks user to specify a city, month, and day to analyze.
>>>>>>> 673aa32 (Updating function documentation)

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        city = input("Would you like to see data for Chicago, New York City or Washington?: ").lower()
        if city not in CITY_DATA:
            print("That's not an available city. Please try again")

    month = ''
    while month not in ['january', 'february', 'march', 'april', 'may', 'june'] and month != "all":
        month = input("Which month would you like to filter by?(Type 'january' etc or 'all' if no filter): ").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june'] and month != "all":
            print("That's not a month. Please try again")

    day = ''
    while day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] and day != "all":
        day = input("Which day would you like to filter by?(Type 'Monday' etc or 'all' if no filter): ").lower()
        if day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] and day != "all":
            print("That's not a day. Please try again")



    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
	Inputs for this function are the result of the get_filter() function.
	
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_number = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    common_month = months[int(common_month_number)-1] 
    print('The most common travel month is', common_month.title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    
    print("The most common travel day of the week is",common_day_of_week)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    
    print("The most common travelling hour is {}h".format(common_hour))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts()
    most_start_station = start_station.index[0]
    print("The most common starting station is",most_start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts()
    most_end_station = end_station.index[0]
    print("The most common ending station is",most_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combined_stations'] = df['Start Station'] + ' to ' + df['End Station']
    combined_station = df['combined_stations'].value_counts()
    most_combined_station = combined_station.index[0]
    print("The most common trip is",most_combined_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_day = total_travel_time // 86400
    total_travel_time_hour = total_travel_time % 86400 // 3600
    total_travel_time_minutes = (total_travel_time - total_travel_time_day * 86400 - total_travel_time_hour * 3600) // 60
    total_travel_time_seconds = (total_travel_time - total_travel_time_day * 86400 - total_travel_time_hour * 3600 -                 total_travel_time_minutes*60)

    print("The total travel time is {} days, {} hours, {} minutes and {} seconds!".format(int(total_travel_time_day),int(total_travel_time_hour),int(total_travel_time_minutes),int(total_travel_time_seconds)))
    # TO DO: display mean travel time
	""" avg in this code means the average"""
    avg_travel_time = df['Trip Duration'].mean()
    avg_travel_time_day = avg_travel_time // 86400
    avg_travel_time_hour = avg_travel_time % 86400 // 3600
    avg_travel_time_minutes = (avg_travel_time - avg_travel_time_day * 86400 - avg_travel_time_hour * 3600) // 60
    avg_travel_time_seconds = (avg_travel_time - avg_travel_time_day * 86400 - avg_travel_time_hour * 3600 - avg_travel_time_minutes*60)
    
    print("The average travel time is {} minutes and {} seconds!".format(int(avg_travel_time_minutes),int(avg_travel_time_seconds)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("There are {} subscribers and {} customers".format(user_type[0],user_type[1]))

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print("There are {} males and {} females".format(gender_count[0],gender_count[1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    oldest = int(df['Birth Year'].min())
    print("The oldest person is {} years old".format(2023-oldest))

    youngest = int(df['Birth Year'].max())
    print("The youngest person is {} years old".format(2023-youngest))

    common = int(df['Birth Year'].mode())
    print("The most common age is {}".format(2023-common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats_WA(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("There are {} subscribers and {} customers".format(user_type[0],user_type[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Displays raw data."""

    print('\nDisplaying raw data...\n')
    start_time = time.time()
    raw_data_sample = df[["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year"]]
    row_nums = raw_data_sample.shape[0]
    
    raw_data = ''
    #in order to not display the same rows over and over I use upper and lower bounds as indices for row number
    lower_bound = 1
    upper_bound = 6
    while raw_data not in ['yes','no']:
        raw_data = input("Would you like to see (more) raw input?(Type 'yes' or 'no'): ").lower()
        if raw_data not in ['yes','no']:
            print("That's not a yes or no answer, please try again")
        elif raw_data == 'yes' and upper_bound != row_nums:
            print(raw_data_sample[lower_bound:upper_bound])
            lower_bound += 5
            upper_bound += 5
            raw_data = ''
        elif raw_data == 'no':
            break    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_WA(df):
    """Displays raw data."""

    print('\nDisplaying raw data...\n')
    start_time = time.time()
    raw_data_sample = df[["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type"]]
    row_nums = raw_data_sample.shape[0]
    
    raw_data = ''
    #in order to not display the same rows over and over I use upper and lower bounds as indices for row number
    lower_bound = 1
    upper_bound = 6
    while raw_data not in ['yes','no']:
        raw_data = input("Would you like to see (more) raw input?(Type 'yes' or 'no'): ").lower()
        if raw_data not in ['yes','no']:
            print("That's not a yes or no answer, please try again")
        elif raw_data == 'yes' and upper_bound != row_nums:
            print(raw_data_sample[lower_bound:upper_bound])
            lower_bound += 5
            upper_bound += 5
            raw_data = ''
        elif raw_data == 'no':
            break    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'washington':
            user_stats_WA(df)
        else:
            user_stats(df)
        if city == 'washington':
            raw_data_WA(df)
        else:
            raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
