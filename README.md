Ordr.in Python API
======================

A Python wrapper for the Restaurant, User, and Order APIs provided by Ordr.in.

Usage
-----
	from Ordrin import *
	
	place = Address("1 Main St", "College Station", "77840", "Suite 200", "Texas", "4044099661", "Home") # street, city, zip, street2, state, phone, nickname
	when = dTime.now()
	when.asap()
	
	subT = Money(100)
	tip = Money(15)
	
	r = Restaurant() # initializes Restaurant API
	r.deliveryList(when, place) # time, location
	r.def deliveryCheck("142", when, place) # subtotal, time, location
	r.deliveryFee("142", subT, tip, when, place) # restaurant ID, subtotal, tip, time, location
	r.details("142") # restaurant ID
       
Notes
----- 
API docs available at http://www.ordr.in/developers/api.