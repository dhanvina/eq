from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from lab import views


router = routers.DefaultRouter()
router.register(r'Departments', views.DepartmentViewSet, basename='Department')
router.register(r'Labs', views.LabViewSet, basename='Lab')
router.register(r'PurchaseOrders', views.PurchaseOrderViewSet, basename='PurchaseOrder')
router.register(r'Equipments', views.EquipmentViewSet, basename='Equipment')
router.register(r'EquipmentIssues', views.EquipmentIssueViewSet, basename='EquipmentIssue')
router.register(r'labincharge', views.LabInChargeViewSet, basename='labIncharge')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', views.Login_api, name='login_api'),
]
