#!/usr/bin/env python

"""
Ordr.in JavaScript Library Alpha
http://www.ordr.in

Copyright 2011
Last updated: Tuesday, July 7
"""

import urllib2, re, json, datetime

class Restaurant():
  def deliveryList(self, dT, addr):
    _apiRequest("r", "dl", dT.convertForRAPI(), addr.zip, addr.city, addr.street)
  def deliveryCheck(self, rID, dT, addr):
    _apiRequest("r", "dc", rID, dT.convertForRAPI(), addr.zip, addr.city, addr.street)
  def deliveryFee(self, rID, subtotal, tip, dT, addr):
    _apiRequest("r", "fee", rID, subtotal, tip, dT.convertForRAPI(), addr.zip, addr.city, addr.street)
  def details(self, rID):
    _apiRequest("r", "rd", rID)

def _apiRequest(api, request, *args):
  dataParams = []
  urlParams = []
  
  # seperate arguments into appropriate lists
  for i in args:
    i = str(i)
    if re.search("=", i):
      dataParams.append(i)
    else:
      urlParams.append(i)

  url = "http://nn2.deasil.com/" + request + "/" + "/".join(urlParams)
  print url + "\n"
  
  print urllib2.urlopen(url).read()
  # return json.loads(response.read())
  
class Address():
  def __init__(self, street, city, zip, street2="", state="", phone="", nick=""):
    self.nick = nick
    self.street = "+".join(street.split(" "))
    if street2 != "":
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
    self.amount = amount
  def convertForRAPI(self):
    if (re.match("/^\s*\d+\s*$/", amount)):
      Ordrin._errs.push("validation", "money")
    else:
      return int(self.amount) * 100
    
