from django.shortcuts import render
import datetime
from sample_app import support_functions

# Create your views here.
def home(request):
    data = dict()
    date = datetime.datetime.now()
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