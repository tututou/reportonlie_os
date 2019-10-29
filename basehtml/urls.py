from django.urls import path,re_path
from basehtml import views
from django.views.generic.base import RedirectView
# from django.conf.urls.static import static, settings
from django.views.static import serve
from reportonline_os.settings import MEDIA_B27_ROOT


urlpatterns = [
    path('login_page/', views.login_page,),
    path('login_action/',views.login_authentication,),
    path('upload_index/', views.upload_index, name='upload_index'),
    path('query_page/', views.query_page, name='query_page'),
    path('query_index/', views.query_index, name='query_index'),
    path('upload/<project_name>', views.upload_project_html, name='upload_project_html'),
    path('upload/<project_name>/action', views.upload_project_html_action_v2, name='upload_project_html_action_v2'),
    path('rpchart/TH/<patient_name>', views.patient_TH_report_echart, name='patient_TH_report_echart'),
    
    path('manage_project_query/<project_name>', views.manage_project_query, name='manage_project_query'),
    path('manage_date_query/<the_time>', views.manage_date_query, name='manage_date_query'),
    path('manage_query_index/', views.manage_query_index, name='manage_query'),
    path('logout/', views.logout_authentication),
    
    re_path('delete/(?P<project_name>.+)/(?P<patient_name>.+)/(?P<RPmtime>.+)/', views.drop_mysql, name='drop_mysql'),
    re_path('media/B27/(?P<path>.*)/', serve, {"document_root":MEDIA_B27_ROOT}),
    re_path('B27/(?P<patient_name>.+)/(?P<RPmtime>.+)/', views.patient_B27_report, name='B27/patient/RPmtime'),
    re_path('TH/(?P<patient_name>.+)/(?P<RPmtime>.+)/', views.patient_TH_report, name='TH/patient/RPmtime'),



    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),

]
