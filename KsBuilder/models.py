from django.db import models


# client registration for login.
class client_register(models.Model):
    DoesNotExist = None
    objects = None
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    Login_Status = models.BooleanField(default=False)


# Registration for project

class project_register(models.Model):
    # Choices
    objects = None
    PROJECT_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Villa', 'Villa'),
        ('Residential Building', 'Residential Building'),
        ('Industrial Building', 'Industrial Building'),
        ('Office', 'Office'),
    ]

    LAND_TYPE_CHOICES = [
        ('Agricultural Land', 'Agricultural Land'),
        ('Brownfield Land', 'Brownfield Land'),
        ('Contaminated land', 'Contaminated land'),
        ('Green Belt Land', 'Green Belt Land'),
        ('Greenfield Land', 'Greenfield Land'),
        ('Strategic Land', 'Strategic Land'),
    ]

    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Mobile = models.CharField(max_length=10)
    Project_Type = models.CharField(max_length=50, choices=PROJECT_TYPE_CHOICES)
    Land_Area_Sqft = models.DecimalField(max_digits=10, decimal_places=2)
    Land_Type = models.CharField(max_length=50, choices=LAND_TYPE_CHOICES)
    Floors = models.IntegerField()
    Manager_Approval = models.CharField(max_length=4, default="No")
    Location_Tested = models.CharField(max_length=4, default="No")
    Design_layout = models.FileField(default=None)
    Vendor_Quotation = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Manager_Quotation = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Other_costs = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Client_approved = models.CharField(max_length=4, default="No")
    Manager_Approved = models.CharField(max_length=4, default="No")
    Actual_Quotation = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Profit = models.DecimalField(max_digits=20, decimal_places=2, default=None)


# Vendor Register

class Vendor_Register(models.Model):
    objects = None
    DoesNotExist = None
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Company = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=10)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=8)
    Login_Status = models.BooleanField(default=False)


# Vendor Quotation

class Vendor_Quotation(models.Model):
    objects = None
    Name = models.CharField(max_length=30)
    Company = models.CharField(max_length=40)
    Email = models.EmailField(max_length=30)
    Land_Area_Sqft = models.DecimalField(max_digits=10, decimal_places=2)
    Floors = models.IntegerField()
    Cement_Price = models.DecimalField(max_digits=20, decimal_places=2)
    Sand_Price = models.DecimalField(max_digits=20, decimal_places=2)
    Stone_Price = models.DecimalField(max_digits=20, decimal_places=2)
    Brick_Price = models.DecimalField(max_digits=20, decimal_places=2)
    Steel_Price = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Paint_Price = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Total_Estimation = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    Vendor_Selection = models.CharField(max_length=20, default='Unselected')
    Project_Type = models.CharField(max_length=50, default=None)
