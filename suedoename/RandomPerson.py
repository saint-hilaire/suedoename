#!/usr/bin/env python3

import argparse
import random
import unicodedata
import string
import pkg_resources

class RandomPerson:
    def __init__(self, gender):
        self.gender = gender
        self.read_first_names()
        self.read_surnames()
        self.read_nicknames()

        self.webmail_forbidden_chars = {
                "gmail": ["-", "_"],
                "yahoo": ["-"],
                "outlook": [],
                "aol": ["-"],
                "zoho": [], # Not sure about this
                "gmx": [] # Provider not available
                }

    def read_first_names(self):
        self.first_names = []
        if self.gender == "":
            file_names = ["male", "female"]
        else:
            file_names = [self.gender]
        for fn in file_names:
            filepath = pkg_resources.resource_filename(__name__, fn+".txt")
            fp = open(filepath)
            names = fp.readlines()
            for i in range(len(names)):
                names[i] = names[i].strip()
            self.first_names += names
            fp.close()

    def read_surnames(self):
        self.surnames = []
        filepath = pkg_resources.resource_filename(__name__, "surnames.txt")
        fp = open(filepath)
        names = fp.readlines()
        for i in range(len(names)):
            names[i] = names[i].strip()
        self.surnames += names
        fp.close()
    def read_nicknames(self):
        self.nicknames = []
        filepath = pkg_resources.resource_filename(__name__, "nicknames.txt")
        fp = open(filepath)
        names = fp.readlines()
        for i in range(len(names)):
            names[i] = names[i].strip()
        self.nicknames += names
        fp.close()

    def random_first_name(self):
        num_of_first_names = len(self.first_names)
        rand_num = random.randint(0, num_of_first_names - 1)
        return self.first_names[rand_num]
    def random_last_name(self):
        num_of_last_names = len(self.surnames)
        rand_num = random.randint(0, num_of_last_names - 1)
        return self.surnames[rand_num]
    def random_full_name(self):
        return {"first": self.random_first_name(), "last": self.random_last_name()}

    def random_nickname(self):
        num_of_nicknames = len(self.nicknames)
        rand_num = random.randint(0, num_of_nicknames - 1)
        return self.nicknames[rand_num]

    def dash_or_underscore(self):
        rand_int = random.randint(0,1)
        if rand_int == 0:
            return "-"
        else:
            return "_"

    def make_name_email_safe(self, name, shorthand = False):
        if type(name) is dict:
            return self.make_name_email_safe(name['first'], bool(random.getrandbits(1)) ) \
                + "." + self.make_name_email_safe(name['last'])
        else:
            name = name.lower()
            name = name.replace(" ", self.dash_or_underscore() )
            name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode("utf-8") 
            if shorthand and len(name) > 0:
                return name[0]
            else:
                return name

    def make_random_email(self, name, webmail, tld="com", nickname="random", pretty=True):
        email = self.make_name_email_safe(name)
        if pretty:
            email = email + self.dash_or_underscore()
        email = email + self.rat_tail(nickname)
        email = email + "@" + webmail + "." + tld
        for forbidden_char in self.webmail_forbidden_chars[webmail]:
            email = email.replace(forbidden_char, "")
        return email
    
    def rat_tail(self, nickname="", size=10, chars=string.ascii_lowercase + string.digits ):

        if nickname == "random":
            size = 5
            nickname = self.random_nickname()
        nickname = self.make_name_email_safe(nickname)
        tail = nickname + self.dash_or_underscore()
        for _ in range(size):
            tail += random.choice(chars)
        #return nickname.join(random.choice(chars) for _ in range(size))
        return tail




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--female", action = "store_true")
    parser.add_argument("-m", "--male", action = "store_true")
    args = parser.parse_args()

    female = args.female
    male = args.male

    if female:
        gender_str = "female"
    elif male:
        gender_str = "male"
    else:
        gender_str = ""
    random_person = RandomPerson(gender_str)
    """
    for i in random_email.first_names:
        print(i)
    """
    random_name = random_person.random_full_name()
    first = random_name['first']
    last = random_name['last']

    print(first + " " + last)
    #print(random_person.make_name_email_safe(random_name) + "@gmail.com")
    webmails = ["gmail", "yahoo", "aol", "outlook", "gmx"]
    for webmail in webmails:
        print(random_person.make_random_email(random_name, webmail))

    #print(last)
