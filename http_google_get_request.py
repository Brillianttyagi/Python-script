import requests

# send http GET request and receive response
r = requests.get(url="http://google.com")

# printing the output
print("Content:%s" % (r.content))
