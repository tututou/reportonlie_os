from django.shortcuts import render
import os
from basehtml.get_report import get_the_th_patient_report,get_the_th_echart,get_the_b27_patient_report
from doc2mysql.doc2docx import beginswith
from django.shortcuts import HttpResponse
from doc2mysql.docx2mysql import patient_B27_extract,patient_TH_extract
from basehtml.query_m import *
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
#


#1


#1
def upload_project_html(request,project_name):
    htmlpath = project_name + '/' + project_name + '_upload.html'
    print(htmlpath)
    tab_name = project_name
    return render(request,'upload_index/report_upload.html', {
        'tab_name':tab_name,
    })

#1
def upload_project_html_action(request, project_name):
    response_data = {}
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    # print(request.POST.)
    if request.method == "POST":
        print(project_name)
        files = request.FILES.getlist('file')
        file_success_list = []
        file_success_patient_name = []
        file_success_patient_RPmtime = []
        file_fail_list = []
        for afile in files:
            dirpath = os.path.join(BASE_DIR,'upload', project_name)
            file_full_name = os.path.join(dirpath,afile.name)
            destination = open(file_full_name,mode='wb')
            for i in afile.chunks():
                destination.write(i)
            destination.close()
            print(project_name,afile.name)
            swith_result=beginswith(project_name, afile.name)
            print(swith_result)
            if swith_result == "swith done":
                print("%s is dod2docxed" % afile)
            else:
                return HttpResponse("%s upload over, but can not be swithed to docx" % swith_result)
           
            if project_name =='B27' or project_name == 'b27':
                tomysql_result = patient_B27_extract(project_name,afile.name)
                if tomysql_result['status'] == 1:
                    file_success_list.append(afile.name)
                    file_success_patient_name.append(tomysql_result['patient_name'])
                    file_success_patient_RPmtime.append(tomysql_result['RPmtime'])
                    print("%s is stored into B27_mysql" % file_success_list)
                else:
                    file_fail_list.append(afile.name)
                    return HttpResponse("\"%s \" upload over and swith to docx,but can not be stored to the B27_mysql \n \"%s \" upload over and swith to docx,but can not be stored to the B27_mysql" % (file_fail_list,file_success_list))

            
            elif project_name =='TH' or project_name == 'th':
                tomysql_result = patient_TH_extract(project_name,afile.name)
                if tomysql_result['status'] == 1:
                    file_success_list.append(afile.name)
                    file_success_patient_name.append(tomysql_result['patient_name'])
                    file_success_patient_RPmtime.append(tomysql_result['RPmtime'])
                    print("%s is stored into TH_mysql" % file_success_list)
                else:
                    file_fail_list.append(afile.name)
                    return HttpResponse("\"%s \" upload over and swith to docx,but can not be stored to the TH_mysql \n \"%s \" upload over and swith to docx,but can not be stored to the TH_mysql" % (file_fail_list,file_success_list))

           
            else:
                print('project_name is wrong')
        print("%s upload over and %s is fail" % (file_success_list,file_fail_list))

        return HttpResponse('上传成功：%s ------------------上传失败：%s' % (file_success_list,file_fail_list))
    else:
        return HttpResponse('method is not POST')

#0
def upload_project_html_action_v2(request, project_name):
    response_data = {}
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    if request.method == "POST":
        print(project_name)
        files = request.FILES.getlist('file')
        print(files)
        file_success_list = []
        file_success_patient_name = []
        file_success_patient_RPmtime = []
        file_fail_list = []
        datedir_name = datetime.datetime.now().strftime("%Y-%m-%d")
        dir_project_path = os.path.join(BASE_DIR, 'upload', project_name)
        dirpath = os.path.join(dir_project_path, datedir_name)
        # 文件保存 ，根据project_name 保存至对应文件夹，
        for afile in files:
            print(afile.name)
            print(type(afile.name))
            if os.path.exists(dirpath):
                pass
            else:
                os.mkdir(dirpath)
            file_full_name = os.path.join(dirpath,afile.name)
            destination = open(file_full_name,mode='wb')
            for i in afile.chunks():
                destination.write(i)
            destination.close()
            thisfilename = afile.name
            thisfilename = thisfilename.split('.')[0]
            print("%s 上传成功" % afile.name)
            print(project_name,file_full_name)
            # file_front_name = afile.name.split('.')[0]
            file_front_name,file_suffix = afile.name.split('.')
            if file_suffix == 'doc':
                swith_result=beginswith(project_name, file_full_name)
                print(swith_result)
                if swith_result == "swith done":
                    print("%s is dod2docxed" % afile)
                else:
                    temp = loader.get_template("upload_result.html")
                    the_result = "%s upload over, but can not be swithed to docx" % swith_result
                    cont = {'upload_result': the_result}
                    return HttpResponse(temp.render(cont))
            else:
                pass
            

            if project_name =='B27' or project_name == 'b27':
                tomysql_result = patient_B27_extract(project_name,file_full_name,thisfilename)
                if tomysql_result['status'] == 1:
                    file_success_list.append(afile.name)
                    file_success_patient_name.append(tomysql_result['patient_name'])
                    this_RPmtime = datetime.datetime.strftime(tomysql_result['RPmtime'],"%Y-%m-%d-%H-%M-%S-%f")
                    file_success_patient_RPmtime.append(this_RPmtime)
                    print("%s is stored into B27_mysql" % file_success_list)
                else:
                    file_fail_list.append(afile.name)
                    the_result = "\"%s \" upload over and swith to docx,but can not be stored to the LYM_mysql \n \"%s \" upload over and swith to docx,but can not be stored to the LYM_mysql" % (
                    file_fail_list, file_success_list)
                    temp = loader.get_template("upload_result.html")
                    cont = RequestContext(request, {'upload_result': the_result})
                    return HttpResponse(temp.render(cont))

            
            elif project_name =='TH' or project_name == 'th':
                tomysql_result = patient_TH_extract(project_name,file_full_name,thisfilename)
                if tomysql_result['status'] == 1:
                    file_success_list.append(afile.name)
                    print(tomysql_result)
                    file_success_patient_name.append(tomysql_result['patient_name'])
                    this_RPmtime = datetime.datetime.strftime(tomysql_result['RPmtime'],"%Y-%m-%d-%H-%M-%S-%f")
                    file_success_patient_RPmtime.append(this_RPmtime)
                    # file_success_patient_RPmtime.append(tomysql_result['RPmtime'])
                    print("%s is stored into TH_mysql" % file_success_list)
                else:
                    file_fail_list.append(afile.name)
                    the_result = "\"%s \" upload over and swith to docx,but can not be stored to the LYM_mysql \n \"%s \" upload over and swith to docx,but can not be stored to the LYM_mysql" % (
                    file_fail_list, file_success_list)
                    temp = loader.get_template("upload_result.html")
                    cont = RequestContext(request, {'upload_result': the_result})
                    return HttpResponse(temp.render(cont))

            
            else:
                print('project_name is wrong')
        pass

        # 返回页面  包含删除按钮
        
        if project_name =='TH' or project_name == 'th':
            today_suceess_upload_result = []
            # 提取今天时间，并把今天所有上传报告返回方便管理
            now_date = datetime.datetime.now()
            today_date = now_date - datetime.timedelta(days=1)
            patient_th_objs = patient_TH.objects.filter(RPmtime__gte=today_date)
            for patient_th_obj in patient_th_objs:
                i = patient_th_obj.RPmtime
                print(type(i))
                print(i)
                i = datetime.datetime.strftime(i,"%Y-%m-%d-%H-%M-%S-%f")
                patient_check_url = THEURL + 'TH' + '/' + patient_th_obj.patient_name + '/' + i
                patient_delete_url = THEURL+"delete/" + 'TH' + '/' + patient_th_obj.patient_name + '/' + i
                this_query_TH_obj = {
                    'patient_name': patient_th_obj.patient_name,
                    'patient_ID': patient_th_obj.patient_ID,
                    'patient_check_url': patient_check_url,
                    'patient_delete_url': patient_delete_url,
                    'patient_RPmtime': patient_th_obj.RPmtime,
                }
                today_suceess_upload_result.append(this_query_TH_obj)
            the_result = '上传成功：%s ------------------上传失败：%s' % (file_success_list,file_fail_list)
            temp = loader.get_template("upload_result.html")
            cont = {
                'upload_result': the_result,
                'today_upload_flie':today_suceess_upload_result,
            }
            return HttpResponse(temp.render(cont))
        
        elif project_name =='B27' or project_name == 'b27':
            today_suceess_upload_result = []
            now_date = datetime.datetime.now()
            today_date = now_date - datetime.timedelta(days=1)
            patient_b27_objs = patient_B27.objects.filter(RPmtime__gte=today_date)
            for patient_B27_obj in patient_b27_objs:
                i = patient_B27_obj.RPmtime
                i = datetime.datetime.strftime(i,"%Y-%m-%d-%H-%M-%S-%f")
                patient_check_url = THEURL + 'B27' + '/' + patient_B27_obj.patient_name + '/' + i
                patient_delete_url = THEURL+"delete/" + 'B27' + '/' + patient_B27_obj.patient_name + '/' + i
                this_query_B27_obj = {
                    'patient_name': patient_B27_obj.patient_name,
                    'patient_ID': patient_B27_obj.patient_ID,
                    'patient_check_url': patient_check_url,
                    'patient_delete_url': patient_delete_url,
                    'patient_RPmtime': patient_B27_obj.RPmtime,
                }
                today_suceess_upload_result.append(this_query_B27_obj)
            the_result = '上传成功：%s ------------------上传失败：%s' % (file_success_list,file_fail_list)
            temp = loader.get_template("upload_result.html")
            cont = {
                'upload_result': the_result,
                'today_upload_flie':today_suceess_upload_result,
            }
            return HttpResponse(temp.render(cont))
        
    else:
        return HttpResponse('method is not POST')

#0
def drop_mysql(request,project_name,patient_name,RPmtime):
    try:
        
        if project_name == 'TH' or project_name == 'th':
            print(RPmtime)
            RPmtime = datetime.datetime.strptime(RPmtime,"%Y-%m-%d-%H-%M-%S-%f")
            print(RPmtime)
            patient_TH.objects.get(patient_name=patient_name, RPmtime=RPmtime).delete()
            this_message = "%s - %s 删除成功" % (patient_name, RPmtime)
            print(this_message)
            temp = loader.get_template("delete_result.html")
            print("1111")
            the_result = "%s " % this_message
            cont = {'delete_result': the_result}
            return HttpResponse(temp.render(cont))

        elif project_name == 'B27' or project_name == 'b27':
            print(RPmtime)
            RPmtime = datetime.datetime.strptime(RPmtime, "%Y-%m-%d-%H-%M-%S-%f")
            print(RPmtime)
            patient_B27.objects.get(patient_name=patient_name, RPmtime=RPmtime).delete()
            this_message = "%s - %s 删除成功" % (patient_name,RPmtime)
            temp = loader.get_template("delete_result.html")
            the_result = "%s " % this_message
            cont = {'delete_result': the_result}
            return HttpResponse(temp.render(cont))
        
        else:
            this_message = "请检查文件是否存在"
            temp = loader.get_template("delete_result.html")
            the_result = "%s " % this_message
            cont = {'delete_result': the_result}
            return HttpResponse(temp.render(cont))
    except Exception as e:
        return HttpResponse(e)

#0
def upload_index(request):
    return render(request, 'upload_index/upload_index.html')




#1
def patient_B27_report(request, patient_name, RPmtime):
    print(patient_name,RPmtime)
    print(type(patient_name),type(RPmtime))
    try:
        patient_report = get_the_b27_patient_report(patient_name,RPmtime)
        return render(request,'B27/B27_report.html',
                      patient_report)
    except Exception as e:
        return HttpResponse(e)



#1
def patient_TH_report(request, patient_name, RPmtime):
    print(patient_name,RPmtime)
    try:
        patient_report = get_the_th_patient_report(patient_name,RPmtime)
        patient_report_echart = get_the_th_echart(patient_name)
        patient_report['option'] = patient_report_echart
        print("修改1")
        return render(request,'TH/TH_report_v2.html',
                      patient_report)
    except Exception as e:
        return HttpResponse(e)



#1
def patient_TH_report_echart(request, patient_name):
    print(patient_name)
    print(type(patient_name))
    try:
        str_option = get_the_th_echart(patient_name)
        return render(request,'THE_echart.html',{
            'option':str_option,
            'patient_name':patient_name,
        }
                     )
    except Exception as e:
        return HttpResponse(e)




def query_page(request):
    query_form = QueryForm()
    return render(request,'query_index/query_page.html',
                  {'query_form':query_form,})

#1
def query_index(request):
    if request.method == "POST":
        try:
            patient_name_or_id = request.POST.get('patient_name_or_id')

            print(type(patient_name_or_id))
            print(patient_name_or_id)
            result_dict = get_query_id_name(patient_name_or_id)
            return render(request, 'query_index/query_index.html', result_dict)
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse("请使用POST方法")

def query_index_try(request):
    if request.method == "POST":
        try:
            patient_name_or_id = request.POST.get('patient_name_or_id')
            print(type(patient_name_or_id))
            print(patient_name_or_id)
            # 淋巴查询
            patient_LYM_obj = patient_LYM.objects.filter(Q(patient_name=patient_name_or_id) | Q(patient_ID=patient_name_or_id))
            print(1)
            query_LYM_result = []
            for i in patient_LYM_obj:
                patient_url = THEURL+"media/" + 'LYM' + '/' + i.patient_name + '/' +i.RPmtime
                print(i.patient_name,i.patient_ID,i.RPmtime)
                this_query_LYM_obj = {
                    'patient_name_or_id':patient_name_or_id,
                    'patient_name':i.patient_name,
                    'patient_ID':i.patient_ID,
                    'patient_url':patient_url,
                    'patient_RPmtime':i.RPmtime,
                }
                query_LYM_result.append(this_query_LYM_obj)
            return render(request,'query_index/query_index_try.html',{
                'lym_items':query_LYM_result
            })
        except Exception as e:
            print(e)
            return HttpResponse(e)
            # if patient_ID != "":
            #     patient_LYM_obj = patient_LYM.objects.get(patient_name=request., RPmtime=RPmtime)
            # else:
    else:
        return HttpResponse("请使用POST方法")

@login_required(login_url='/login_page/')
def manage_query_index(request):
    manage_time_query = Manage_time_query()
    manage_project_query = Manage_project_query()
    manage_department_query = Manage_department_query()
    specify_query_form = QueryForm()
    return render(request,'query_index/RP_manage_query.html',{
        'specify_query_form': specify_query_form,
        'manage_time_query': manage_time_query,
        'manage_project_query' :manage_project_query,
        'manage_department_query': manage_department_query
    })

@login_required(login_url='/login_page/')
def manage_project_query(request,project_name):
    manage_time_query = Manage_time_query()
    manage_project_query = Manage_project_query()
    manage_department_query = Manage_department_query()
    specify_query_form = QueryForm()
    return render(request,'query_index/RP_manage_query.html',{
        'specify_query_form': specify_query_form,
        'manage_time_query': manage_time_query,
        'manage_project_query' :manage_project_query,
        'manage_department_query': manage_department_query
    })

@login_required(login_url='/login_page/')
def manage_date_query(request,the_time):
    print(the_time)
    print(type(the_time))
    try:
        if the_time == "1days":
            now = datetime.datetime.now()
            start_time = now - 1 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        if the_time == '7days':
            now = datetime.datetime.now()
            start_time = now - 7*(datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request,'query_index/RP_manage_query_index.html',this_time_query_set)
        elif the_time == '14days':
            now = datetime.datetime.now()
            start_time = now - 14 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        elif the_time == '30days':
            now = datetime.datetime.now()
            start_time = now - 30 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        elif the_time == '60days':
            now = datetime.datetime.now()
            start_time = now - 60 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        elif the_time == '90days':
            now = datetime.datetime.now()
            start_time = now - 90 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        elif the_time == '180days':
            now = datetime.datetime.now()
            start_time = now - 180 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        elif the_time == '365days':
            now = datetime.datetime.now()
            start_time = now - 365 * (datetime.timedelta(hours=24))
            print(start_time)
            # 封装函数time_query,传入start_time,return this_time_query_set
            this_time_query_set = time_query_action_for_manage(start_time)
            print("!!!!!!!!!")
            return render(request, 'query_index/RP_manage_query_index.html', this_time_query_set)
        else:
            return HttpResponse('特殊病人查询，请先查找病人ID号或姓名，再准确查询')
    except Exception as e:
        return HttpResponse(e)


def time_query_action_for_manage(start_time):
    
    # B27
    patient_B27_obj = patient_B27.objects.filter(
        RPmtime__gte=start_time)
    query_B27_result = []
    for i in patient_B27_obj:
        the_time = i.RPmtime
        this_rpmtime = datetime.datetime.strftime(the_time, '%Y-%m-%d-%H-%M-%S-%f')
        patient_url = THEURL + 'B27' + '/' + i.patient_name + '/' + this_rpmtime
        patient_delete_url = THEURL + 'delete/B27' + '/' + i.patient_name + '/' + this_rpmtime
        this_query_B27_obj = {
            'patient_name': i.patient_name,
            'patient_ID': i.patient_ID,
            'patient_url': patient_url,
            'patient_delete': patient_delete_url,
            'patient_RPmtime': this_rpmtime,
        }
        query_B27_result.append(this_query_B27_obj)
   
    # TH
    patient_TH_obj = patient_TH.objects.filter(
        RPmtime__gte=start_time)
    query_TH_result = []
    for i in patient_TH_obj:
        the_time = i.RPmtime
        this_rpmtime = datetime.datetime.strftime(the_time, '%Y-%m-%d-%H-%M-%S-%f')
        patient_url =THEURL + 'TH' + '/' + i.patient_name + '/' + this_rpmtime
        patient_delete_url = THEURL + 'delete/TH' + '/' + i.patient_name + '/' + this_rpmtime
        this_query_TH_obj = {
            'patient_name': i.patient_name,
            'patient_ID': i.patient_ID,
            'patient_url': patient_url,
            'patient_delete_url': patient_delete_url,
            'patient_RPmtime': this_rpmtime,
        }
        query_TH_result.append(this_query_TH_obj)
    
    total_query_num = len(query_B27_result)+len(query_TH_result)
    this_time_query_set = {
        
        'b27_items': query_B27_result,
        'th_items': query_TH_result,
        
        
        'b27_items_num': len(query_B27_result),
        'th_items_num': len(query_TH_result),
        
        'total_query_num':total_query_num,
    }
    print(this_time_query_set)
    return this_time_query_set

def logout_authentication(request):
    print('logou action')
    logout(request)
    print("_______________________")
    query_form = QueryForm()
    return render(request,'query_index/query_page.html',
                  {'query_form':query_form,})

def login_authentication(request):

    response_data = {'status':'failure',
                     'message':'出问题了，再试一下'}
    if request.method == "POST":
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        print(user)
        if user is not None:
            if user.is_active:

                response_data = {'status':'success',
                                 'message':'欢迎回来',
                                 }
                # TODO 根据状态显示title，以及改变tpnav里的
                login(request, user)
                query_form = QueryForm()
                return render(request, 'query_index/query_page.html',
                              {'query_form': query_form, })
            else:
                response_data = {'status':'failure',
                                 'message':'你的账户还被困在火星上'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {
                'status':'failure',
                'message':'用户名密码错误'
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data = {
            'status':'failure',
            'message':'请检查网络配置或使用POST'
        }
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def login_page(request):
    login_form = LoginForm()
    return render(request,'login_page.html',{
        'login_form':login_form,
    })

def download_file(requeset,project_name,patient_name,file_time):
    print(project_name,patient_name,file_time)
    try:
        #可优化
        file_time = file_time[:10]
        print(file_time)
        patient_name_time = file_time.replace("-",'')
        patient_file_docx_name = patient_name + patient_name_time + ".docx"
        print(patient_file_docx_name)
        FilePathName = os.path.join(BASE_DIR,project_name,file_time,patient_file_docx_name)
        print(FilePathName)
        with open(FilePathName) as f:
            c = f.read()
        return HttpResponse(c)
    except Exception as e:
        return HttpResponse(e)







