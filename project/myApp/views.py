from django.shortcuts import render,redirect

from django import views
from myApp.models import Question,AnswerRecord,Answer,Kit_Interested_Countries
from userApp.models import MyUser as User
from django_countries import countries


# Create your views here.
from myApp.utils import Mail

class endView(views.View):
    def get(self,requers):
        return render(requers,'end.html')


class IndexView(views.View):
    def get(self,request):
        id =request.GET.get("id",None)
        if id is None or id =="":
            id=1
        question=Question.objects.get(qid=id)
        Isanswer =False


        return render(request,'index.html',locals())

class IndexAnsView(views.View):
    def get(self,request):
        id =request.GET.get("id",None)
        type=request.GET.get("type",None)
        question=Question.objects.get(qid=id)
        isFirst=False
        isFinish=False

        if int(id)==1:

            answerRecord=AnswerRecord.objects.create(userId=request.user.id)
            if int(type)==1:
                Recommendation=" You are free to go next question."
            else:
                isFirst=True
                countrylst = []

                for code, name in list(countries):
                    countrylst.append(name)

            Answer.objects.create(titleId=id,rid=answerRecord.id,result=type)



        else:

            answerRecord=AnswerRecord.objects.filter(userId=request.user.id).last()

            if int(id) == 10:
                isFinish = True
                answerRecord.isFinish=1
                answerRecord.save()


            if int(type)==1:
                Recommendation=question.Recommendation

            else:
                Recommendation=" You are free to go next question."
            Answer.objects.create(titleId=id,rid=answerRecord.id,result=type)


        Isanswer =True

        id=int(id)+1
        return render(request,'index.html',locals())

    def post(self,request):
        name=request.POST.get("name")
        gender=request.POST.get("gender")
        suburb=request.POST.get("suburb")
        country=request.POST.get("country")
        province=request.POST.get("province")
        email=request.POST.get("email")
        answerRecord = AnswerRecord.objects.filter(userId=request.user.id).last()
        Kit_Interested_Countries.objects.create(name=name,gender=gender,suburb=suburb,country=country,province=province,email=email,rid=answerRecord.id)

        mail = Mail()
        content="first and last name:"+name+"\ngender:"+gender+"\nsuburb/postcode:"+suburb+"\ncountry"+country+"\nprovince:"+province+"\nemail:"+email

        mail.send(content)

        return redirect("/index?id=2")



class adminView(views.View):
    def get(self,request):
        #第一次运行需要，第之后删除即可
        try:
            Question.objects.get(qid=1)
        except:
            for i in range(0,11):
                Question.objects.create(title="question"+str(i),qid=i)

        questionlst=Question.objects.all()
        return render(request,'admin.html',locals())


class adminDetailView(views.View):
    def get(self,request):
        id =request.GET.get("id")

        question=Question.objects.get(id=id)
        return render(request,'adminDetail.html',locals())

    def post(self,request):
        id = request.GET.get("id")

        question = Question.objects.get(id=id)
        title=request.POST.get("title")
        Recommendation=request.POST.get("Recommendation").strip()
        question.title=title
        question.Recommendation=Recommendation
        question.save()
        return redirect('/admin')


class adminUserListView(views.View):
    def get(self,request):
        record=AnswerRecord.objects.filter(isFinish=1).all().order_by("-id")
        result=[]
        for i in record:
            dict1={}
            try:
                user=User.objects.get(id=i.userId)
            except:
                continue
            dict1['name']=user.username
            dict1['id']=i.id
            result.append(dict1)
        return render(request,'adminUser.html',locals())

class adminUserLisDetailtView(views.View):
    def get(self,request):
        id =request.GET.get("id")
        isnotAs=False

        answeerlst=Answer.objects.filter(rid=id) .all()
        result=[]
        for i in answeerlst:
            question=Question.objects.get(id=i.titleId)
            dict1={}
            dict1['title']=question.title
            dict1['id']=question.id
            if i.result==1:

                dict1['anser']="yes"
            else:
                dict1['anser']="no"
            result.append(dict1)
            if question.qid==1 and i.result==0:
                userinfo=Kit_Interested_Countries.objects.get(rid=id)
                isnotAs=True


        return render(request,'adminUserDetail.html',locals())


