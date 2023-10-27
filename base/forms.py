from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import *

class createcourseform(ModelForm):
    class Meta:
        model=course
        fields='__all__'


class createsubjectform(ModelForm):
    class Meta:
        model=subject
        fields='__all__'

class studentregistrationform(ModelForm):
    class Meta:
        model=student
        exclude=['user','qualifications']
class createclassform(ModelForm):
    class Meta:
        model=classes
        fields='__all__'

class StaffCreationForm(UserCreationForm):
    username = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    first_name=forms.CharField(max_length=20, required=True)
    last_name=forms.CharField(max_length=20, required=True)

    class Meta:
        model = staff
        fields = 'phone_number', 'position',  'password1', 'password2', 'username', 'staff_id'
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        data = self.cleaned_data
        user_data = {
            'username': data['username'],
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        if self.instance.pk:
            st=self.instance
            user=st.user
            for key,val in user_data.items():
                setattr(user, key, val)
        else:
            user = User(**user_data)
            user.set_password(data['password1'])
        user.save()

        staff_data = {
            'staff_id': data['staff_id'],
            'phone_number': data['phone_number'],
            'position': data['position'],
        }
        if self.instance.pk:
            st=self.instance
            obj = st
            for key,val in staff_data.items():
                setattr(st, key, val)
        else:
            obj = staff(**staff_data, user=user)
        obj.save()
        return obj


class studentcreationform(UserCreationForm):
    username=forms.CharField(required=True)
    email=forms.EmailField( required=False)
    first_name=forms.CharField( max_length=20, required=True)
    last_name=forms.CharField( max_length=20, required=True)
    
    class Meta:
        model=student
        fields=['address','phone_number','date_of_birth',  'password1', 'password2','enrollment_date','batch']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'flatpickr'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'flatpickr'}),
        }
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        data = self.cleaned_data
        user_data = {
            'username': data.get('username', None),
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
        if self.instance.pk:
            st = self.instance
            user = st.user
            for key,val in user_data.items():
                setattr(user, key, val)

        else:
            user = User(**user_data)
            user.set_password(data['password1'])
        user.save()

        student_data = {
            'phone_number': data['phone_number'],
            'address': data['address'],
            'date_of_birth': data['date_of_birth'],
            'enrollment_date': data['enrollment_date'],
            'batch': data['batch'],
            
        }
        if self.instance.pk:
            st=self.instance
            obj = st
            for key,val in student_data.items():
                setattr(st, key, val)
        else:
            obj = student(**student_data, user=user)
        obj.save()
        return obj


class StudentEditForm(studentcreationform):
    password1 = None
    password2 = None
    class Meta:
        model=student
        fields=['address','phone_number','date_of_birth','enrollment_date','batch']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'flatpickr'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'flatpickr'}),
        }

    def _post_clean(self):
        return super(ModelForm, self)._post_clean()


class roomform(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=["host","participants"]

class eventform(ModelForm):
    class Meta:
        model = event
        fields = '__all__'


class staffeditform(StaffCreationForm):
    password1 = None
    password2 = None
    class Meta:
        model=staff
        fields = 'phone_number', 'position', 'username', 'staff_id'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'flatpickr'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'flatpickr'}),
        }

    def _post_clean(self):
        return super(ModelForm, self)._post_clean()

