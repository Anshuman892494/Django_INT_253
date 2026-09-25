from django import forms

class StudentForm(forms.Form):
    roll_no = forms.IntegerField(required=True, label="Roll Number")
    name = forms.CharField(max_length=100, required=True, label="Student Name")


class CourseEnrollmentForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    COURSE_CHOICES = [
        ('', '-- Select a Course --'),
        ('python', 'Python Full Stack'),
        ('django', 'Django Web Framework'),
        ('data_science', 'Data Science & AI'),
        ('java', 'Java Full Stack'),
        ('react', 'React Frontend Development'),
    ]

    HOBBY_CHOICES = [
        ('coding', 'Coding'),
        ('reading', 'Reading'),
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('traveling', 'Traveling'),
    ]

    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    age = forms.IntegerField(min_value=1, max_value=120, label="Age")
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label="Gender")
    course = forms.ChoiceField(choices=COURSE_CHOICES, widget=forms.Select, label="Course")
    hobbies = forms.MultipleChoiceField(choices=HOBBY_CHOICES, widget=forms.CheckboxSelectMultiple, required=False, label="Hobbies")
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False, label="About (Description)")

