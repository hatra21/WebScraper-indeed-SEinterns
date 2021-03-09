from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.indeed.com/jobs?q=software+engineer+intern&l=Milwaukee%2C+WI').text
soup = BeautifulSoup(source, 'lxml')


# jobTitle = soup.find('h2', 'title').text.strip()
# company = soup.find('span', class_='company').text.strip()
# location = soup.find('span', class_='location accessible-contrast-color-location').text.strip()
# des = soup.find('div', class_='summary').text.strip()

# title = soup.find(name='a', attrs={'data-tn-element':'jobTitle'})['title'] 
# # print(title)

def get_jobTitle(soup):
    titles = []
    for div in soup.find_all('div', attrs={'class':'row'}):
        for a in div.find_all('a', attrs={'data-tn-element':'jobTitle'}):
            titles.append(a['title'])
    return titles

def get_company(soup):
    companies = []
    for name in soup.find_all('span', class_='company'):
        companies.append(name.text.strip())
    return companies

def get_location(soup):
    locations = []
    for location in soup.find_all('span', class_='location accessible-contrast-color-location'):
        locations.append(location.text.strip())

    return locations


def get_description(soup): 
  summaries = []
  for summary in soup.find_all('div', class_='summary'):
        summaries.append(summary.text.strip())
  return summaries

titles = get_jobTitle(soup)
companies = get_company(soup)
locations = get_location(soup)
descriptions = get_description(soup)


#start csv file and write data into its corresponded column        
csv_file = open('indeed-SE-interns.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Job Title', 'Company', 'Location', 'Job Summary'])

for i in range(len(get_jobTitle(soup))):
    csv_writer.writerow([titles[i], companies[i], locations[i], descriptions[i]])

csv_file.close()



