import requests
import json
import string
import random
data = json.loads(open('namelist.json').read())

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
