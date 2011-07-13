"""
Ordr.in Python Library Alpha
http://www.ordr.in

Copyright 2011
Last updated: July 11
"""

import datetime, re, r, u, api

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
    if element == "zip" and not re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip):
      api._errs.append(("validation - address", "zipcode"))
    elif element == "phone" and self.phone and not re.match("(^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$)", self.phone):
      api._errs.append(("validation - address", "phone"))
    elif element == "city" and not re.match("[A-Za-z.-]", self.city):
      api._errs.append(("validation - address", "city"))
    elif element == "state" and self.state and not re.match("^([A-Za-z]){2}$", self.state):
      api._errs.append(("validation - address", "state"))
    else:
      if not re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip):
        api._errs.append(("validation - address", "zip"))
      if self.phone and not re.match("^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$", self.phone):
        api._errs.append(("validation - address", "phone"))
      if not re.match("[A-Za-z.-]", self.city):
        api._errs.append(("validation - address", "city"))
      if self.state and not re.match("^([A-Za-z]){2}$", self.state):
        api._errs.append(("validation - address", "state"))
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
    if not amount.isdigit():
      api._errs.append(("validation", "money must be numerical"))
    else:
      self.amount = amount
  def convertForRAPI(self):
    return self.amount * 100