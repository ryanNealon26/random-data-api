import json
import string
import random

name_list = json.loads(open('namelist.json').read())
words = json.loads(open('words.json').read())
street_names = json.loads(open('address.json').read())

class RandomData:
    def create_profile_data(self):
        girl_or_boy = bool(random.getrandbits(1))
        lastName = random.choice(name_list['last_names'])
        if girl_or_boy == True:
            firstName = random.choice(name_list['boysFirst'])
            fullName = f"{firstName} {lastName}"
        else:
            firstName = random.choice(name_list['girlsFirst'])
            fullName = f"{firstName} {lastName}"
        email = f"{firstName[0].lower()}{lastName.lower()}@gmail.com"
        return [fullName, email]

    def generate_password(self, passwordLength):
        password = ""
        special_char_list = ['&', '$', '%', '!', '@', '?']
        for x in range(passwordLength):
            rand_int = random.randint(0, 9)
            # if 0 or 1 is generate the password gains an integer
            if rand_int== 0 or rand_int == 1:
                password = password + str(random.randint(0, 9))
            # if 2 is generated the password gains a random special character
            elif rand_int == 2:
                special_char = random.choice(special_char_list)
                password = password + special_char
            #else the password gains a random letter
            else:
                randomLetter = random.choice(string.ascii_letters)
                password = password + randomLetter
        return password
    def profile_json(self):
        name_and_email = self.create_profile_data()
        password = self.generate_password(15)
        user_data = {
            "Name": name_and_email[0],
            "Email": name_and_email[1],
            "Password": password
        }
        return user_data

    def generate_rand_date(self):
        month =  str(random.randrange(1, 13))
        year = 2024
        month_list = {
            '1': "January",
            '2': "February",
            '3': "March",
            '4': "April",
            '5': "May", 
            '6': "June",
            '7': "July",
            '8': "August",
            '9': "September",
            '10': "October",
            '11': "November",
            '12': "December"
        }
        if month == '9' or month == '4' or month=='7' or month=='11':
            day = str(random.randrange(1, 31))
        elif month == '2':
            if year%4==0:
                day = str(random.randrange(1, 30))
            else:
                day = str(random.randrange(1, 30))
        else:
            day = str(random.randrange(1, 32))
        json = {
            "Month": month,
            "formatted_date": f"{month_list[month]} {day}, {year}",
            "unformatted_date": f"{month}/{day}/{year}"
        }
        return json
    #Generated Random text in lorem lipsum style
    def generate_random_text(self, wordCount):
        text = ""
        #limits max count at 300
        if wordCount > 300:
            text = "Word Count limit is 300"
        else:
            for x in range(wordCount):
                word = random.choice(words['words'])
                text = text + word + " "
        json = {
            "text": text
        }
        return json
    def generate_time_of_day(self):
        hour = str(random.randrange(1, 13))
        minute = str(random .randrange(1, 61))
        if int(minute) < 10:
            minute = "0"+minute 
        pm_or_am = random.getrandbits(1)
        if pm_or_am:
            fake_time = f"{hour}:{minute} PM"
        else:
            fake_time = f"{hour}:{minute} AM"
        json = {
            "Random Time": fake_time,
        }
        return json 
    def generate_phone_number(self):
        counter = 0
        phonenumber = ""
        for x in range(9):
            number = str(random.randrange(1, 10))
            phonenumber = phonenumber + number
            counter+=1
            if counter % 3 == 0 and counter !=9:
                phonenumber = phonenumber + '-'
        json = {
            "Phone Number": phonenumber
        }
        return json
    def generate_temperature(self, season):
        if season== 'Winter':
            temp = random.randrange(0, 37)
        if season == 'Spring':
            temp = random.randrange(38, 70)
        if season == 'Summer':
            temp = random.randrange(70, 100)
        if season == 'Fall':
            temp = random.randrange(40, 60)
        return temp
    def generate_weather_condition(self, temperature):
        rand_int = random.randint(0, 3)
        match rand_int:
            case 0:
                condition = 'Mostly Cloudy'
            case 1:
                condition = 'Mostly Sunny'
            case 2:
                if temperature < 32:
                    chance_hail = random.randint(0, 4)
                    if chance_hail == 4:
                        condition = 'Hail'
                    elif chance_hail == 3:
                        condition = 'Heavy Snow'
                    elif chance_hail == 2:
                        condition = 'Light Snow'
                    else:
                        condition = 'Chance of Snow'
                else:
                    chance_rain = random.randint(0, 3)
                    if chance_rain == 3:
                        condition = 'Heavy Rain'
                    elif chance_rain == 3 and temperature > 90:
                        condition = 'Thunderstorms'
                    elif chance_rain == 2:
                        condition = 'Light Rain'
                    else:
                        condition = 'Chance of Rain'
            case 3:
                windspeed = random.randint(0, 24)
                if windspeed < 4:
                    condition = 'Calm Winds'
                elif windspeed in range(5, 8):
                    condition = 'Light Winds'
                elif windspeed in range(9, 18):
                    condition = 'Moderate Winds'
                else:
                    condition = 'Heavy Winds'
        return condition

    def random_weather(self):      
        date_data = self.generate_rand_date()
        month = int(date_data["Month"])
        if month in [12, 1, 2]:
            season = "Winter"
        if month in [3, 4, 5]:
            season = "Spring"
        if month in [6, 7, 8]:
            season = "Summer"
        if month in [9, 10, 11]:
            season = "Fall"
        temperature =self.generate_temperature(season)
        json = {
            "Date": date_data["formatted_date"],
            "Season": season,
            "Temperature": f"{temperature}º Fahrenheit",
            "Weather Condtion": self.generate_weather_condition(temperature)
        }
        return json
    def generate_fake_address(self):
        street_name = random.choice(street_names['street_names'])
        street_closure = random.choice(street_names['finish'])
        number = random.randrange(1, 350)
        state = random.choice(street_names['states'])
        address = f"{number} {street_name} {street_closure}"
        json = {
            "Address": address,
            "State": state,
            "Abbreviaton": state[0:2].upper()
        }
        return json