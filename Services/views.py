from django.shortcuts import render,render_to_response
from Services.models import Customer,Login,List_of_fligths
from django.shortcuts import HttpResponse
global Fligth_No

# Create your views here
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request, 'login.html')
def test_login(request):
	uname = request.GET['uname']
	pwd = request.GET['pwd']
	
	try:
		obj = Login.objects.get(username=uname)
	except:
		return HttpResponse('User Not available')
	if obj:
		if obj.password == pwd:
			return render(request,'form.html')
			#return HttpResponse('Login Successful')
		else:
			return HttpResponse("Incorrect Password")
def check_fligths(request):
	return render(request,'fligths.html')

def fligth_search(request):
	to=request.GET['to']
	try:
		obj=List_of_fligths.objects.get(To=to)
	except:
		return HttpResponse('Fligths are not available')
	if obj:
		if obj.To==to:
			Fligth_obj=List_of_fligths.objects.get(To=to)
			data={  'fligth_no':Fligth_obj.Fligth_No,
					'fligth_name':Fligth_obj.Fligth_Name,
					'from':Fligth_obj.From,
					'to':Fligth_obj.To,
					'date':Fligth_obj.Date}
			return render_to_response('fligth_search.html',data)
		else:
			return HttpResponse('No Fligth')

def sign_up(request):
    return render(request,'sign_up.html')
def sign_up_user(request):
    if request.method == 'POST':
		Login_Name= request.POST['login_name']
		try :
			obj = Customer.objects.get(Login_Name=login_name)
		except:
			obj = None
			if not obj:
				if request.POST['pwd1'] == request.POST['pwd2']:
					obj = Customer(Login_Name= request.POST['login_name'],Full_Name= request.POST['full_name'],
								   Phone_Number=request.POST['phone_number'],
								   Email_Id= request.POST['email_id'],Password= request.POST['pwd1'],
								   Gender= request.POST['gender'],Date_of_Birth=request.POST['date_of_birth'],
								   Nationality= request.POST['nationality'],Address= request.POST['address'],
								   City= request.POST['city'],Country= request.POST['country'],
								   State= request.POST['state'],Postal_Code= request.POST['postal_code'],
								   ID_Card_Type= request.POST['id_card_type'],ID_Card_Number= request.POST['id_card_number'],
								   Issuing_Authority= request.POST['issuing_authority'])
					obj.save()
					obj = Login(username=request.POST['login_name'], password = request.POST['pwd1'])
					obj.save()
					return render(request, 'login.html')
				else:
					return HttpResponse("Passwords doesn't match")
			else:
				return HttpResponse('User already Exists')
#def frames(request):
#	return render(request,'frames.html')
#def creditcard(request):
	#return render(request,'creditcard.html')






		    
