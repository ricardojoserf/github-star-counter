import sys
import requests


def get_data(username, page, total_count):
	max_number_repos = 100
	url = "https://api.github.com/users/" + username + "/repos?per_page=" + str(max_number_repos) + "&page=" + str(page)
	response = requests.get(url)
	data = response.json()

	repo_counter = 0
	for repo in data:
		repo_counter += 1
		print ("| {:<50} | {:<50} |".format( repo["name"], str(repo["stargazers_count"]) ))
		total_count += repo["stargazers_count"]
	if repo_counter == 100:
		page+=1
		return get_data(username, page, total_count)
	return total_count


def main():
	username = sys.argv[1]

	aux = 107
	print("-"*aux)
	print ("| {:<50} | {:<50} |".format('Repository','Total stars'))
	print("-"*aux)

	page = 1
	total_count = 0
	total_count = get_data(username, page, total_count)
	print ("| {:<50} | {:<50} |".format( "", "" ))
	print ("| [+] Total count: "+ str(total_count))
	print ("-"*aux)


if __name__ == "__main__":
    main()
