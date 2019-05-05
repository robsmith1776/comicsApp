import requests
from bs4 import BeautifulSoup, SoupStrainer

# Config Stuff
weeks_info = ["info_0", "info_1", "info_2"]


def get_html():
    r = requests.get('http://thecomicstop.com/new-arrivals')
    whole_text = r.text
    info_tables = SoupStrainer(id=weeks_info)
    soup = BeautifulSoup(whole_text, 'html.parser')
    date_info = get_weeks(soup)
    smaller_soup = BeautifulSoup(soup.prettify(), 'html.parser', parse_only=info_tables)
    tables = smaller_soup.find_all('table', {"class": "nrGrid"})
    add_dates(tables, weeks_info, date_info)
    larger_list = parse_lists(tables)
    larger_list.sort()
    return larger_list


def get_weeks(soup_or_tag):
    # Expects Tab
    x = [(option['value'], option.text) for option in soup_or_tag.find_all('option')
         if option['value'][0:4] == "info"]
    return dict(x)


# Return Lists
def parse_lists(tables=""):
    # Expects BS4 ResultSet, Returns List
    title, cost, number, return_list = ([] for i in range(4))
    for table in tables:
        date_for_table = table.get('date') or "No Date"
        for row in table.find_all('tr'):
            find_title = row.find('td', {"class": "title"})
            find_cost = row.find('td', {"class": "srp"})
            find_number = row.find('td', {"class": "dmdNo"})
            if find_title:
                title = find_title.text.strip()
            if find_cost:
                cost = find_cost.text.strip()
            if find_number:
                number = find_number.text.strip()
            if find_title and find_cost and find_number and title != '':
                return_list.append([title, cost, number, date_for_table])
    return return_list


def add_dates(tables, weeks, dates):
    for table in tables:
        for tag in table.parents:
            if tag.get('id') in weeks:
                table['date'] = (dates[tag.get('id')])
    return tables
# Parse Results

# date_info = get_weeks(soup)
