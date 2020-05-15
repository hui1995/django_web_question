from django.shortcuts import render
# Create your views here.

from django.views import View
from django.contrib import auth
from .models import MyUser as User





from django.shortcuts import redirect
import datetime
# 登录接口


class AuthLogin(View):
    # 跳转登录页面
    def get(self,request):

        return render(request,'login.html')
    def post(self,request):
        # 获取form表单内容

        username=request.POST.get("username")
        password=request.POST.get("password")
        message = "请检查填写的内容"
        # 校验内容

        # 验证账户密码是否争取
        user = auth.authenticate(username=username, password=password)
        # 判断是否验证成功
        if user is not None:
            # 记录session
            auth.login(request, user)
            if user.user_type==0:

                return redirect('/index/')
            else:
                return redirect("/admin/")


        else:

            message = "用户不存在或密码不存在！"

        return render(request, 'login.html', locals())
import time

# 注册页面
class RegisterView(View):


    def get(self,request):

        return render(request,'register.html',locals())
    #添加用户
    def post(self,request):
        #判断是否为管理员用户，如果是则可以添加用户

        username = request.POST.get("username",None)
        password1 = request.POST.get("password",None)
        password2 = request.POST.get("password2",None)
        if username is None:
            message = "用户名不能为空！"
            return render(request, 'register.html', locals())
        if password2 is None or password1 is None:
            message = "密码不能为空！"
            return render(request, 'register.html', locals())


        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'register.html', locals())
        else:
            same_name_user = User.objects.filter(username=username)
            if same_name_user:  # 用户名唯一
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'register.html', locals())


            # 当一切都OK的情况下，创建新用户

            user = User.objects.create_user(username, username+"@admin.com", password1)
            user.user_type=0
            user.save()

            return redirect('/login/')



class UserListView(View):
    def get(self,request):
        userlst=User.objects.exclude(user_type=2)
        return render(request,'adminUser.html',locals())

class UserUpdateView(View):

    def get(self,request):
        user_id=request.GET.get("userId")
        if user_id is not None:
            try:
                user=User.objects.get(id=user_id)
                if user.user_type==0:
                    user.user_type=1
                else:
                    user.user_type=0
                user.save()

            except:
                pass
        return redirect("/user/list")


#退出接口
class LoginOut(View):
    def get(self,reqeust):
        auth.logout(reqeust)
        return redirect('/login')
