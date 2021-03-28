from sample_app.models import *

def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("https://thefactfile.org/countries-currencies-symbols/")
    soup = BeautifulSoup(response.content, features="html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    for row in rows:
        details = row.find_all('td')
        try:
            country_name = details[1].get_text()
            currency_name = details[2].get_text()
            currency_symbol = details[3].get_text()
            if currency_name == "Currency":
                continue
            currency_list.append((country_name, currency_name, currency_symbol))
        except:
            continue

    return currency_list

def get_capitals():
    import pandas as pd
    print("start")
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_national_capitals")[1]
    df.set_index('Country/Territory', inplace=True)
    return df

def add_countries_and_currencies(currency_list):
    capitals_df = get_capitals()

    for currency in currency_list:
        country_name = currency[0]
        currency_name = currency[1]
        currency_symbol = currency[2]
        wiki_link = "https://en.wikipedia.org/wiki/"+country_name.replace(" ","_")

        try:
            capital_city = capitals_df.loc[country_name]['City/Town']
        except:
            capital_city = ""
            print("No capital for ", country_name)

        try:
            c = Currency.objects.get(symbol=currency_symbol)
        except:
            c = Currency(name=currency_name, symbol=currency_symbol)
        c.name = currency_name #the name might have been changed.
        c.save()

        try:
            print("Trying country stuff")
            cy = Country.objects.get(name=country_name)
            cy.name = country_name
            cy.wiki_link = wiki_link
            cy.capital = capital_city
            cy.currency = c
            print("Updating existing country object", cy)
        except:
            if len(capital_city) == 1:
                cy = Country(name=country_name, capital=capital_city, wiki_link=wiki_link, currency=c)
            else:
                cy = Country(name=country_name, capital=capital_city[0], wiki_link=wiki_link, currency=c)
            print("Creating new country object", cy)
        cy.save()
