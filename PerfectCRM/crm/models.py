from django.db import models

from django.contrib.auth.models import  User
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=32)
    qq = models.CharField(max_length=64,unique=True)
    weixin = models.CharField(max_length=64,blank=True,null=True)
    age = models.PositiveSmallIntegerField(blank=True,null=True)
    gender = models.PositiveIntegerField(choices=((0,'Female'),(1,'Male')),blank=True,null=True)
    phone = models.PositiveIntegerField(blank=True,null=True)

    source_choices = ((0,'Baidu商桥'),
                      (1,'51CTO'),
                      (2,'QQ群'),
                      (3,'知乎'),
                      (4,'SOGO'),
                      (5,'转介绍'),
                      (6,'其他'),
                      )
    source = models.SmallIntegerField(choices=source_choices)
    referral_from = models.ForeignKey("Customer",related_name="my_referrals",
                                      blank=True,null=True,verbose_name="转介绍")

    consult_courses = models.ManyToManyField("Course")
    status_choices = ((0,'已报名'),(1,'未报名'),(2,'已退学'))
    status = models.SmallIntegerField(choices=status_choices)
    consultant  = models.ForeignKey("UserProfile", verbose_name="课程顾问")
    consult_content = models.TextField(max_length=1024)

    date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "客户信息表"
        verbose_name = "客户信息表"

class Enrollment(models.Model):
    """学员报名信息"""
    customer = models.ForeignKey("Customer")
    class_grade = models.ForeignKey("ClassList")
    enrollment_date = models.DateField()

    def __str__(self):
        return self.customer

    class Meta:
        unique_together =  ("customer","class_grade")


class FollowUpRecord(models.Model):
    customer = models.ForeignKey("Customer")
    content = models.TextField(max_length=1024)

    status_choices = (
        (0,'绝无报名计划'),
        (1,'一个月内报名'),
        (2,'2周内报名'),
        (3,'已报名其它机构'),
    )
    status = models.SmallIntegerField(choices=status_choices)
    consultant  = models.ForeignKey("UserProfile", verbose_name="课程顾问")

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s" % self.customer

class Course(models.Model):
    '''课程表'''
    name = models.CharField(unique=True,max_length=64)
    price = models.PositiveIntegerField(default=19800)
    outline = models.TextField()


    def __str__(self):
        return self.name


class ClassList(models.Model):
    '''班级列表'''
    course = models.ForeignKey("Course")
    semester = models.PositiveSmallIntegerField(verbose_name="学期")
    class_type_choices = ((0,'脱产'),(1,'周末'),(2,'网络'))
    branch  = models.ForeignKey("Branch")
    class_type = models.PositiveSmallIntegerField(choices=class_type_choices)
    teachers = models.ManyToManyField("UserProfile")
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return "%s" % self.course




class CourseRecord(models.Model):
    """每节课上课纪录"""
    class_grade = models.ForeignKey("ClassList")
    day_number = models.PositiveSmallIntegerField(verbose_name="节次")
    teacher = models.ForeignKey("UserProfile")
    CourseContent = models.TextField(verbose_name="课程内容",max_length=1024)
    has_homework = models.BooleanField(default=True)
    homework_title = models.CharField(max_length=128,blank=True,null=True)
    homework_requirement = models.TextField(verbose_name="作业需求",max_length=1025,blank=True,null=True)


    def __str__(self):
        return " daynum:%s" %(self.day_number)

    class Meta:
        unique_together = ("class_grade","day_number")

class StudyRecord(models.Model):
    """每个学生上的每节课的成绩纪录"""
    course_record = models.ForeignKey("CourseRecord")
    student  = models.ForeignKey("Enrollment")
    score_choices = ((100,"A+"),
                     (90,"A"),
                     (85,"B+"),
                     (80,"B"),
                     (75,"B-"),
                     (70,"C+"),
                     (65,"C"),
                     (40,"C-"),
                     (-20,"D"),
                     (-50,"COPY"),
                     (0,"N/A"),
                     )
    score = models.SmallIntegerField(choices=score_choices)
    show_status_choices = ((0,"缺勤"),(1,"已签到"),(2,"迟到"))
    show_status = models.SmallIntegerField(choices=show_status_choices)
    grade_comment = models.TextField(max_length=1024,blank=True,null=True)


    def __str__(self):
        return "%s  daynum:%s" % (self.course_record, self.student)


    class Meta:
        unique_together = ("course_record", "student")



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)

    roles = models.ManyToManyField("Role",blank=True,null=True)


    def __str__(self):
        return self.name

class Role(models.Model):
    """角色表"""
    name = models.CharField(unique=True,max_length=32)
    menus = models.ManyToManyField("Menu")

    def __str__(self):
        return self.name


class Branch(models.Model):
    """分校"""
    name = models.CharField(unique=True,max_length=128)

    def __str__(self):
        return self.name

class Menu(models.Model):
    """动态菜单"""
    name = models.CharField(unique=True,max_length=32)
    url_type = models.SmallIntegerField(choices=((0,'relative_name'),(1,'absolute_url')))
    url_name = models.CharField(unique=True,max_length=128)


    def __str__(self):
        return self.name