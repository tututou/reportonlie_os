from doc2mysql.models import patient_LYM
from django.forms import ModelForm
from django import forms

class LYM_form(ModelForm):
    class Meta:
        model = patient_LYM
        fields = [
            # 报告抬头
            'patient_ID',
            'patient_name',
            'patient_sex',
            'patient_department',
            'patient_age',
            'submit_doctor_name',
            # 报告数据
            'patient_T',
            'patient_Ts',
            'patient_Th',
            'patient_TsTh_ratio',
            'patient_NK',
            'patient_B',
            'patient_DP',
            'patient_DN',
            'patient_NKT',
            'patient_ABnormal',
            # 图片
            'patient_imgurl_T_F',
            'patient_imgurl_T_T1',
            'patient_imgurl_T_T2',
            'patient_imgurl_B_F',
            'patient_imgurl_B_T1',
            'patient_imgurl_B_T2',
            # 报告时间 人
            'RPmtime',
            'Submit_Sample_time',
            'Detection_time',
            'Inspection_person',
            'Report_Doctor',
        ]

class QueryForm(forms.Form):
    # patient_name = forms.CharField(
    #     label="患者姓名",
    #     max_length=256,
    #     widget=forms.TextInput(attrs={
    #         'type':'patient_name',
    #         'class':'form-control',
    #         'placeholder':'请输入患者姓名'
    #    }),
    #    required=None,
    # )
    # patient_ID = forms.CharField(
    #     label="患者ID",
    #     max_length=256,
    #     widget=forms.TextInput(attrs={
    #         'type':'patient_ID',
    #         'class':'form-control',
    #         'placeholder':'请输入患者ID'
    #    }),
    #    required=None,
    # )
    patient_name_or_id = forms.CharField(
        label="患者姓名或者患者ID",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type':'patient_name_or_id',
            'class':'form-control',
            'placeholder':'请输入患者姓名或者患者ID'
       }),
       required=True,
    )

    # captcha = CaptchaField(
    #     label='验证码',
    #     error_messages={
    #         "invalid":"验证码错误",
    #         "required":"请输入验证码",
    #     })


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type':'usernmae',
            'class':'form-control',
            'placeholder':'用户名/电话/邮箱'
       }),
       required=True,
    )
    password = forms.CharField(
        label='密码',
        max_length=256,
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': '请输入密码'
        }),
        required=True,
    )


class Manage_time_query(forms.Form):
    begin_time = forms.CharField(
        label="开始时间",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type': 'begin_time',
            'class': 'form-control',
            'placeholder': '请输入开始时间'
        }),
        required=True,
    )
    end_time = forms.CharField(
        label="截止时间",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type': 'end_time',
            'class': 'form-control',
            'placeholder': '请输入截止时间'
        }),
        required=True,
    )

class Manage_department_query(forms.Form):
    department_name = forms.CharField(
        label="科室名称",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type': 'department_name',
            'class': 'form-control',
            'placeholder': '请输入科室名称'
        }),
        required=True,
    )

class Manage_project_query(forms.Form):
    project_name = forms.CharField(
        label="检查项目名称",
        max_length=256,
        widget=forms.TextInput(attrs={
            'type': 'project_name',
            'class': 'form-control',
            'placeholder': '请输入检查项目名称'
        }),
        required=True,
    )