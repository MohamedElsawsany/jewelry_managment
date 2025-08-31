from django.db import models
from authentication.models import User, SoftDeleteMixin


class Branch(SoftDeleteMixin):
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_branches')
    updated_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return self.name


class Vendor(SoftDeleteMixin):
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_vendors')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name


class Customer(SoftDeleteMixin):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_customers')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.phone}"


class Seller(SoftDeleteMixin):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='sellers')
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_sellers')
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.branch.name}"