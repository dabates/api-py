"""
Ordr.in Python Library Alpha
http://www.ordr.in

Copyright 2011
Last updated: July 11
"""

import datetime, re, r, u

class Address():
  def __init__(self, street, city, zip, street2="", state="", phone="", nick=""):
    self.nick = nick
    self.street = "+".join(street.split(" "))
    self.street2 = "+".join(street2.split(" "))
    self.city = "+".join(city.split(" "))
    self.zip = zip
    self.state = state
    self.phone = phone
  def validate(self, element="all"):
    if element == "zip":
      re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip)
    elif element == "phone":
      re.match("(^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$)", self.phone)
    elif element == "city":
      re.match("[A-Za-z.-]", self.city)
    elif element == "state":
      re.match("^([A-Za-z]){2}$", self.state)
    else:
      re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip)
      re.match("^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$", self.phone)
      re.match("[A-Za-z.-]", self.city)
      re.match("^([A-Za-z]){2}$", self.state)
  def convertForRAPI(self):
    return self.zip + "/" + self.city + "/" + self.street;

class dTime(datetime.datetime):
  def asap(self):
    self.asap = 1
  def convertForRAPI(self):
    if self.asap == 1:
      return "ASAP"
    else:
      return self.month + "-" + self.day + "+" + self.hour + ":" + self.minute

class Money():
  def __init__(self, amount):
    self.amount = int(amount)
  def convertForRAPI(self):
    return self.amount * 100