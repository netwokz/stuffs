from datetime import datetime
from dateutil import relativedelta

# datetime in string format
born_braylen = '2022/10/19 04:50:00'
born_zander = '2017/01/29 04:50:00'
born_zoie = '2012/04/12 04:50:00'

born_taylor = '1994/07/15 04:50:00'
born_steve = '1984/12/15 04:50:00'

str_dt2 = datetime.now()

# convert string to datetime
dt_braylen = datetime.strptime(born_braylen, "%Y/%m/%d %H:%M:%S")
dt_zander = datetime.strptime(born_zander, "%Y/%m/%d %H:%M:%S")
dt_zoie = datetime.strptime(born_zoie, "%Y/%m/%d %H:%M:%S")
dt_taylor = datetime.strptime(born_taylor, "%Y/%m/%d %H:%M:%S")
dt_steve = datetime.strptime(born_steve, "%Y/%m/%d %H:%M:%S")

# difference between datetime in timedelta
# delta = str_dt2 - dt1
# print(f'Difference is {delta.seconds} seconds')
# print(f'Difference is {delta.days} days')
# print(f'Difference is {delta.days / 7} weeks')

def get_age(born_date):
    # Get the relativedelta between two dates
    delta2 = relativedelta.relativedelta(str_dt2, born_date)
    days = delta2.days
    if (delta2.days > 7):
        days -= (delta2.weeks * 7)
    print(delta2.years, 'Years,', delta2.months, 'months,', delta2.weeks, 'weeks,', days, 'days,', delta2.hours, 'hours,', delta2.minutes, 'minutes,', delta2.seconds, 'seconds')

print("\n")
print("Braylen")
get_age(dt_braylen)

print("\n")
print("Zander")
get_age(dt_zander)

print("\n")
print("Zoie")
get_age(dt_zoie)

print("\n")
print("Zoie")
get_age(dt_taylor)

print("\n")
print("Zoie")
get_age(dt_steve)
