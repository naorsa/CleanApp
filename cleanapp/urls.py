from django.conf.urls import url
from . import views, Create_report,display_report
app_name = 'cleanapp'
urlpatterns = [
    url(r'^$', views.mainMenu, name='mainMenu'),
    url(r'^/questions/$', views.questions, name='questions'),
    url(r'^/(?P<reportid>[0-9]+)/report/$', Create_report.report, name='report'),
    url(r'^/login$', views.login_view, name='login'),
    url(r'^/logout$', views.logout_view, name='logout'),
    url(r'^/display_report$', display_report.display, name='display_report'),
    url(r'^/add_bill$', views.add_bill, name='add_bill'),
    url(r'^/display_bill$', views.display_bill, name='display_bill'),
    url(r'^/(?P<date>\d{4}-\d{2}-\d{2})/$', views.display_bill_name, name='display_bill_name'),
]

