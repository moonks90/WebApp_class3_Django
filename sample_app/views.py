from django.shortcuts import render
import datetime
from sample_app import support_functions
from sample_app.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    data = dict()
    user = request.user
    if user.is_superuser:
        return render(request, "maintenance.html", context=data)
    import datetime
    date = 12#datetime.datetime.now()
    data['now'] = date
    print(data)
    return render(request,"home.html",context=data)


def show3divs(request):
    data = dict()
    return render(request,"html_divtag.html",context=data)

def showform(request):
    data = dict()
    return render(request, "html_test.html",context=data)

def formresults(request):
    data = dict()
    username = request.GET['name']
    date = request.GET['date']
    amount = float(request.GET['dollars'])
    commission = amount * 0.2
    returned_amount = amount - commission
    data['person'] = username
    data['selected_date'] = date
    data['amount'] = returned_amount
    print(username,date,amount)
    return render(request, "form_results.html",context=data)

def maintenance(request):
    data = dict()
    try:
        form_submitted = request.GET['form_submitted']
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_countries_and_currencies(support_functions.get_currency_list())
    except:
        pass
    return render(request,"maintenance.html",context=data)

#Make sure you’ve imported Country from models.py!
def currency_selection(request):
    data = dict()
    countries = Country.objects.all()
    data['countries'] = countries

    previous = "None"
    try:
        user = request.user
        if user.is_authenticated:
            account_holder = AccountHolder.objects.get(user=user)
            previous = account_holder.countries
    except:
        previous = "None"
        pass

    data['previous'] = previous

    return render(request, "country_selector.html", context=data)

def exch_rate(request):
    data = dict()
    try:
        country1 = request.GET['country_from']
        country2 = request.GET['country_to']
        data['country1'] = Country.objects.get(id=country1)
        data['country2'] = Country.objects.get(id=country2)

        try:
            user = request.user
            if user.is_authenticated:
                account_holder = AccountHolder.objects.get(user=user)
                account_holder.countries.add(country2)
                data['countries_visited'] = account_holder.countries.all()
        except:
            pass

        currency1 = Country.objects.get(id=country1).currency
        currency2 = Country.objects.get(id=country2).currency
        data['currency1'] = currency1
        data['currency2'] = currency2
        try:
            rate = currency1.rates_set.get(x_currency=currency2.symbol).rate
            data['rate'] = rate
        except:
            pass
    except:
        pass
    # test
    country_visited_list = list()
    try:
        if user.is_authenticated:
            account_holder = AccountHolder.objects.get(user=user)
        countries = account_holder.countries.all()
        for country in countries:
            lat, lon = support_functions.get_lat_lon(country.name)
        country_visited_list.append([country.name, lat, lon])
    except:
        pass
    data['countries_visited'] = country_visited_list

    return render(request, "exchange_detail.html", context=data)

def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user,date_of_birth=dob)
        acct_holder.save()
        return render(request,"entry.html",context=dict())
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context=context)

def entry(request):
    data = dict()

    return render(request, "entry.html", context=data)

# testing git
