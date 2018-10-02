"""
author: Nosova Olga
email: nosova-olenka@mail.ru

1. Serialize a datetime UTC object as JSON.
2. Deserialize JSON as a datetime object
"""
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import json


def serialize_datetime_utc(date: datetime):
    """
    Convert datetime in utf format to string
    Example: date : datetime.datetime(2014, 8, 24, 5, 57, 26, tzinfo=datetime.timezone(datetime.timedelta(0), 'UTC'))
            convert to : 'Sun, 24 Aug 2014 05:57:26 UTC'

            date : datetime.datetime(2014, 8, 24, 5, 57, 26, tzinfo=datetime.timezone(datetime.timedelta(0, 7200), 'UTC'))
            conver to: 'Sun, 24 Aug 2014 05:57:26 UTC+0200'
    :param date: datetime in utf format
    :return: date in str format
    """
    if not date.tzinfo:
        date = date.astimezone(timezone(timedelta(0, 0)))

    if date.tzinfo.utcoffset(date).seconds == 0:
        return date.strftime("%a, %d %b %Y %I:%M:%S %Z")
    else:
        return date.strftime("%a, %d %b %Y %I:%M:%S %Z%z")


def deserialize_datetime_utc(date: str):
    """
    Convert date string in utf format to datetime
    Example: string : 'Sun, 24 Aug 2014 05:57:26 UTC'
             convert to : datetime.datetime(2014, 8, 24, 5, 57, 26, tzinfo=datetime.timezone(datetime.timedelta(0), 'UTC'))

            date : 'Sun, 24 Aug 2014 05:57:26 UTC+0200'
            conver to: datetime.datetime(2014, 8, 24, 5, 57, 26, tzinfo=datetime.timezone(datetime.timedelta(0, 7200), 'UTC'))
    :param date: date string in utf format
    :return: date
    """
    try:
        date_dsrlz = datetime.strptime(date, '%a, %d %b %Y %I:%M:%S %Z').astimezone(timezone(timedelta(0, 0)))
    except Exception:
        try:
            date_dsrlz = datetime.strptime(date, '%a, %d %b %Y %I:%M:%S %Z%z')
        except Exception:
            print("Invalid format")
            return None

    return date_dsrlz


def serialize_datetime_utc_to_json(date: datetime, name: str):
    """
    Serialize a datetime UTC object as JSON.
    :param date: datetime in utf format
    :param name: name of date
    :return: json: {date:'',name:''}
    """
    srlz_date = serialize_datetime_utc(date)
    if srlz_date:
        return json.dumps({"date": srlz_date, "name": name})
    else:
        return None


def deserialize_datetime_utc_of_json(date_json: str):
    """
    Deserialize JSON as a datetime object
    :param date_json: json in format {date:'',name:''}
    :return: date,name
    """
    try:
        date_json=json.loads(date_json)
    except Exception:
        print("Incorrect format json")
        return None

    if 'date' in date_json and 'name' in date_json:
        dsrld_date=deserialize_datetime_utc(date_json['date'])
        if dsrld_date:
            return dsrld_date, date_json['name']
        else:
            return None
    else:
        print("Incorrect format json. Json must consist of 'name' and 'date'")
        return None


def test(str_json='{"date": "Sat, 1 Sep 2018 10:00:00 UTC", "name": "lolkek4eburek"}'):
    print("json string: ", str_json)
    date = deserialize_datetime_utc_of_json(str_json)
    print("Deserialize: ", date)
    if date:
        date = serialize_datetime_utc_to_json(date[0], date[1])
    else:
        date=None
    print("Serialize: ", date)

if __name__ == "__main__":
    print("Test")
    test()
    print("\n")
    test('{"date": "Sun, 24 Aug 2014 05:57:26 UTC+0200", "name": "LALA"}')

    str_json=input("\nInput json: ")
    test(str_json)
