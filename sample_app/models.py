from django.db import models
from datetime import datetime,timezone,date
import requests
from bs4 import BeautifulSoup


# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=3)

    def __repr__(self):
        return self.name + " " + self.symbol

    def __str__(self):
        return self.name + " " + self.symbol


class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=50)
    wiki_link = models.URLField()
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)

    def has_valid_wiki_link(self):
        response = requests.get(self.wiki_link)
        soup = BeautifulSoup(response.content, features="html.parser")
        no_content = soup.find_all(class_="noarticletext")
        result = False if len(no_content) else True
        return result

    def __repr__(self):
        return self.name + ' ' + self.capital + ' ' + self.currency.name

    def __str__(self):
        return self.name + '' + self.capital + '' + self.currency.name


class Rates(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    x_currency = models.CharField(max_length=3)
    rate = models.FloatField(default=1.0)
    last_update_time = models.DateTimeField()

    def time_since_last_update(self):
        time_delta = datetime.now(timezone.utc) - self.last_update_time
        d = time_delta.days
        m, s = divmod(time_delta.seconds, 60)
        h, m = divmod(m, 60)
        result = (d, h, m, s)
        return result

    def __repr__(self):
        return self.currency.symbol + " " + self.x_currency + " " + str(self.rate)

    def __str__(self):
        return self.currency.symbol + " " + self.x_currency + " " + str(self.rate)

"""
#####Default class script#####
from sample_app.models import *
usd = Currency(name="United States Dollar",symbol="USD")
eur = Currency(name="European Euro",symbol="EUR")
jpy = Currency(name="Japanese Yen",symbol="JPY")
gbp = Currency(name="Great Britain Pound",symbol="GBP")

usd.save()
eur.save()
jpy.save()
gbp.save()

usa = Country(name="United States of America",capital="Washington D.C.",wiki_link="https://en.wikipedia.org/wiki/United_States",currency=usd)
japan = Country(name="Japan",capital="Tokyo",wiki_link="https://en.wikipedia.org/wiki/Japan",currency=jpy)
spain = Country(name="Spain",capital="Madrid",wiki_link="https://en.wikipedia.org/wiki/Spain",currency=eur)
italy = Country(name="Italy",capital="Rome",wiki_link="https://en.wikipedia.org/wiki/Italy",currency=eur)
britain = Country(name="United Kingdom of Great Britain and Northern Ireland",capital="London",wiki_link="https://en.wikipedia.org/wiki/United_Kingdom",currency=gbp)
japan.save()
spain.save()
italy.save()
britain.save()

from datetime import datetime,timezone
time_now = datetime.now(timezone.utc)
time_now

r1 = Rates(currency=usd, x_currency="EUR",rate=0.83, last_update_time=time_now)
r2 = Rates(currency=usd, x_currency="JPY",rate=105.07, last_update_time=time_now)
r3 = Rates(currency=eur, x_currency="JPY",rate=126.35, last_update_time=time_now)
r4 = Rates(currency=eur, x_currency="USD",rate=1.2, last_update_time=time_now)
r5 = Rates(currency=gbp,x_currency="USD",rate=1.37,last_update_time=time_now)
r1.save()
r2.save()
r3.save()
r4.save()
r5.save()


###### Question 1 Testing ######
testtime = datetime(2011, 1, 1, 0,0,0,tzinfo = timezone.utc)
r1.last_update_time = testtime
r1.time_since_last_update()

###### Question 2 Testing ######
usa.has_valid_wiki_link()
usa.wiki_link = "https://en.wikipedia.org/wiki/Brefsdsdgsgsf"
usa.has_valid_wiki_link()
"""

class Author(models.Model):
    name = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __repr__(self):
        return self.name + ' - ' + self.nationality

    def __str__(self):
        return self.name + ' - ' + self.nationality


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publisher = models.CharField(max_length=30)
    date = models.DateField()

    def __repr__(self):
        return self.title # + ' - ' + self.author.name + ' - ' + self.publisher

    def __str__(self):
        return self.title #+ ' - ' + self.author.name + ' - ' + self.publisher



'''
from sample_app.models import *

a1 = Author(name="Tolstoy", nationality="Russian", date_of_birth=date(1828, 9, 9))
a2 = Author(name="Anthony Doerr", nationality="American", date_of_birth=date(1973, 10, 27))
a3 = Author(name="Aalkdkl", nationality="English", date_of_birth=date(1945, 6, 5))
a4 = Author(name="Sslfjfa", nationality="Irish", date_of_birth=date(1987, 1, 3))
a5 = Author(name="Pafkjfank", nationality="Russian", date_of_birth=date(1647, 2, 19))
a1.save()
a2.save()
a3.save()
a4.save()
a5.save()

b1 = Book(title="Anna Karenina", author=a1, publisher="Little Brown & Company", date=date(1858, 9, 19))
b2 = Book(title="War and Peace", author=a1, publisher="", date=date(1868, 1, 9))
b3 = Book(title="All the light you cannot see", author=a2, publisher="Scribner", date=date(2014, 5, 6))
b4 = Book(title="Asjfkaskjnf", author=a3, publisher="Little Brown & Company", date=date(1967, 1, 1))
b5 = Book(title="Asjfkjs vaks", author=a4, publisher="Publisher X", date=date(1997, 1, 1))
b6 = Book(title="Asjfkdkjsfn fsdkf", author=a5, publisher="Little Brown & Company", date=date(1687, 1, 19))
b7 = Book(title="182jkslf sc saf", author=a4, publisher="Publisher Y", date=date(2001, 1, 19))
b1.save()
b2.save()
b3.save()
b4.save()
b5.save()
b6.save()
b7.save()
'''