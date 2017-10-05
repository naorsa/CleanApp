from django import forms
from django.utils.safestring import mark_safe
from .models import CityModel, Question, BillImge, WeekArrangeMorning
from django.forms import ModelForm
from .widgets import AdminImageWidget
from multi_email_field.forms import MultiEmailField


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
      return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'))


class CloseAnsware(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        if self.instance.answare_type == True:
            self.fields['answare'] = forms.ChoiceField(choices=CHOICES ,widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
        else:
            self.fields['answare'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'הכנס תשובה','cols':10, 'rows':4}))
        self.fields['answare'].label = self.instance.question_text
    image = forms.ImageField(widget=AdminImageWidget(), label="")


    class Meta:
        model = Question
        fields = ('answare', 'image')


class CityForm(forms.Form):
    city_choice = forms.ModelChoiceField(queryset=CityModel.objects.all().order_by('id'),label='בחר עיר')


class UserForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())



class ChooseReport(forms.Form):
    def __init__(self,cid, Reports, *args, **kwargs):
        super(ChooseReport, self).__init__(*args, **kwargs)
        self.fields['selected_date'] = forms.ChoiceField(
            choices=[(report.pub_date, str(report.pub_date)) for report in Reports.objects.filter(city__id=cid)]
        )
        self.fields['selected_date'].label = ""


class UploadBill(ModelForm):
    name = forms.CharField(label="הכנס שם", required=True)
    image = forms.ImageField(widget=AdminImageWidget())
    notes = forms.CharField(label="הערות")

    class Meta:
        model = BillImge
        fields = ('name', 'image', 'notes')

class ChooseBill(forms.Form):
    def __init__(self, bills, *args, **kwargs):
        super(ChooseBill, self).__init__(*args, **kwargs)
        self.fields['selected_date'] = forms.ChoiceField(
            choices=[(bill.pub_date, str(bill.pub_date)) for bill in bills.objects.all()]
        )
        self.fields['selected_date'].label = ""


class ChooseBillName(forms.Form):
    def __init__(self,date, bills, *args, **kwargs):
        super(ChooseBillName, self).__init__(*args, **kwargs)
        self.fields['selected_name'] = forms.ChoiceField(
            choices=[(bill.name, str(bill.name)) for bill in bills.objects.filter(pub_date=date)]
        )
        self.fields['selected_name'].label = ""


class SendMessageForm(forms.Form):
    emails = MultiEmailField(label='נמענים')


class SidurAvudaFormMorning(ModelForm):
    day1m = forms.CharField(max_length=200)
    day2m = forms.CharField(max_length=200)
    day3m = forms.CharField(max_length=200)
    day4m = forms.CharField(max_length=200)
    day5m = forms.CharField(max_length=200)
    day6m = forms.CharField(max_length=200)
    day7m = forms.CharField(max_length=200)
    day1e = forms.CharField(max_length=200)
    day2e = forms.CharField(max_length=200)
    day3e = forms.CharField(max_length=200)
    day4e = forms.CharField(max_length=200)
    day5e = forms.CharField(max_length=200)
    day6e = forms.CharField(max_length=200)
    day7e = forms.CharField(max_length=200)

    class Meta:
        model = WeekArrangeMorning
        fields = ('day1m','day2m','day3m','day4m','day5m','day6m','day7m','day1e','day2e','day3e','day4e','day5e','day6e','day7e')

