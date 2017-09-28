from .forms import ChooseReport
from .models import Reports,UserProfile,CityModel
from .Create_report import report
from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.decorators import login_required



@login_required(login_url='cleanapp/login')
def display(request):
    userid = request.user.id
    user = UserProfile.objects.get(user_id=userid)
    city_ref = CityModel.objects.get(userprofile=user)
    cid = city_ref.id
    if request.method == 'POST':
        form = ChooseReport(cid,Reports,request.POST)
        if form.is_valid():
            selected_date= form.cleaned_data['selected_date']
            basename = "report"
            filename = "_".join([basename, selected_date])
            cid = str(cid)
            filename="cleanapp/reports/"+cid+"_"+filename+".pdf"
            try:
                return FileResponse(open(filename, 'rb'), content_type='application/pdf')
            except FileNotFoundError:
                reportInstance = Reports.objects.get(pub_date=selected_date, city=city_ref.id)
                report(request,reportInstance.id)

    else:
        form = ChooseReport(cid,Reports)
    return render(request, 'cleanapp/display_report.html', {"form": form})




