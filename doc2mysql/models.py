from django.db import models

# Create your models here.
class patient_information(models.Model):
    id = models.AutoField(primary_key=True)
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)


class patient_TH(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主要内容
    patient_IL2 = models.CharField(max_length=32)
    patient_IL4 = models.CharField(max_length=32)
    patient_IL6 = models.CharField(max_length=32)
    patient_IL10 = models.CharField(max_length=32)
    patient_TNF = models.CharField(max_length=32)
    patient_IFN = models.CharField(max_length=32)
    # 第三个表格内容
    RPmtime = models.DateTimeField(max_length=64)
    Submit_Sample_time =models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)


class patient_JIEHE(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主要内容
    patient_N = models.CharField(max_length=32)
    patient_T = models.CharField(max_length=32)
    patient_P = models.CharField(max_length=32)
    patient_value = models.CharField(max_length=32)
    patient_result = models.CharField(max_length=32)
    patient_opinion = models.CharField(max_length=1024)
    # 第三个表格内容
    RPmtime = models.DateTimeField(max_length=64)
    Submit_Sample_time =models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)

class patient_LYM(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主要内容
    patient_T = models.CharField(max_length=32)
    patient_Ts = models.CharField(max_length=32)
    patient_Th = models.CharField(max_length=32)
    patient_TsTh_ratio = models.CharField(max_length=32)
    patient_NK = models.CharField(max_length=32)
    patient_B = models.CharField(max_length=32)
    patient_DP = models.CharField(max_length=32, default='0')
    patient_DN = models.CharField(max_length=32, default='0')
    patient_NKT = models.CharField(max_length=32, default='0')
    patient_ABnormal = models.CharField(max_length=32,default='0')
    # 图片链接，共四张图片，抬头一张，
    patient_imgurl_T_F = models.CharField(max_length=1000, default='0')
    patient_imgurl_T_T1 = models.CharField(max_length=1000, default='0')
    patient_imgurl_T_T2 = models.CharField(max_length=1000, default='0')
    patient_imgurl_B_F = models.CharField(max_length=1000, default='0')
    patient_imgurl_B_T1 = models.CharField(max_length=1000, default='0')
    patient_imgurl_B_T2 = models.CharField(max_length=1000, default='0')
    #报告创建时间，上传即在服务器端创建
    RPmtime = models.DateTimeField(max_length=64)
    Submit_Sample_time =models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)


class patient_B27(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主要内容
    patient_result = models.CharField(max_length=64)
    patient_imageurl = models.CharField(max_length=1000)
    report_opinion = models.CharField(max_length=1000)
    # 报告网站生成时间
    RPmtime = models.DateTimeField(max_length=64)
    # 报告时间及检测报告人员
    Submit_Sample_time =models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)

class patient_IRP(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    patient_result= models.CharField(max_length=256)
    patient_imgurl_first_panel = models.CharField(max_length=1000)
    patient_imgurl_sec_panel = models.CharField(max_length=1000)
    report_opinion = models.CharField(max_length=1000)
    # 1
    RPmtime = models.DateTimeField(max_length=64)
    Submit_Sample_time = models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)

class patient_CD34(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主内容
    imgurl = models.CharField(max_length=1000)
    test_total = models.CharField(max_length=1000)
    test_live = models.CharField(max_length=1000,default='未知')
    test_cd34 = models.CharField(max_length=300,default='未知')
    test_cd34_ratio = models.CharField(max_length=1000,default='未知')
    # 报告网站生成时间
    RPmtime = models.DateTimeField(max_length=64)
    # 报告时间及检测报告人员
    Submit_Sample_time = models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)

class patient_FBKT(models.Model):
    id = models.AutoField(primary_key=True)
    # 报告抬头
    patient_ID = models.CharField(max_length=64)
    patient_name = models.CharField(max_length=64)
    patient_sex = models.CharField(max_length=64)
    patient_department = models.CharField(max_length=64)
    patient_age = models.CharField(max_length=64)
    submit_doctor_name = models.CharField(max_length=64)
    # 报告主要内容
    imageurl_contrast = models.CharField(max_length=1000)
    imageurl_detection = models.CharField(max_length=1000)
    CD3_contrast = models.CharField(max_length=64)
    CD3_4_contrast = models.CharField(max_length=64)
    CD3_8_contrast = models.CharField(max_length=64)
    CD3_detection = models.CharField(max_length=64)
    CD3_4_detection = models.CharField(max_length=64)
    CD3_8_detection = models.CharField(max_length=64)
    CD3_block_efficiency = models.CharField(max_length=64)
    CD3_4_block_efficiency = models.CharField(max_length=64)
    CD3_8_block_efficiency = models.CharField(max_length=64)
    # 报告网站生成时间
    RPmtime = models.DateTimeField(max_length=64)
    # 报告时间及检测报告人员
    Submit_Sample_time = models.CharField(max_length=64)
    Detection_time = models.CharField(max_length=64)
    Inspection_person = models.CharField(max_length=64)
    Report_Doctor = models.CharField(max_length=64)