import docx
import os
import datetime
from doc2mysql.models import patient_B27,patient_TH
from doc2mysql.img_extract import B27_img_extract
from doc2mysql.date_extract import b27_date_extract,TH_date_extract


docdir = r'D:\Temp\docdir'
docxdir = r'D:\Temp\docxdir'

media_B27 = r'E:\reportonline_os\media\B27'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))







def patient_B27_extract(project_name,filename,thisfilename):
    try:
        filename1 = filename.split('.')[0]  # 切片
        FiledocxPathName = filename1 + '.docx'
        print(FiledocxPathName)
        b27_date = b27_date_extract(FiledocxPathName, project_name, filename)
        patient_name = b27_date['patient_name']
        patient_sex = b27_date['patient_sex']
        patient_age = b27_date['patient_age']
        patient_department = b27_date['patient_department']
        patient_ID = b27_date['patient_ID']
        submit_doctor = b27_date['submit_doctor']
        Submit_Sample_time = b27_date['Submit_Sample_time']
        Detection_time = b27_date['Detection_time']
        Inspection_person = b27_date['Inspection_person']
        Report_Doctor = b27_date['Report_Doctor']
        RPmtime = b27_date['RPmtime']
        patient_result = b27_date['patient_result']
        report_opinion = b27_date['report_opinion']
        thisfilename = thisfilename.split('.')[0]
        RPmtime_urltime = datetime.datetime.strftime(RPmtime, "%Y-%m-%d-%H-%M-%S-%f")
        patient_imageurl = B27_img_extract(media_B27,thisfilename,RPmtime_urltime,FiledocxPathName)
        print("%s 图片提取结束" % FiledocxPathName)

        # 存入数据库
        new_b27 = patient_B27.objects.create(
            # 报告抬头
            patient_ID=patient_ID,
            patient_name=patient_name,
            patient_sex=patient_sex,
            patient_department=patient_department,
            patient_age=patient_age,
            submit_doctor_name=submit_doctor,
            # 报告主要内容 书写错误
            patient_result = patient_result,
            patient_imageurl = patient_imageurl,
            report_opinion = report_opinion,
            # 报告时间即检测报告人员
            RPmtime=RPmtime,
            Submit_Sample_time=Submit_Sample_time,
            Detection_time=Detection_time,
            Inspection_person=Inspection_person,
            Report_Doctor=Report_Doctor,
        )
        result = {
            'status':1,
            'patient_name':patient_name,
            'RPmtime':RPmtime,
        }
        return result
    except Exception as e:
        print(e)
        return e




def patient_TH_extract(project_name,filename,thisfilename):
    try:
        filename1 = filename.split('.')[0]  # 切片
        FiledocxPathName = filename1 + '.docx'
        print(FiledocxPathName)
        TH_date = TH_date_extract(FiledocxPathName, project_name, filename)
        patient_name = TH_date['patient_name']
        patient_sex = TH_date['patient_sex']
        patient_age = TH_date['patient_age']
        patient_department = TH_date['patient_department']
        patient_ID = TH_date['patient_ID']
        submit_doctor = TH_date['submit_doctor']
        Submit_Sample_time = TH_date['Submit_Sample_time']
        Detection_time = TH_date['Detection_time']
        Inspection_person = TH_date['Inspection_person']
        Report_Doctor = TH_date['Report_Doctor']
        RPmtime = TH_date['RPmtime']
        patient_IL2 = TH_date['patient_IL2']
        patient_IL4 = TH_date['patient_IL4']
        patient_IL6 = TH_date['patient_IL6']
        patient_IL10 = TH_date['patient_IL10']
        patient_TNF = TH_date['patient_TNF']
        patient_IFN = TH_date['patient_IFN']
        # 存入数据库
        new_TH = patient_TH.objects.create(
            # 报告抬头
            patient_ID=patient_ID,
            patient_name=patient_name,
            patient_sex=patient_sex,
            patient_department=patient_department,
            patient_age=patient_age,
            submit_doctor_name=submit_doctor,
            # 报告主要内容
            patient_IL2 = patient_IL2,
            patient_IL4 = patient_IL4,
            patient_IL6 = patient_IL6,
            patient_IL10 = patient_IL10,
            patient_TNF = patient_TNF,
            patient_IFN = patient_IFN,
            # 报告时间即检测报告人员
            RPmtime=RPmtime,
            Submit_Sample_time=Submit_Sample_time,
            Detection_time=Detection_time,
            Inspection_person=Inspection_person,
            Report_Doctor=Report_Doctor,
        )
        result = {
            'status':1,
            'patient_name':patient_name,
            'RPmtime':RPmtime,
            # 'RPmtime_urltime':RPmtime_urltime,
        }
        print(result)
        return result
    except Exception as e:
        print(e)
        return e

