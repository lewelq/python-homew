import date_check as dtc

date_month_year = str(input())
dmy_splitted = date_month_year.split(".")

date = int(dmy_splitted[0])
month = dmy_splitted[1]
year = int(dmy_splitted[2])

print(f"{date}.{month}.{year} - {dtc.DMY(date, month, year)}")