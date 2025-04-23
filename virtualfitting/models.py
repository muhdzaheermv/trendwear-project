from django.db import models # type: ignore

# Create your models here.
class usregister(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    gender_choices=(
        ('MALE','male'),
        ('FEMALE','female'),
    )
    gender=models.CharField(max_length=10,choices=gender_choices,null=True,blank=True)
    email=models.CharField(unique=True,max_length=50,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    confirm_password=models.CharField(max_length=10,null=True,blank=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    
    def __str__(self):
            return self.name


class shopowner(models.Model):
    shopname=models.CharField(max_length=50,null=True,blank=True)
    shopid= models.CharField(max_length=15,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    shopaddress=models.CharField(max_length=50,null=True,blank=True)
    place=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    confirm_password=models.CharField(max_length=10,null=True,blank=True)
    shopimage=models.ImageField(upload_to='shop/',null=True,blank=True)
    licenceno=models.IntegerField(null=True,blank=True)
    shopownername=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
            return self.shopname
    
    
    
    


    
class addproduct(models.Model):
    # productid=models.IntegerField(null=True,blank=True)
    productname=models.CharField(max_length=20,null=True,blank=True)
    CATEGORY_CHOICE = [
        ('tshirt','T-shirt'),
        ('shirt','Shirt'),
        ('shoes','Shoes'),
        ('westernwear','Westernwear'),
        ('watch','Watch'),
        ('glass','Glass'),
        ('cap','Cap'),
        ('casualwear','Casualwear'),
        ('jewellery','Jewellery'),
        ('coat','Coat'),
        ('gown','Gown'),
    ]
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICE)
    price=models.IntegerField(null=True,blank=True)
    size=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=225,null=True,blank=True)
    image=models.ImageField(upload_to='shop/',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    product_id=models.IntegerField(unique=True)
    stock=models.IntegerField(null=True,blank=True)

    status_choice=[
        ('available','Available'),
        ('out_of_stock','Out_of_stock'),
    ]
    status=models.CharField(max_length=20, choices=status_choice,default='available')
    email=models.CharField(max_length=50)
    gender_choices=(
        ('MALE','male'),
        ('FEMALE','female'),
    )
    gender=models.CharField(max_length=10,choices=gender_choices,null=True,blank=True)

    def __str__(self):
            return self.productname






class Addcart(models.Model):
    user = models.ForeignKey(usregister, on_delete=models.CASCADE)
    product = models.ForeignKey(addproduct, on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    total =models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
            return self.user

class Transaction(models.Model):
    user = models.ForeignKey(usregister, on_delete=models.CASCADE)
    products = models.ForeignKey(addproduct, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)
    order_id = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField()
    feedback=models.TextField()
    rating=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
            return self.name

class Order(models.Model):
    user = models.ForeignKey(usregister, on_delete=models.CASCADE)
    products = models.ManyToManyField(addproduct)
    payment_success = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')  # New field

    

class fileupload(models.Model):
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.image.name


























































