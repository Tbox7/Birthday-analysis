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


##################### sleep how many hours input display how many weeks you slep so far ##################################################
sleep_year = tyear-inpy
sleepin = float(input("How many hours do you sleep? "))
sleep_final = int(((sleepin*365)*sleep_year)/24)
##########################################################################################################################################
print("################################################")
print("################################################")
print("################################################")
print("################################################")
print("################################################")
print("<<<CALCULATIONS BASED OFF OF A 90 YEAR CALENDAR>>>")

################      ZODIAC SIGN     ##############################
if (inpm == 12 and inpd >= 22) or (inpm == 1 and inpd <= 19):
    print('Your zodiac sign is Capricorn')

elif(inpm == 1 and inpd >= 20) or (inpm == 2 and inpd <= 18):
    print('Your zodiac sign is Aquarius')

elif(inpm == 2 and inpd >= 19) or (inpm == 4 and inpd <= 20):
    print('Your zodiac sign is Pisces')

elif(inpm == 3 and inpd >= 21) or (inpm == 4 and inpd <= 19):
    print('Your zodiac sign is Aries')

elif(inpm == 4 and inpd >= 20) or (inpm == 5 and inpd <= 20):
    print('Your zodiac sign is Taurus')

elif(inpm == 5 and inpd >= 21) or (inpm == 6 and inpd <= 20):
    print('Your zodiac sign is Gemini')

elif(inpm == 6 and inpd >= 21) or (inpm == 7 and inpd <= 22):
    print('Your zodiac sign is Cancer')

elif(inpm == 7 and inpd >= 23) or (inpm == 8 and inpd <= 22):
    print('Your zodiac sign is Leo')

elif(inpm == 8 and inpd >= 23) or (inpm == 9 and inpd <= 22):
    print('Your zodiac sign is Virgo')

elif(inpm == 9 and inpd >= 23) or (inpm == 10 and inpd <= 22):
    print('Your zodiac sign is Libra')

elif(inpm == 10 and inpd >= 23) or (inpm == 11 and inpd <= 21):
    print('Your zodiac sign is Scorpio')

elif(inpm == 11 and inpd >= 22) or (inpm == 12 and inpd <= 21):
    print('Your zodiac sign is Sagittarius')

else: 
    print("Can't determine zodiac sign")
######################################################################

####################      Chinese Animal    ##########################

if inpy >= 2000:
   
    chtest = int(inpy - 2000)
    if chtest >= 12:
        for x in range(100):
            if chtest >= 12:
                chtest = chtest - 12   
        animals = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Oxen', 'Tiger', 'Rabbit']
    else:
        animals = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Oxen', 'Tiger', 'Rabbit']
else:
######### FOR YEARS BEFORE 2000 ################################################################################################
    chtest = abs(int( inpy - 2000))
    if chtest >= 12:
        for x in range(100):
            if chtest >= 12:
                chtest = chtest - 12   
        animals = ['Dragon', 'Rabbit', 'Tiger', 'Oxen', 'Rat', 'Pig', 'Dog', 'Rooster', 'Monkey', 'Sheep', 'Horse', 'Snake']
    else:
        animals = ['Dragon', 'Rabbit', 'Tiger', 'Oxen', 'Rat', 'Pig', 'Dog', 'Rooster', 'Monkey', 'Sheep', 'Horse', 'Snake']

# result
print(f"Your chinese animal is a {animals[chtest]}")
print(f"Have been sleeping for around {sleep_final} days of your life!!!")
print(f"You have roughly {days} day(s), {months} month(s), and {years} year(s) left.")
print("################################################")
print("################################################")
print("################################################")
print("################################################")
print("################################################")
