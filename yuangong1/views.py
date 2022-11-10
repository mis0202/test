from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from yuangong1 import models
from django.core.validators import RegexValidator



def depart_list(request):
    depart_info = models.department.objects.all()
    print(depart_info)
    return render(request, "depart_list.html", {"depart_info": depart_info})


def depart_add(request):
    """添加部门"""
    # return render(request, "depart_add.html")
    # 进行判断，如果为GET请求，直接进入添加页面；否则执行添加操作
    if request.method == "GET":
        return render(request, "depart_add.html")
    title = request.POST.get("title")
    models.department.objects.create(title=title)
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""

    # 获取ID
    nid = request.GET.get("nid")

    # 删除
    models.department.objects.filter(id=nid).delete()

    # 重定向到列表
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """修改部门"""
    if request.method == "GET":
        row_object = models.department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_object": row_object})
    title = request.POST.get("title")
    models.department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def user_list(request):
    user_info = models.user_info.objects.all()
    # depart = models.department.objects.filter(id=user.id)

    return render(request, "user_list.html", {"user_list": user_info})


class myForm(forms.ModelForm):
    class Meta:
        model = models.user_info
        fields = ["name", "passwd", "age", "account", "create_time", "depart", "gender"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            print(name, field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_add(request):
    if request.method == "GET":
        form = myForm()
        return render(request, "user_add.html", {"form": form})

    form = myForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_add.html", {"form": form})


def user_edit(request, nid):
    row_object = models.user_info.objects.filter(id=nid).first()
    if request.method == "GET":
        form = myForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})
    form = myForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})


def user_delete(request):
    nid = request.GET.get("nid")

    # 删除
    models.user_info.objects.filter(id=nid).delete()

    # 重定向到列表
    return redirect("/user/list/")

from yuangong1.utiles.pageination import Pageination

def phone_list(request):
    # for i in range(300):
    #     models.phone_num_info.objects.create(phone="16619880393", price=99, status=1, level=2)
    date_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        date_dict["phone__contains"] = search_data

    phone = models.phone_num_info.objects.filter(**date_dict).order_by("status")
    print(phone)
    page_object = Pageination(request, phone)
    page_queryset = page_object.page_queryset

    page_string = page_object.html()

    context = {
        "queryset" : page_queryset,
        "search_data": search_data,
        "page_string": page_string
    }

    return render(request, "phone_list.html", context)


class phoneAdd(forms.ModelForm):
    """ 靓号类添加 """
    # 手机号输入值校验
    phone = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.phone_num_info
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_phone(self):
        txt_phone = self.cleaned_data["phone"]
        exists = models.phone_num_info.objects.filter(phone=txt_phone).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_phone


def phone_add(request):
    """ 添加靓号"""
    if request.method == "GET":
        form = phoneAdd()
        return render(request, "phone_add.html", {"form": form})

    form = phoneAdd(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/phone/list/")
    return render(request, "phone_add.html", {"form": form})


class phoneEdit(forms.ModelForm):
    """ 靓号类编辑 """
    # 手机号输入值校验
    phone = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    )

    class Meta:
        model = models.phone_num_info
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_phone(self):

        txt_phone = self.cleaned_data["phone"]
        exists = models.phone_num_info.objects.exclude(id=self.instance.id).filter(phone=txt_phone).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_phone


def phone_edit(request, nid):
    """ 编辑靓号 """
    row_object = models.phone_num_info.objects.filter(id=nid).first()
    if request.method == "GET":
        form = phoneEdit(instance=row_object)
        return render(request, "phone_edit.html", {"form": form})

    form = phoneEdit(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect("/phone/list/")
    return render(request, "phone_edit.html", {"form": form})


def phone_delete(request):
    """ 删除靓号 """
    nid = request.GET.get("nid")

    # 删除
    models.phone_num_info.objects.filter(id=nid).delete()

    # 重定向到列表
    return redirect("/phone/list/")


######################### dev_operator##########################
def dev_type_list(request):
    date_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        date_dict["dev_type__contains"] = search_data

    dev_type_list = models.dev_type.objects.filter(**date_dict)
    return render(request, "dev_type_list.html", {"dev_type_list": dev_type_list, "search_data": search_data})


class devEdit(forms.ModelForm):
    """ 类编辑 """

    class Meta:
        model = models.dev_type
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    def clean_dev_type(self):

        txt_dev_type = self.cleaned_data["dev_type"]
        exists = models.dev_type.objects.exclude(id=self.instance.id).filter(dev_type=txt_dev_type).exists()
        if exists:
            raise ValidationError("类别已存在")
        return txt_dev_type


def dev_edit(request, nid):
    """ 编辑靓号 """
    row_object = models.dev_type.objects.filter(id=nid).first()
    if request.method == "GET":
        form = devEdit(instance=row_object)
        return render(request, "dev_edit.html", {"form": form})

    form = devEdit(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect("/dev/list/")
    return render(request, "dev_edit.html", {"form": form})


def dev_delete(request):
    """删除部门"""

    # 获取ID
    nid = request.GET.get("nid")

    # 删除
    models.dev_type.objects.filter(id=nid).delete()

    # 重定向到列表
    return redirect("/dev/list/")
