from django.db import models

""" 数据库创建操作：
# 需要用数据库工具链接后创建：
# create database day17 default charset utf8 collate utf8_general_ci; 
# makemigrations   
# migrate --fake
# 删库重建后需要加 --fake 参数

"""


class department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name="部门名", max_length=32)

    def __str__(self):
        return self.title


class user_info(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    passwd = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间", )

    # 数据库做的操作
    # 无约束
    # depart = models.BigIntegerField(verbose_name="部门ID")
    # 1、有约束
    # - to 关联表
    # - to_field 关联表中的那一列
    # 2、django自动
    # - 写的是depart
    # - 生成的时候自动改成depart_id
    # 3、部门表被删除后
    # - 置空（前提是该列允许为空）
    #   depart = models.ForeignKey(verbose_name="部门ID",to="department", null= True, blank=True,to_field="id",on_delete=models.SET_NULL)
    # - 级联删除
    #   depart = models.ForeignKey(verbose_name="部门ID",to="department",to_field="id",on_delete=models.CASCADE)

    depart = models.ForeignKey(verbose_name="部门", to="department", to_field="id", on_delete=models.CASCADE)

    # 在django中做的约束
    gender_choise = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choise)


# Create your models here.


# class user(models.Model):
#     """ 员工表 """
#     name = models.CharField(verbose_name="姓名", max_length=16)
#     passwd = models.IntegerField(verbose_name="密码")
#     age = models.IntegerField(verbose_name="年龄")
#     depart = models.ForeignKey(verbose_name="部门ID", to="department", to_field="id", on_delete=models.CASCADE)
#     phone_num = models.IntegerField(verbose_name="手机号")
#     mail = models.CharField(verbose_name="邮箱地址", max_length=132)
#     # account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
#     create_time = models.DateTimeField(verbose_name="入职时间")
#     # birthday = models.DateTimeField(verbose_name="生日")
#     # 数据库做的操作
#     # 无约束
#     # depart = models.BigIntegerField(verbose_name="部门ID")
#     # 1、有约束
#     # - to 关联表
#     # - to_field 关联表中的那一列
#     # 2、django自动
#     # - 写的是depart
#     # - 生成的时候自动改成depart_id
#     # 3、部门表被删除后
#     # - 置空（前提是该列允许为空）
#     #   depart = models.ForeignKey(verbose_name="部门ID",to="department", null= True, blank=True,to_field="id",on_delete=models.SET_NULL)
#     # - 级联删除
#     #   depart = models.ForeignKey(verbose_name="部门ID",to="department",to_field="id",on_delete=models.CASCADE)
#
#     depart = models.ForeignKey(verbose_name="部门ID", to="department", to_field="id", on_delete=models.CASCADE)
#
#     # 在django中做的约束
#     gender_choise = (
#         (1, "男"),
#         (2, "女"),
#     )
#     gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choise)


class phone_num_info(models.Model):
    """靓号表"""
    phone = models.CharField(verbose_name="手机号", max_length=11)
    price = models.DecimalField(verbose_name="价格", max_digits=10, decimal_places=2, default=99.00)
    status_choise = (
        (0, "闲置"),
        (1, "占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choise)

    level_choise = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choise)


# Create your models here.、


""" 云平台工单 """


class things_source(models.Model):
    """ 请求来源表 """
    things_source = models.CharField(verbose_name='请求来源', max_length=32)

    def __str__(self):

        return self.things_source


class dev_type(models.Model):
    dev_type = models.CharField(verbose_name='设备类型', max_length=32)

    def __str__(self):
        return self.dev_type


