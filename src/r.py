import api

def deliveryList(dT, addr):
  api._request("GET", "dl", dT.convertForRAPI(), addr.zip, addr.city, addr.street)
def deliveryCheck(rID, dT, addr):
  api._request("GET", "dc", rID, dT.convertForRAPI(), addr.zip, addr.city, addr.street)
def deliveryFee(rID, subtotal, tip, dT, addr):
  api._request("GET", "fee", rID, subtotal.convertForRAPI(), tip.convertForRAPI(), dT.convertForRAPI(), addr.zip, addr.city, addr.street)
def details(rID):
  api._request("GET", "rd", rID)