# from django.shortcuts import render
import os
# from doc2mysql.doc2docx import beginswith
from django.shortcuts import HttpResponse
from doc2mysql.docx2mysql import patient_B27_extract,patient_TH_extract

import datetime
from basehtml.forms import QueryForm,LoginForm,Manage_department_query,Manage_project_query,Manage_time_query
from doc2mysql.models import patient_TH,patient_B27
from django.db.models import Q
from django.template import RequestContext, loader
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from reportonline_os.settings import THEURL

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
upload_file_wait_for_extract = []





def get_the_th_patient_report(patient_name,RPmtime):
    try:
        RPmtime = datetime.datetime.strptime(RPmtime, '%Y-%m-%d-%H-%M-%S-%f')
        patient_obj = patient_TH.objects.get(patient_name=patient_name,RPmtime= RPmtime)

        print('已找到确定患者报告')
        # patient_imageurl = imgurl_jion('B27',patient_obj.patient_imageurl)
        patient_IL2 =float(patient_obj.patient_IL2)
        patient_IL4 =float(patient_obj.patient_IL4)
        patient_IL6 =float(patient_obj.patient_IL6)
        patient_IL10 =float(patient_obj.patient_IL10)
        patient_TNF =float(patient_obj.patient_TNF)
        patient_IFN =float(patient_obj.patient_IFN)
        echart_href = THEURL+"rpchart/" + 'TH' + '/' + patient_name
        patient_report = {
            #报告抬头
            'patient_name': patient_obj.patient_name,
            'patient_ID': patient_obj.patient_ID,
            'patient_sex': patient_obj.patient_sex,
            'patient_department': patient_obj.patient_department,
            'patient_age': patient_obj.patient_age,
            'submit_doctor_name': patient_obj.submit_doctor_name,
            # 2
            'patient_IL2' : patient_IL2,
            'patient_IL4' : patient_IL4,
            'patient_IL6' : patient_IL6,
            'patient_IL10' : patient_IL10,
            'patient_TNF' : patient_TNF,
            'patient_IFN' : patient_IFN,
            # 3
            'RPmtime': patient_obj.RPmtime,
            'Submit_Sample_time': patient_obj.Submit_Sample_time,
            'Detection_time': patient_obj.Detection_time,
            'Inspection_person': patient_obj.Inspection_person,
            'Report_Doctor': patient_obj.Report_Doctor,
            # 4
            'echart_href':echart_href
        }
        return patient_report
    except Exception as e:
        return HttpResponse(e)

def get_the_b27_patient_report(patient_name,RPmtime):
    try:
        RPmtime = datetime.datetime.strptime(RPmtime, '%Y-%m-%d-%H-%M-%S-%f')
        patient_obj = patient_B27.objects.get(patient_name=patient_name, RPmtime=RPmtime)
        patient_imageurl = imgurl_jion('B27', patient_obj.patient_imageurl)
        patient_report = {
            # 报告抬头
            'patient_name': patient_obj.patient_name,
            'patient_ID': patient_obj.patient_ID,
            'patient_sex': patient_obj.patient_sex,
            'patient_department': patient_obj.patient_department,
            'patient_age': patient_obj.patient_age,
            'submit_doctor_name': patient_obj.submit_doctor_name,
            # 2
            'patient_result': patient_obj.patient_result,
            'patient_imageurl': patient_imageurl,
            'report_opinion': patient_obj.report_opinion,
            # 3
            'RPmtime': patient_obj.RPmtime,
            'Submit_Sample_time': patient_obj.Submit_Sample_time,
            'Detection_time': patient_obj.Detection_time,
            'Inspection_person': patient_obj.Inspection_person,
            'Report_Doctor': patient_obj.Report_Doctor,
        }
        return patient_report
    except Exception as e:
        return HttpResponse(e)



def get_the_th_echart(patient_name):
    try:
        patient_objs = patient_TH.objects.filter(patient_name = patient_name)
        print(patient_objs)
        print(type(patient_objs))
        patient_objs = patient_objs
        option = {
            'title': {
                'text': 'TH'
            },
            'tooltip': {
                'trigger': 'axis'
            },
            'legend': {
                'data': ['IL-2', 'IL-4', 'IL-6', 'IL-10', 'TNF-α', 'IFN-γ']
            },
            'toolbox': {
                'show': 'true',
                'feature': {
                    'mark': {'show': 'true'},
                    'magicType': {'show': 'true', 'type': ['line', 'bar', 'stack', 'tiled']},
                }
            },
            'calculable': 'true',
            'xAxis': [
                {
                    'type': 'category',
                    'boundaryGap': 'false',
                    'axisLabel': {'interval': 0},
                    'data': []
                }
            ],
            'yAxis': [
                {
                    'type': 'value'
                }
            ],
            
            'series': [
                {
                    'name': 'IL-2',
                    'type': 'bar',
                    'data': []
                },
                {
                    'name': 'IL-4',
                    'type': 'bar',
                    'data': []
                },
                {
                    'name': 'IL-6',
                    'type': 'bar',
                    'data': []
                },
                {
                    'name': 'IL-10',
                    'type': 'bar',
                    'data': []
                },
                {
                    'name': 'TNF-α',
                    'type': 'bar',
                    'data': []
                },
                {
                    'name': 'IFN-γ',
                    'type': 'bar',
                    'data': []
                }
            ]
        }
        for patient_obj in patient_objs:
            print(patient_obj.patient_IL2)
            print(type(patient_obj.patient_IL2))
            patient_IL2 =float(patient_obj.patient_IL2)
            print(patient_IL2)
            patient_IL4 =float(patient_obj.patient_IL4)
            patient_IL6 =float(patient_obj.patient_IL6)
            patient_IL10 =float(patient_obj.patient_IL10)
            patient_TNF =float(patient_obj.patient_TNF)
            patient_IFN =float(patient_obj.patient_IFN)
            RPmtime = datetime.datetime.strftime(patient_obj.RPmtime,"%Y-%m-%d")
            # RPmtime = patient_obj.RPmtime[0:10]
            option['xAxis'][0]['data'].append(RPmtime)
            option['series'][0]['data'].append(patient_IL2)
            option['series'][1]['data'].append(patient_IL4)
            option['series'][2]['data'].append(patient_IL6)
            option['series'][3]['data'].append(patient_IL10)
            option['series'][4]['data'].append(patient_TNF)
            option['series'][5]['data'].append(patient_IFN)
        import json
        str_option = json.dumps(option)
        return str_option
    except Exception as e:
        return HttpResponse(e)







def imgurl_jion(project_name,local_imgurl):
    try:

        locals_imgurl_index = local_imgurl.rfind(project_name+'\\') + len(project_name) +1
        imgurl_name = local_imgurl[locals_imgurl_index:]
        print(imgurl_name)
        imgurl_name = imgurl_name.replace('\\', '/')
        imgurl = THEURL + "media/" + project_name + '/' + imgurl_name
        print(imgurl)
        return imgurl
    except Exception as e:
        return e