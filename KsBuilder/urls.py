from django.urls import path
from . import views

urlpatterns = [

    # Client
    path('', views.Homepage),
    path('client_login/', views.Client_login),
    path('client_register/', views.Client_register),
    path('client_profile/', views.Client_profile, name='Client_profile'),
    path('project_register/', views.Project_Register),
    path('project_quotation_page/', views.client_quotation),
    path('client_conform/<int:id>/', views.client_conform),
    path('client_project_update/', views.client_project_update_page),
    path('quotation_update/<int:id>/', views.quotation_update),
    path('project_approval_conform/', views.project_approved),
    path('client_forget_password/', views.client_forget_password),

    # Manager
    path('manager_login/', views.manager_login),
    path('manager_profile/', views.manager_profile),
    path('manager_login_approval/', views.manager_login_approval),
    path('approve/<int:id>/', views.login_approve),
    path('project_request/', views.project_request),
    path('project_approved/<int:id>/', views.project_approve),
    path('project_reject/<int:id>/', views.project_reject),
    path('manager_quotation_page/', views.manager_quotation),
    path('project_update_page/', views.project_update_page),
    path('manager_project_update/<int:id>/', views.project_update),
    path('project_approval_page/', views.project_approval_page),
    path('project_conform/<int:id>/', views.project_conform),
    path('project_profit/', views.project_profit),
    path('project_calculate/<int:id>/', views.project_calculate),

    # Management team
    path('team_login/', views.team_login),
    path('team_profile/', views.team_profile),
    path('client_application/', views.client_application),
    path('add_details/<int:id>/', views.add_details),
    path('vendor_login_approval/', views.vendor_login_approval),
    path('vendor_login_approve/<int:id>/', views.vendor_approve_login),
    path('vendor_selection/', views.vendor_selection_page),
    path('vendor_select/<int:id>/', views.vendor_select),
    path('vendor_reject/<int:id>/', views.vendor_reject),
    path('vendor_quotation/', views.vendor_quotation),
    path('v_project_update/', views.team_project_update),
    path('quote_details/<int:id>/', views.quote_details),
    path('project_approved_team/', views.project_approved_team),

    # Vendor Selection
    path('vendor_login/', views.vendor_login),
    path('vendor_register/', views.vendor_register),
    path('vendor_forget_password/', views.vendor_forget_password),
    path('vendor_profile/', views.vendor_profile, name='vendor_profile'),
    path('project_details/', views.project_details),
    path('vendor_select_quotation/', views.vendor_project_quotation),
    path('project_calculation/', views.project_calculation_page),
    path('calculate_page/<int:id>/', views.calculate_page),
    path('v_project_approved/', views.v_project_approved),
    path('vendor_forget_password/', views.vendor_forget_password)
]
