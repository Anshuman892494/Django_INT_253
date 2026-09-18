from decimal import Context
from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hey Anshu!</h1>")

# def about(request):
#     return HttpResponse("<h1>About Us Page</h1>")

# def contact(request):
#     return HttpResponse("<h1>Contact Us Page</h1>")

# def services(request):
#     return HttpResponse("<h1>Our Services Page</h1>")

# def result(request, marks=85):
#     if marks >= 80:
#         grade = "Excellent"
#     elif marks >= 60:
#         grade = "Good"
#     elif marks >= 40:
#         grade = "Average"
#     else:
#         grade = "Fail"
#     return HttpResponse(f"<h1>Marks: {marks}</h1><h2>Result: {grade}</h2>")


# def greet(request, name):
#     return HttpResponse(f"<h1>Hello, {name}</h1>")

# # Adding Items 
# def dictionary(request, item=None):
#     items = {
#         'Pizza':'Pizza cost Rs. 500/-',
#         'Burger':'Burger cost Rs. 50/-',
#         'Noodles':'Noodles cost Rs. 40/-',
#     }
    
#     # Format items using a for loop to create a bulleted list
#     formatted_items = "<ul>"
#     for key, value in items.items():
#         formatted_items += f"<li>{key}: {value}</li>"
#     formatted_items += "</ul>"
    
#     return HttpResponse(f"<h1>All Items:</h1><h2>{formatted_items}</h2>")

# # make dynamic items
# def dict(request, item):
#     items = {
#         'pizza': 'Pizza cost Rs. 500/-',
#         'burger': 'Burger cost Rs. 50/-',
#         'noodles': 'Noodles cost Rs. 40/-',
#     }
    
#     item_show = item
#     if item_show in items:
#         return HttpResponse(f"<h1>{items[item_show]}</h1>")
#     else:
#         return HttpResponse(f"<h1>Item '{item}' not found!</h1>")

# # Query Parameter Example
# # Access using request.GET.get('key', 'default_value')
# # Example URL: http://127.0.0.1:8000/profile/?name=John&age=21
# def profile(request):
#     name = request.GET.get('name', 'Guest')
#     age = request.GET.get('age', 'Not specified')
    
#     return HttpResponse(
#         f"<h1>User Profile (Query Parameters)</h1>"
#         f"<p><b>Name:</b> {name}</p>"
#         f"<p><b>Age:</b> {age}</p>"
#     )

# # Query Parameter Search Example
# # Example URL: http://127.0.0.1:8000/search/?item=pizza
# def search_item(request):
#     items = {
#         'pizza': 'Pizza cost Rs. 500/-',
#         'burger': 'Burger cost Rs. 50/-',
#         'noodles': 'Noodles cost Rs. 40/-',
#     }
#     query = request.GET.get('item', '').lower()
    
#     if query in items:
#         return HttpResponse(f"<h1>Search Result:</h1><p>{items[query]}</p>")
#     else:
#         return HttpResponse(f"<h1>Search Result:</h1><p>Item '{query}' not found in stock!</p>")


# # Regular Expression

# def user_profile(request, username):
#     return HttpResponse(
#         f"<h1>Welcome, {username}</h1>"
#     )

# def item_detail(request, item_id):
#     return HttpResponse(f"<h1>Item ID: {item_id}</h1>")


# # Giving two parameter in URL
# def restro_details(request, category, subcategory):
#     if not subcategory:
#         message = f"<h1>Showing all items in {category}</h1>"
#     else:
#         message = f"<h1>Showing {subcategory} in {category}</h1>"
#     return HttpResponse(message)



# ========================================================================================. 01/09/2026

# Django Templates

# def dash(request):
#     context = {
#         "name" : "Anshu"
#     }
#     return render(request, 'dash.html', context)


# def aboutus(request):
#     context = {
#         "name" : "Anshu",
#         "course": "B.Tech CSE",
#         "semester": 7,
#         "marks": 90.56
#     }
#     return render(request, 'aboutus.html', context)

# def filterdemo(request):
#     context = {
#         "sname" : "Anshu",
#         "surname" : "Verma",
#         "city": "Ballia",
#         "State": "Uttar Pradesh",
#         "class" : 12,
#         "subjects" : [
#             "Hindi",
#             "English",
#             "Maths",
#             "Science"
#         ]

#     }
#     return render(request,'filterDemo.html', context)


# # For Loop
# def menu_view(request):
#     menu = [
#         "Pizza",
#         "Burger",
#         "Pasta",
#         "Tea"
#     ]
#     context = {
#         "menu" : menu
#     }
#     return render(request, "menu.html", context)

# # def result(request):
# #     context = {
# #         "name" : "Anshu",
# #         "marks" : 85,
# #     }
# #     return render(request, "result.html", context)


# def extend_demo(request):
#     return render(request, "extend_demo.html")


# def students_profile(request):
#     students = [
#         {
#             "reg_no": "12015678",
#             "name": "anshu verma",
#             "email": "ANSHU.VERMA@LPU.IN",
#             "address": "ballia, uttar pradesh",
#             "year": 4,
#             "course": "b.tech cse",
#             "attendance": 88.5,
#             "marks": 92.4,
#             "status": "Active",
#         },
#         {
#             "reg_no": "12018942",
#             "name": "rahul sharma",
#             "email": "RAHUL.SHARMA@GMAIL.COM",
#             "address": "jalandhar, punjab",
#             "year": 3,
#             "course": "bca",
#             "attendance": 71.0,
#             "marks": 64.5,
#             "status": "Active",
#         },
#         {
#             "reg_no": "12014421",
#             "name": "priya singh",
#             "email": "PRIYA.SINGH@YAHOO.COM",
#             "address": "patna, bihar",
#             "year": 4,
#             "course": "b.tech it",
#             "attendance": 94.2,
#             "marks": 82.0,
#             "status": "Active",
#         },
#         {
#             "reg_no": "12019933",
#             "name": "amit kumar",
#             "email": "AMIT.KUMAR@OUTLOOK.COM",
#             "address": "delhi, ncr",
#             "year": 2,
#             "course": "b.tech cse",
#             "attendance": 68.4,
#             "marks": 38.0,
#             "status": "Inactive",
#         },
#         {
#             "reg_no": "12016654",
#             "name": "sneha patel",
#             "email": "SNEHA.PATEL@GMAIL.COM",
#             "address": "ahmedabad, gujarat",
#             "year": 3,
#             "course": "mca",
#             "attendance": 81.6,
#             "marks": 74.5,
#             "status": "Active",
#         },
#         {
#             "reg_no": "12019933",
#             "name": "amit kumar",
#             "email": "AMIT.KUMAR@OUTLOOK.COM",
#             "address": "delhi, ncr",
#             "year": 2,
#             "course": "b.tech cse",
#             "attendance": 68.4,
#             "marks": 38.0,
#             "status": "Inactive",
#         },
        
#     ]

#     context = {
#         "students": students,
#     }
#     return render(request, "students.html", context)

# # ================================= CA Question =================================

# def student_result(request):
#     roll = request.GET.get('roll')
#     semester = request.GET.get('semester')
    
#     return HttpResponse(f"<h1>Roll {roll} | Semester: {semester}</h1>")


# def student_profile(request, name):
#     return HttpResponse(f"<h1>Student Profile: {name}</h1>")


# def student_id(request, student_id):
#     return HttpResponse(f"<h1>Student ID: {student_id}</h1>")


# def student_id_reg(request, student_id_reg):
#     return HttpResponse(f"<h1>Student ID: {student_id_reg}</h1>")


# # ==================================================================

# def result(request):
#     context = {
#         "name" : "Anshu",
#         "marks" : 85,
#     }
#     return render(request, "result.html", context)


# ======================================================================== UNIT 4 - FORM

from django.middleware.csrf import get_token

def simple_form(request):
    token = get_token(request)
    if request.method == "POST":
        print("POST Data:", request.POST)
        name = request.POST.get('name')
        print("Name:", name)
        return HttpResponse(f"<h1>Hey {name} 😉</h1>")

    return HttpResponse(
    f"""
    <form action="" method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <br>
        <input type="submit" value="Submit">
    </form>
    """
    )


def stu_form(request):
    token = get_token(request)
    if request.method == "POST":
        print("POST Data:", request.POST)
        roll_no = request.POST.get('roll_no')
        name = request.POST.get('name')
        course = request.POST.get('course')
        marks = request.POST.get('marks')
        print("Roll No:", roll_no)
        print("Name:", name)
        print("Course:", course)
        print("Marks:", marks)  

        data = {
            "roll_no":roll_no,
            "name": name,
            "marks": marks,
            "course": course,
        }
        # return HttpResponse(f"""
        # <h1>Hey {name} 😉</h1>
        # <h2>Roll Number: {roll_no} </h2>
        # <h2>Course: {course} </h2>
        # <h2>Marks: {marks} </h2>
        # <a href="/stu_form">Go back</a>
        # """)
        return render(request, "stu_form.html", data)
    return render(request, 'stu_form.html')
