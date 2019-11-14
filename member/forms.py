from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import University,Profile

# settings 에 설정된 파일임. ACCOUNT_SIGNUP_FORM_CLASS = 'member(앱이름).forms.SignupForm' #회원가입 폼 클래스를 지정

class SignupForm(forms.Form):
    first_name = forms.CharField(label=_('First name'),
                                 max_length=30,
                                 widget=forms.TextInput(
                                     attrs={'placeholder':
                                                _('First name'), }))
    last_name = forms.CharField(label=_('Last name'),
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs={'placeholder':
                                               _('Last name'), }))

    university = forms.ModelChoiceField(queryset=University.objects.all(), empty_label="--학교 선택--") # 100 개가 넘는 항목에는 사용하지 않아야합니다
                                           
    student_num = forms.CharField(label=_('학번'),
                            max_length=40,
                            widget=forms.TextInput(
                                attrs={'placeholder':
                                           _('Student number'), }))


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Profile()
        profile.user = user
        profile.university = self.cleaned_data['university']
        profile.student_num = self.cleaned_data['student_num']        
        user.profile.save()