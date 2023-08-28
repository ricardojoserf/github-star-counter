import sys
import requests

username = sys.argv[1]
max_number_repos = 1000

url = "https://api.github.com/users/" + username + "/repos?per_page=" + str(max_number_repos)
response = requests.get(url)
data = response.json()

total_count = 0
aux = 107
print("-"*aux)
print ("| {:<50} | {:<50} |".format('Repository','Total stars'))
print("-"*aux)
for repo in data:
	print ("| {:<50} | {:<50} |".format( repo["name"], str(repo["stargazers_count"]) ))
	total_count += repo["stargazers_count"]
print("-"*aux)

print("\n[+] Total count: "+ str(total_count))
