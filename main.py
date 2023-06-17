import pandas
import requests

# getting data from open api
response_api = requests.get('http://universities.hipolabs.com/search?country=United+States')
universities_data = response_api.json()

# creating and manipulating DataFrame from received data
universities_df = pandas.DataFrame(universities_data)
universities_df.drop(columns=['state-province'], inplace=True)
universities_df.rename(columns={
    'country': 'COUNTRY', 'alpha_two_code': 'ALPHA TWO CODE',
    'name': 'UNIVERSITY NAME', 'domains': 'DOMAINS', 'web_pages': 'WEB-PAGE'}, inplace=True)

# saving manipulated data in CSV file
universities_df.to_csv("university_list.csv", index=False)
