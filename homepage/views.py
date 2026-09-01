from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Homepage!</h1>")

def about(request):
    return HttpResponse("<h1>About Us Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us Page</h1>")

def services(request):
    return HttpResponse("<h1>Our Services Page</h1>")

def result(request, marks=85):
    if marks >= 80:
        grade = "Excellent"
    elif marks >= 60:
        grade = "Good"
    elif marks >= 40:
        grade = "Average"
    else:
        grade = "Fail"
    return HttpResponse(f"<h1>Marks: {marks}</h1><h2>Result: {grade}</h2>")


def greet(request, name):
    return HttpResponse(f"<h1>Hello, {name}</h1>")

# Adding Items 
def dictionary(request, item=None):
    items = {
        'Pizza':'Pizza cost Rs. 500/-',
        'Burger':'Burger cost Rs. 50/-',
        'Noodles':'Noodles cost Rs. 40/-',
    }
    
    # Format items using a for loop to create a bulleted list
    formatted_items = "<ul>"
    for key, value in items.items():
        formatted_items += f"<li>{key}: {value}</li>"
    formatted_items += "</ul>"
    
    return HttpResponse(f"<h1>All Items:</h1><h2>{formatted_items}</h2>")

# make dynamic items
def dict(request, item):
    items = {
        'pizza': 'Pizza cost Rs. 500/-',
        'burger': 'Burger cost Rs. 50/-',
        'noodles': 'Noodles cost Rs. 40/-',
    }
    
    item_show = item
    if item_show in items:
        return HttpResponse(f"<h1>{items[item_show]}</h1>")
    else:
        return HttpResponse(f"<h1>Item '{item}' not found!</h1>")

# Query Parameter Example
# Access using request.GET.get('key', 'default_value')
# Example URL: http://127.0.0.1:8000/profile/?name=John&age=21
def profile(request):
    name = request.GET.get('name', 'Guest')
    age = request.GET.get('age', 'Not specified')
    
    return HttpResponse(
        f"<h1>User Profile (Query Parameters)</h1>"
        f"<p><b>Name:</b> {name}</p>"
        f"<p><b>Age:</b> {age}</p>"
    )

# Query Parameter Search Example
# Example URL: http://127.0.0.1:8000/search/?item=pizza
def search_item(request):
    items = {
        'pizza': 'Pizza cost Rs. 500/-',
        'burger': 'Burger cost Rs. 50/-',
        'noodles': 'Noodles cost Rs. 40/-',
    }
    query = request.GET.get('item', '').lower()
    
    if query in items:
        return HttpResponse(f"<h1>Search Result:</h1><p>{items[query]}</p>")
    else:
        return HttpResponse(f"<h1>Search Result:</h1><p>Item '{query}' not found in stock!</p>")


# Regular Expression

def user_profile(request, username):
    return HttpResponse(
        f"<h1>Welcome, {username}</h1>"
    )

def item_detail(request, item_id):
    return HttpResponse(f"<h1>Item ID: {item_id}</h1>")


# Giving two parameter in URL
def restro_details(request, category, subcategory):
    if not subcategory:
        message = f"<h1>Showing all items in {category}</h1>"
    else:
        message = f"<h1>Showing {subcategory} in {category}</h1>"
    return HttpResponse(message)



# ========================================================================================. 01/09/2026

# Django Templates

def dash(request):
    context = {
        "name" : "Anshu"
    }
    return render(request, 'dash.html', context)


def aboutus(request):
    context = {
        "name" : "Anshu",
        "course": "B.Tech CSE",
        "semester": 7,
        "marks": 90.56
    }
    return render(request, 'aboutus.html', context)

def filterdemo(request):
    context = {
        "sname" : "Anshu",
        "surname" : "Verma",
        "city": "Ballia",
        "State": "Uttar Pradesh",
        "class" : 12,
        "subjects" : [
            "Hindi",
            "English",
            "Maths",
            "Science"
        ]

    }
    return render(request,'filterDemo.html', context)