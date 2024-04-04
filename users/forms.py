
from .models import User
from django import forms

class RegisterForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['password_confirm']=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','photo', 'phone_number']


    def clean_password_confirm(self):
        password=self.cleaned_data['password']
        password_confirm=self.cleaned_data['password_confirm']

        if password!=password_confirm:
            raise forms.ValidationError('Parolni tekshiring va bir xil kiriting')
        
        return password
    
    def clean_username(self):
        username=self.cleaned_data['username']

        if len(username)<4 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan katta 30 dan kichik bolishi kerakl')
        return username
    
    def clean_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number)!=13 or not phone_number.startswith('+998'):
             raise forms.ValidationError('Mobile raqam kiritishda xatolik')
 




class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username=self.cleaned_data['username']
        if not isinstance(username,str):
            raise forms.ValidationError('usernameni stringda kiriting')
        if len(username)<5 or len(username)>30:
            raise forms.ValidationError('username uzunligi 5 dan katta 30 dan kichik bolishi kerakl')
        return username
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if not password.isdigit():
            raise forms.ValidationError('passwordni raqamda kiriting ')
        return password
    
class ProfileUpdateview(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','photo', 'phone_number']


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    

    def clean(self):
        new_password = self.cleaned_data['new_password']
        confirm_password = self.cleaned_data=['confirm_password']

        if new_password !=confirm_password:
            raise forms.ValidationError(" Nimadur Xato ketdi qaytadan urining!")
        
        return self.cleaned_data
    
