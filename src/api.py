import urllib2, re, json, hashlib

_key = ""
_url = ""

_currEmail = ""
_currPass = ""

def initialize(key, url):
  global _key, _url
  _key = key
  _url = url
  
def setCurrAcct(currEmail, currPass):
  global _currEmail, _currPass
  _currEmail = currEmail
  _currPass = hashlib.sha256(currPass).hexdigest()

def _request(type, *args):
  dataParams = []
  urlParams = []
  
  # seperate arguments into appropriate lists
  for i in args:
    i = str(i)
    if re.search("=", i):
      dataParams.append(i)
    else: 
      if i == "uN": # this is to prevent the header for the user API going out with the makeAcct function
        iN = "u"
        urlParams.append(iN)
      else:
        urlParams.append(i)

  append = "/" + "/".join(urlParams)
  print "URL: " + _url
  print "append: " + append
  
  opener = urllib2.build_opener(urllib2.HTTPHandler)
  request = urllib2.Request(_url + append, "&".join(dataParams))
  request.add_header('X-NAAMA-CLIENT-AUTHENTICATION', 'id="' + _key + '", version="1"')
  request.add_header("Content-Type", "application/x-www-form-urlencoded");
  
  if args[0] == "u":
    print "Hash is being created."
    hash = hashlib.sha256(_currPass + _currEmail + append).hexdigest()
    print "hash: " + hash
    request.add_header("X-NAAMA-AUTHENTICATION", 'username="' + _currEmail + '", response="' + hash + '", version="1"')
    print "header looks like: " + 'username="' + _currEmail + '", response="' + hash + '", version="1"'
  
  request.get_method = lambda: type
  call = opener.open(request)
  
  print call.read()
  # return json.loads(response.read())