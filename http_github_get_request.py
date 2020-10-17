import requests

# send http GET request and receive response
resp = requests.get(
    url="https://api.github.com/repos/Brillianttyagi/Python-script")

# unmarshal JSON
json_resp = resp.json()

name = json_resp["full_name"]
stars = json_resp["stargazers_count"]

# printing the number of stars
print("GitHub repository '%s' has %s stars." % (name, stars))
