# Task - 1
#
# Introduction
# The objective for this task is straightforward, 
# you're expected to fix the issue present in the following script 
# and get the changes into the main branch.
#
# You are expected to follow the following steps roughly
#   1. Get the following code up and running in your system.
#   2. Debug the code and get the desired result.
#   3. Commit & Push your changes and raise a Pull Request.
#
# Resources
# Here are some resources to get you up and running
#   1. https://realpython.com/python-requests/
#   2. https://swapi.dev/

# Setting Up
import requests
import json

import logging
logging.basicConfig(
  level=logging.DEBUG, 
  format='%(asctime)s - %(levelname)s - %(message)s'
)

# To disable SSL Certificate Errors
import urllib3
urllib3.disable_warnings()


# Section 1
# The objective of this section is to fetch the people from the 
# Star Wars API and have all the people in one list 
# ready for analysis.

page_no = 1
people = []

while True:
  url = f"https://swapi.dev/api/people/?page={page_no}&format=json"
  logging.info(f"GET {url}")

  response = requests.get(url, verify=False)
  result = json.loads(response.content)

  list_of_people = result["results"]
  people.extend(list_of_people)
  logging.info(f"Fetched {len(list_of_people)} people")

  page_no += 1

  if result["next"] == None:
    break


# Section 2
# The objective of this section is to compute the average height 
# of all the fetched charecters from the Star Wars API.

sum_height = 0
num_height = 0

for person in people:
  try:

    sum_height += int(person["height"])
    num_height += 1

  except ValueError:
    # logging.error(f'{person["name"]} ({person["url"]}) does not have a mentioned height.')
    pass

print(sum_height / num_height, "cm")