from django.shortcuts import render
from .models import CityModel, Question, Title, Reports,UserProfile,BillImge
from .forms import CloseAnsware, UserForm,UploadBill, ChooseBill, ChooseBillName
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.core.urlresolvers import reverse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'cleanapp/base.html')
        else:
            raise Http404("Wrong user or password")
    else:
        form = UserForm()
    return render(request, 'cleanapp/login.html',{"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('cleanapp:login'))

@login_required(login_url='cleanapp/login')
def mainMenu(request):
    return render(request,'cleanapp/base.html',{"request":request})


@login_required
def questions(request):
    title = Title.objects.order_by('id')
    FormSet = modelformset_factory(Question, form=CloseAnsware)
    questionFormSet = FormSet()
    userid = request.user.id
    user=UserProfile.objects.get(user_id=userid)
    city_ref=CityModel.objects.get(userprofile=user)
    if request.method == 'POST':
        if Reports.objects.filter(pub_date=date.today(),city__id=city_ref.id)!=None:
            Reports.objects.filter(pub_date=date.today(), city__id=city_ref.id).delete()
        report = Reports(city=city_ref)
        report.save()
        questionFormSet = FormSet(request.POST, request.FILES)
        if questionFormSet.is_valid():
            ans_list = []
            image_list = []
            for form in questionFormSet[:-1]:
                ans = form.cleaned_data['answare']
                ans_list.append(ans)
                image = form.cleaned_data['image']
                image_list.append(image)
                questionFormSet.save()
            count = 0
            question = Question.objects.all()
            qansdict = {}
            imagesdict = {}
            for q in question:
                qid = str(q.id)
                img = str(q.image)
                qansdict[qid] = ans_list[count]
                imagesdict[qid] = img
                count=count+1
            qanstring = json.dumps(qansdict)
            imagestring = json.dumps(imagesdict)
            reportid = report.id
            report.questions_answers = qanstring
            report.questions_images = imagestring
            report.save()
            clean_question()
            return HttpResponseRedirect(reverse('cleanapp:report', args=[reportid]))
    context = {'questionFormSet': questionFormSet, 'title': title }
    return render(request, 'cleanapp/print.html', context)

@login_required
def add_bill(request):
    if request.method == 'POST':
        form = UploadBill(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = UploadBill()
    return render(request, 'cleanapp/add_bill.html', {"form": form})


def clean_question():
    questions = Question.objects.all()
    for q in questions:
        q.image = 'uploads/No_image_3x4.svg.png'
        q.answare = ''
        q.save()
    return

@login_required(login_url='cleanapp/login')
def display_bill(request):
    if request.method == 'POST':
        form = ChooseBill(BillImge,request.POST)
        if form.is_valid():
            date=form.cleaned_data['selected_date']
            return HttpResponseRedirect(reverse('cleanapp:display_bill_name', args=[date]))

    else:
        form = ChooseBill(BillImge)
    return render(request, 'cleanapp/display_bill.html', {"form": form})


def display_bill_name(request, date):
    if request.method == 'POST':
        form = ChooseBillName(date,BillImge,request.POST)
        if form.is_valid():
            selected_name=form.cleaned_data['selected_name']
            bills = BillImge.objects.filter(name=selected_name,pub_date=date)
            for bill in bills:
                path = bill.image
            image_data = open(str(path), "rb").read()
            return HttpResponse(image_data, content_type="image/png")


    else:
        form = ChooseBillName(date,BillImge)
    return render(request, 'cleanapp/display_bill.html', {"form": form})
