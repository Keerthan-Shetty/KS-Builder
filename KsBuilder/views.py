from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from .models import client_register, project_register, Vendor_Register, Vendor_Quotation


# Home page

def Homepage(request):
    return render(request, 'Homepage.html')


# Customer/client Login page

def Client_login(request):
    if request.method == 'POST':
        client_username = request.POST.get('username')
        client_password = request.POST.get('password')
        try:
            user = client_register.objects.get(Username=client_username, Password=client_password)
            if user.Login_Status:
                return redirect('/client_profile/')
            else:
                return HttpResponse('Your Account is still Verifying, please wait some time...')
        except client_register.DoesNotExist:
            return HttpResponse('Invalid Username or Password')
    return render(request, 'Client/Client_Login.html')


# Customer/client register page

def Client_register(request):
    if request.method == "POST":
        client_name = request.POST.get('name')
        client_email = request.POST.get('email')
        client_mobile = request.POST.get('tel')
        client_username = request.POST.get('username')
        client_password = request.POST.get('password')
        users = client_register()
        users.Name = client_name
        users.Email = client_email
        users.Mobile = client_mobile
        users.Username = client_username
        users.Password = client_password
        users.save()
        return redirect('/client_login/')
    return render(request, 'Client/Client_Register.html')


# Client Profile

def Client_profile(request):
    return render(request, 'Client/client_profile.html')


# Client Project registration

def Project_Register(request):
    if request.method == "POST":
        getname = request.POST.get('name')
        get_email = request.POST.get('email')
        get_mobile = request.POST.get('mobile')
        get_project_type = request.POST.get('project_type')
        get_land_area = request.POST.get('land_area')
        get_land_type = request.POST.get('land_type')
        get_floors = request.POST.get('floors')
        project = project_register()
        project.Name = getname
        project.Email = get_email
        project.Mobile = get_mobile
        project.Project_Type = get_project_type
        project.Land_Area = get_land_area
        project.Land_Type = get_land_type
        project.Floors = get_floors
        project.save()
    return render(request, 'Client/client_project_register.html')


# Client Quotation page

def client_quotation(request):
    details = project_register.objects.all()
    return render(request, 'Client/project_quotation.html', {'value': details})


# client project approval

def client_conform(request, id):
    details = project_register.objects.get(id=id)
    details.Client_approved = 'Yes'
    details.save()
    return redirect('/project_quotation_page/')


# project update

def client_project_update_page(request):
    details = project_register.objects.filter(Client_approved='No')
    return render(request, 'Client/project_update.html', {'value': details})


# updating the quotation

def quotation_update(request, id):
    details = project_register.objects.get(id=id)
    if request.method == 'POST':
        get_quotation = request.POST.get('total_quote')
        details.Manager_Quotation = get_quotation
        details.save()
        return redirect('/client_project_update/')
    return render(request, 'Client/project_update.html', {'values': details})


# project approval conformed(Client profile)

def project_approved(request):
    details = project_register.objects.filter(Manager_Approved='Yes')
    return render(request, 'Client/project_approval_conformed.html', {'values': details})


# client forget password

def client_forget_password(request):
    user_details = None
    if request.method == 'POST':
        if 'username_form' in request.POST:
            get_name = request.POST.get('name')
            try:
                user_details = client_register.objects.get(Username=get_name)
            except client_register.DoesNotExist:
                return HttpResponse('User not found')
        elif 'password_form' in request.POST:
            get_name = request.POST.get('name')
            get_password = request.POST.get('client_password')
            try:
                user_details = client_register.objects.get(Username=get_name)
                user_details.Password = get_password
                user_details.save()
                return redirect('/client_login/')
            except Vendor_Register.DoesNotExist:
                return HttpResponse('User not found')
    return render(request, 'Client/client_forget_password.html', {'data': user_details})


# ------------------Manager------------------

# Manager login

def manager_login(request):
    if request.method == "POST":
        manager_name = request.POST.get('manager_name')
        manager_password = request.POST.get('manager_password')
        if manager_name.lower() == 'manager' and manager_password.lower() == 'manager':
            return redirect('/manager_profile/')
        else:
            return HttpResponse('Your Password or Username might be incorrect..!')
    return render(request, 'Manager/manager_login.html')


# Manager profile

def manager_profile(request):
    return render(request, 'Manager/manager_profile.html')


# client login approval page

def manager_login_approval(request):
    details = client_register.objects.filter(Login_Status=False)
    return render(request, 'Manager/managerlogin_approval.html', {'data': details})


# login approve

def login_approve(request, Id):
    details = client_register.objects.get(id=Id)
    details.Login_Status = True
    details.save()
    return redirect('/manager_login_approval/')


# Project request form

def project_request(request):
    details = project_register.objects.all()
    return render(request, 'Manager/client_request_form.html', {'data': details})


# Project approve

def project_approve(request, id):
    details = project_register.objects.get(id=id)
    details.Project_Approved = "Yes"
    details.save()
    return redirect('/project_request/')


# Project reject

def project_reject(request, id):
    details = project_register.objects.get(id=id)
    details.delete()
    return redirect('/project_request/')


# Manager side project quotation page

def manager_quotation(request):
    project_detail = project_register.objects.filter(Location_Tested='Yes')
    return render(request, 'Manager/manager_quotation.html', {'value': project_detail})


# Manager project update page

def project_update_page(request):
    details = project_register.objects.filter(Location_Tested='Yes')
    return render(request, 'Manager/project_update.html', {'value': details})


# Manager project update

def project_update(request, id):
    detail = project_register.objects.get(id=id)
    if request.method == 'POST':
        get_vendor_quotation = request.POST.get('vendor_quote')
        get_other_cost = request.POST.get("other-cost")
        get_manager_quotation = request.POST.get('manager-quotation')
        detail.Vendor_Quotation = get_vendor_quotation
        detail.Other_costs = get_other_cost
        detail.Manager_Quotation = get_manager_quotation
        detail.save()
        return redirect('/project_update_page/')
    return render(request, 'Manager/project_update.html', {'values': detail})


# manager project approval page

def project_approval_page(request):
    detail = project_register.objects.filter(Client_approved='Yes')
    return render(request, 'Manager/project_approved.html', {'values': detail})


# Manager project approval

def project_conform(request, id):
    details = project_register.objects.get(id=id)
    details.Manager_Approved = 'Yes'
    details.save()
    return redirect('/project_approval_page/')


# Project Profit

def project_profit(request):
    details = project_register.objects.filter(Manager_Approved='Yes')
    return render(request, 'Manager/project_profit.html', {'value': details})


# project calculation

def project_calculate(request, id):
    details = project_register.objects.get(id=id)
    if request.method == 'POST':
        get_actual_quote = request.POST.get('actual_quote')
        get_profit = request.POST.get('profit')
        details.Actual_Quotation = get_actual_quote
        details.Profit = get_profit
        details.save()
        return redirect('/project_profit/')
    return render(request, 'Manager/project_profit.html', {'values': details})


# ------------------Management team------------------
# Management team login

def team_login(request):
    if request.method == "POST":
        team_username = request.POST.get('team_username')
        team_password = request.POST.get('team_password')
        if team_username.lower() == 'team' and team_password.lower() == 'team':
            return redirect('/team_profile/')
        else:
            return HttpResponse('Your Password or Username might be incorrect..!')
    return render(request, 'Management_Team/team_login.html')


# Management team profile

def team_profile(request):
    return render(request, 'Management_Team/team_profile.html')


# vendor login approval page

def vendor_login_approval(request):
    details = Vendor_Register.objects.filter(Login_Status=False)
    return render(request, 'Management_Team/vendor_login_approval.html', {'data': details})


# vendor approve for login

def vendor_approve_login(request, id):
    users = Vendor_Register.objects.get(id=id)
    users.Login_Status = True
    users.save()
    return redirect('/vendor_login_approval/')


# client_application

def client_application(request):
    details = project_register.objects.filter(Manager_Approval='Yes')
    return render(request, 'Management_Team/client_application.html', {'data': details})


# add details

def add_details(request, id):
    details = project_register.objects.get(id=id)
    if request.method == 'POST':
        get_location_test = request.POST.get('select_test')
        get_design_layout = request.FILES['file_upload']
        details.Location_Tested = get_location_test
        details.Design_layout = get_design_layout
        details.save()
        return redirect('/client_application/')
    return render(request, 'Management_Team/client_application.html', {'value': details})


# vendor selection page

def vendor_selection_page(request):
    quote = Vendor_Quotation.objects.filter(Q(Vendor_Selection='Unselected') | Q(Vendor_Selection='Rejected'))
    return render(request, 'Management_Team/vendor_selection.html', {'value': quote})


# vendor select

def vendor_select(request, id):
    quote = Vendor_Quotation.objects.get(id=id)
    quote.Vendor_Selection = 'Selected'
    quote.save()
    return redirect('/vendor_selection/')


# vendor Reject

def vendor_reject(request, id):
    quote = Vendor_Quotation.objects.get(id=id)
    quote.Vendor_Selection = 'Rejected'
    quote.save()
    return redirect('/vendor_selection/')


# vendor quotation

def vendor_quotation(request):
    quote = Vendor_Quotation.objects.filter(Vendor_Selection='Selected')
    return render(request, 'Management_Team/vendor_quotation.html', {'data': quote})


# project update

def team_project_update(request):
    details = project_register.objects.filter(Location_Tested='Yes')
    return render(request, 'Management_Team/team_project_update.html', {'value': details})


# updating quote details

def quote_details(request, id):
    project_detail = project_register.objects.get(id=id)
    if request.method == 'POST':
        get_vendor_quotation = request.POST.get('vendor_quote')
        project_detail.Vendor_Quotation = get_vendor_quotation
        project_detail.save()
        return redirect('/v_project_update/')
    return render(request, 'Management_Team/team_project_update.html', {'values': project_detail})


# project approved page on team profile

def project_approved_team(request):
    details = project_register.objects.filter(Manager_Approved='Yes')
    return render(request, 'Management_Team/man_project_approved.html', {'values': details})


# ------------------Vendor------------------
# Vendor login

def vendor_login(request):
    if request.method == 'POST':
        get_name = request.POST.get('vendor_username')
        get_password = request.POST.get('vendor_password')
        try:
            user = Vendor_Register.objects.get(Username=get_name, Password=get_password)
            if user.Login_Status:
                return redirect('/vendor_profile/')
            else:
                return HttpResponse('Your Account is still Verifying, please wait some time...')
        except Vendor_Register.DoesNotExist:
            return HttpResponse('Invalid Username or Password')
    return render(request, 'Vendor/vendor_login.html')


# Vendor register

def vendor_register(request):
    if request.method == 'POST':
        v_name = request.POST.get('vendor_name')
        v_email = request.POST.get('vendor_email')
        v_company = request.POST.get('vendor_company')
        v_mobile = request.POST.get('vendor_tel')
        v_username = request.POST.get('vendor_email')
        v_password = request.POST.get('vendor_password')
        users = Vendor_Register()
        users.Name = v_name
        users.Email = v_email
        users.Company = v_company
        users.Mobile = v_mobile
        users.Username = v_username
        users.Password = v_password
        users.save()
        return redirect('/vendor_login/')
    return render(request, 'Vendor/vendor_register.html')


# forget password

def vendor_forget_password(request):
    user_details = None
    if request.method == 'POST':
        if 'username_form' in request.POST:
            get_name = request.POST.get('username')
            try:
                user_details = Vendor_Register.objects.get(Username=get_name)
            except Vendor_Register.DoesNotExist:
                return HttpResponse('User not found')
        elif 'password_form' in request.POST:
            get_name = request.POST.get('username')
            get_password = request.POST.get('vendor_password')
            try:
                user_details = Vendor_Register.objects.get(Username=get_name)
                user_details.Password = get_password
                user_details.save()
                return redirect('/vendor_login/')
            except Vendor_Register.DoesNotExist:
                return HttpResponse('User not found')
    return render(request, 'Vendor/vendor_forget_password.html', {'data': user_details})


# vendor profile

def vendor_profile(request):
    return render(request, 'Vendor/vendor_profile.html')


# project Details

def project_details(request):
    details = project_register.objects.filter(Location_Tested='Yes')
    return render(request, 'Vendor/project_details.html', {'value': details})


# vendor project quotation

def vendor_project_quotation(request):
    quote = Vendor_Quotation.objects.filter(Vendor_Selection='Selected')
    return render(request, 'Vendor/vendor_project_quotation.html', {'data': quote})


# project Calculation

def project_calculation_page(request):
    details = project_register.objects.filter(Location_Tested='Yes')
    return render(request, 'Vendor/project_calculation.html', {'value': details})


# calculation page pop-up

def calculate_page(request, id):
    details = project_register.objects.get(id=id, Location_Tested='Yes')
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_company = request.POST.get('company')
        get_email = request.POST.get('email')
        get_project_type = request.POST.get('project_type')
        get_land_area = request.POST.get('land-area')
        get_floors = request.POST.get('floors')
        get_cement_price = request.POST.get('cement')
        get_sand_price = request.POST.get('sand')
        get_stone_price = request.POST.get('stone')
        get_brick_price = request.POST.get('brick')
        get_steel_price = request.POST.get('steel')
        get_paint_price = request.POST.get('paint')
        get_total_estimation = request.POST.get('total_estimation')
        vendor_quote = Vendor_Quotation()
        vendor_quote.Name = get_name
        vendor_quote.Company = get_company
        vendor_quote.Email = get_email
        vendor_quote.Project_Type = get_project_type
        vendor_quote.Land_Area_Sqft = get_land_area
        vendor_quote.Floors = get_floors
        vendor_quote.Cement_Price = get_cement_price
        vendor_quote.Sand_Price = get_sand_price
        vendor_quote.Stone_Price = get_stone_price
        vendor_quote.Brick_Price = get_brick_price
        vendor_quote.Steel_Price = get_steel_price
        vendor_quote.Paint_Price = get_paint_price
        vendor_quote.Total_Estimation = get_total_estimation
        vendor_quote.save()
        return redirect('/project_calculation/')
    return render(request, 'Vendor/project_calculation.html', {'data': details})


# project approved page on team profile

def v_project_approved(request):
    details = project_register.objects.filter(Manager_Approved='Yes')
    return render(request, 'Vendor/v_project_approved_page.html', {'values': details})
