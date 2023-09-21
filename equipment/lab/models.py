from django.db import models


class Department(models.Model):
    department_number = models.CharField(max_length=10)
    department_name = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department_number}, {self.department_name}"

class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.lab_number}, {self.department.department_name}"  # Use department_name

class LabInCharge(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    lab_incharge_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.lab_incharge_name} (Lab Incharge)"

class Equipment(models.Model):
    equipment_serial_number = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    equipment_value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    invoice = models.ImageField(upload_to='invoices/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.equipment_serial_number}, {'Working' if self.status else 'Not Working'}"

class EquipmentIssue(models.Model):
    experiment = models.CharField(max_length=100)
    lab_incharge = models.ForeignKey(LabInCharge, on_delete=models.CASCADE, default=1)
    number_of_equipments = models.PositiveIntegerField()
    details = models.TextField()

    def __str__(self):
        return f"Equipment Issue ({self.experiment})"

class EquipmentReview(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField()
    lab_incharge = models.ForeignKey(LabInCharge, on_delete=models.CASCADE)
    not_working_quantity = models.PositiveIntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f"Review for {self.equipment.equipment_serial_number} on {self.date}"
    
class PurchaseOrder(models.Model):
    purchase_order_number = models.CharField(max_length=10, unique=True)
    purchase_date = models.DateField()
    supplier = models.CharField(max_length=200)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.purchase_order_number}, {self.purchase_date}"

class LabInchargeRegister(models.Model):
    lab_incharge = models.ForeignKey(LabInCharge, on_delete=models.CASCADE, default=1)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lab_incharge}, {self.email}"
    

class LabInchargeLogin(models.Model):
    email = models.ForeignKey(
        LabInchargeRegister,
        on_delete=models.CASCADE,
        related_name='lab_incharge_login_emails'  
    )
    password = models.ForeignKey(
        LabInchargeRegister,
        on_delete=models.CASCADE,
        related_name='lab_incharge_login_passwords' 
    )



    def __str__(self):
        return f"{self.email}, {self.password}"