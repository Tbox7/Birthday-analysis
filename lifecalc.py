#imports
from datetime import date

print("Welcome to Life Calculator")
print("Enter your Birth Month, Day, and Year. ")
#input 
inpm = int(input(" Month(00): "))
inpd = int(input(" Day(00): "))
inpy = int(input(" Year(0000): "))
#calculations
today = str(date.today())
    #remove "-" from date
today = today.replace("-","")
tyear = (today[0:4])
tmonth = (today[4:6])
tday = (today[6:8])
    #data type changed to int
today = int(today)
tyear = int(tyear)
tmonth = int(tmonth)
tday = int(tday)

if tmonth <= inpm:
    years = (inpy + 90) - tyear
    if tday <= inpd:
        months = abs(inpm - tmonth)
        days = abs(inpd - tday)
    else:
        months = abs((inpm - tmonth)-1)
        if (tmonth % 2) == 0:
            value = (30 - tday)
            days = (value + inpd)
        else:
            value = (31 - tday)
            days = (value + inpd)
else:
    years = (inpy + 89) - tyear
    if tday <= inpd:
        months = abs(inpm - tmonth)
        days = abs(inpd - tday)
    else:
        months = abs((inpm - tmonth)-1)
        if (tmonth % 2) == 0:
            value = (30 - tday)
            days = (value + inpd)
        else:
            value = (31 - tday)
            days = (value + inpd)


#leap year

#zodiac sign, chinese animal, etc


# result
print(f"You have roughly {days} days, {months} months, and {years} years left.")
print("<<<calculations based of 90 year calendar>>>")

