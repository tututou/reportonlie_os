from django.db.models import Q
from django.shortcuts import HttpResponse
from doc2mysql.models import *
import datetime
from reportonline_os.settings import THEURL


def get_query_id_name(patient_name_or_id):
    try:
        patient_LYM_obj = patient_LYM.objects.filter(
            Q(patient_name=patient_name_or_id) | Q(patient_ID=patient_name_or_id))
        
        # B27
        patient_B27_obj = patient_B27.objects.filter(
            Q(patient_name=patient_name_or_id) | Q(patient_ID=patient_name_or_id))
        query_B27_result = []
        for i in patient_B27_obj:
            the_time = i.RPmtime
            this_rpmtime = datetime.datetime.strftime(the_time, '%Y-%m-%d-%H-%M-%S-%f')
            patient_url = THEURL + 'B27' + '/' + i.patient_name + '/' + this_rpmtime
            this_query_B27_obj = {
                'patient_name_or_id': patient_name_or_id,
                'patient_name': i.patient_name,
                'patient_ID': i.patient_ID,
                'patient_url': patient_url,
                'patient_RPmtime': this_rpmtime,
            }
            query_B27_result.append(this_query_B27_obj)
        
        # TH
        patient_TH_obj = patient_TH.objects.filter(
            Q(patient_name=patient_name_or_id) | Q(patient_ID=patient_name_or_id))
        query_TH_result = []
        for i in patient_TH_obj:
            the_time = i.RPmtime
            this_rpmtime = datetime.datetime.strftime(the_time, '%Y-%m-%d-%H-%M-%S-%f')
            patient_url = THEURL + 'TH' + '/' + i.patient_name + '/' + this_rpmtime
            this_query_TH_obj = {
                'patient_name_or_id': patient_name_or_id,
                'patient_name': i.patient_name,
                'patient_ID': i.patient_ID,
                'patient_url': patient_url,
                'patient_RPmtime': this_rpmtime,
            }
            query_TH_result.append(this_query_TH_obj)
        
            ############################全部查询完毕####################
        total_query_num = len(query_LYM_result) + len(query_B27_result) + len(query_TH_result) + len(
            query_FBKT_result) + len(query_CD34_result) + len(query_IRP_result) + len(query_JIEHE_result)
        result_dict = {
                
                'b27_items': query_B27_result,
                'th_items': query_TH_result,
                
                'total_query_num':total_query_num,
                
                'b27_items_num': len(query_B27_result),
                'th_items_num': len(query_TH_result),
                
            }
        return result_dict

    except Exception as e:
        return HttpResponse(e)

