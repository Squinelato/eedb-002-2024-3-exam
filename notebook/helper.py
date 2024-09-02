from datetime import datetime

import pandas as pd

seasons_dates = {
    'normal_year': {
        'autumn': {
            'starts_at': 80,
            'ends_at': 172
        },
        'winter': {
            'starts_at': 172,
            'ends_at': 266
        },
        'spring': {
            'starts_at': 266,
            'ends_at': 355
        }
    },
    'leap_year': {
        'autumn': {
            'starts_at': 81,
            'ends_at': 173
        },
        'winter': {
            'starts_at': 173,
            'ends_at': 267
        },
        'spring': {
            'starts_at': 267,
            'ends_at': 356
        }
    }
}

def get_season_as_number(date: datetime) -> int:
    """
    A function to determine the season of given a date, considering leap
    years. Besides, this function considers the southern hemisphere
    seasons. Finally, this function considers the day of the year insted
    of the absolute date in the format 'dd-MM-yyyy' for simplicity use.
    """
    is_leap_year = date.is_leap_year
    day_in_year = date.day_of_year
    season = 0

    seasons = seasons_dates['leap_year'] if is_leap_year else seasons_dates['normal_year']

    if seasons['autumn']['starts_at'] <= day_in_year < seasons['autumn']['ends_at']:
        season = 1
    elif seasons['winter']['starts_at'] <= day_in_year < seasons['winter']['ends_at']:
        season = 2
    elif seasons['spring']['starts_at'] <= day_in_year < seasons['spring']['ends_at']:
        season = 3
    else:
        season = 4

    return season

def get_season_as_string(date: datetime) -> str:
    """
    A function to determine the season of given a date, considering leap
    years. Besides, this function considers the southern hemisphere
    seasons. Finally, this function considers the day of the year insted
    of the absolute date in the format 'dd-MM-yyyy' for simplicity use.
    """
    is_leap_year = date.is_leap_year
    day_in_year = date.day_of_year
    season = ''

    seasons = seasons_dates['leap_year'] if is_leap_year else seasons_dates['normal_year']

    if seasons['autumn']['starts_at'] <= day_in_year < seasons['autumn']['ends_at']:
        season = 'Autumn'
    elif seasons['winter']['starts_at'] <= day_in_year < seasons['winter']['ends_at']:
        season = 'Winter'
    elif seasons['spring']['starts_at'] <= day_in_year < seasons['spring']['ends_at']:
        season = 'Spring'
    else:
        season = 'Summer'

    return season


def get_date_features(X: pd.DataFrame) -> pd.DataFrame:
    """
    A function to extract the day of week and the month of the year
    from a given date
    """
    X['day_of_week'] = X['date'].dt.day_of_week + 1
    X['week_of_month'] = X['date'].dt.day // 7 + 1
    X['month_of_year'] = X['date'].dt.month
    X['season'] = X['date'].apply(hp.get_season_as_number)
    X = X.drop(columns=['date'])
    
    return X