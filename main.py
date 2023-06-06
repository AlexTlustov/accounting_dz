from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time

if __name__ == '__main__': 
    calculate_salary()
    get_employees()
    datetime_now = datetime.now()
    only_date = datetime_now.date()
    print(only_date)