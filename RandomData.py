import requests
import json
import string
import random
data = json.loads(open('namelist.json').read())
words = json.loads(open('words.json').read())

class RandomData:
    def create_profile_data(self):
        girl_or_boy = bool(random.getrandbits(1))
        lastName = random.choice(data['last_names'])
        if girl_or_boy == True:
            firstName = random.choice(data['boysFirst'])
            fullName = f"{firstName} {lastName}"
        else:
            firstName = random.choice(data['girlsFirst'])
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
            time = f"{hour}:{minute} PM"
        else:
            time = f"{hour}:{minute} AM"
        json = {
            "Time": time
        }
        return json 