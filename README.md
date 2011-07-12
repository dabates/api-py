Ordr.in Python API
======================

A Python wrapper for the Restaurant, User, and Order APIs provided by Ordr.in.

Usage
-----
	from src import *
	
	api.initialize("shds1d6c4BGDGs8", "http://localhost") # developer key and site where hosted
	
	place = Address("1 Main St", "College Station", "77840", "Suite 200", "Texas", "4044099661", "Home") # street, city, zip, street2, state, phone, nickname
	when = dTime.now()
	when.asap()
	
	subT = Money(100)
	tip = Money(15)
	
	r.deliveryList(when, place) # time, location
	r.def deliveryCheck("142", when, place) # subtotal, time, location
	r.deliveryFee("142", subT, tip, when, place) # restaurant ID, subtotal, tip, time, location
	r.details("142") # restaurant ID

	u.makeAcct("test@test.com", "pass", "John", "Doe")

	api.setCurrAcct("test@test.com", "pass") # user and pass required to be set before using rest of User API
	
	u.updateAddress(place) # sets address with such a nickname if it does not yet exists, updates it if otherwise
	u.getAddress("home") # returns details on address with given nickname
	src.u.deleteAddress("home") # deletes address with nickname
	
	u.updateCard("personal", "John Doe", "4111111111111111", "444", "02", "12", place) # sets card with such a nickname if it does not yet exists, updates it if otherwise
	u.getCard("personal") # returns details on card with given nickname
	u.deleteCard("personal") # deletes card with nickname
	
	u.orderHistory("12") # returns previous order; if no ID given, all previous orders listed
	
	u.updatePassword("newPassword") # sets new password
       
Notes
----- 
API docs available at http://www.ordr.in/developers/api.