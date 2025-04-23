from pyexpat.errors import messages
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import messages
from .models import  usregister,addproduct,Feedback,shopowner,Transaction,Addcart,Order
from . import models

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def shophome(request):
    return render(request,'shophome.html')
def shopindex(request):
    return render(request,'shop.html')
def shopdbrd(request):
    return render(request,'shopdbrd.html')


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone_number=request.POST.get('phonenumber')
        gender=request.POST.get('gender')
        email=request.POST.get('email') 
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        image=request.FILES.get('image')
        if password==confirm_password:
            user=usregister(name=name,phone_number=phone_number,image=image,gender=gender,email=email,password=password,confirm_password=confirm_password)
            user.save()
            return redirect('login')
        return render(request,'register.html',{'error':'password is Invalid'})
    return render(request,'register.html')
def login(request):
    if request .method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cr=usregister.objects.filter(email=email,password=password)
        if cr:
            u=usregister.objects.get(email=email,password=password)
            email=u.email
            password=u.password
            request.session['email']=email
            request.session['password']=password
            return redirect ('home')
        return render(request,'login.html')
    return render(request,'login.html') 

def profile(request):
    if 'email' in request.session:
        email=request.session['email']
        user=usregister.objects.get(email=email) 
    return render(request,'profile.html',{'u':user})       
                
def edit_profile(request,eid):
    edit=usregister.objects.get(id=eid)
    if request.method =="POST":
        name=request.POST.get('name')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        edit.name=name
        edit.phone_number=phone_number
        edit.password=password
        if image is not None:
            edit.image=image
        im=edit.image
        edit.image=im
        edit.save()
        return redirect('profile')
    return render(request,'edit.html',{'edit':edit})
       

def user_list(request):
    users = usregister.objects.all() 
    return render(request, 'userlist.html', {'users': users})

def delete_user(request,did):
    x=usregister.objects.get (id=did)
    x.delete()
    return redirect('user_list')  
    
    

def adminindex(request):
    return render(request,'adminindex.html') 

def adminlog(request):
   if request .method=="POST":
       uname=request.POST.get('username')
       psword=request.POST.get('password')
       u='adminadvo'
       p='adv123'
       if uname==u:
            if psword==p:
                request.session['uname']=uname
                return redirect('adminindex')
       return render(request,'adminlogin.html')
   return render(request,'adminlogin.html')
from . models import shopowner
def shopregister(request):
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        shopid=request.POST.get('shopid')
        phone_number=request.POST.get('phonenumber')
        shopaddress=request.POST.get('shopaddress')
        place=request.POST.get('place')
        email=request.POST.get('email') 
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        shopimage=request.FILES.get('shopimage')
        licenceno=request.POST.get('licenceno')
        shopownername=request.POST.get('shopownername')
        age=request.POST.get('age')
        address=request.POST.get('address')

        if password==confirm_password:
            shopowner(shopname=shopname,shopid=shopid,phone_number=phone_number,shopaddress=shopaddress,place=place,shopimage=shopimage,licenceno=licenceno,shopownername=shopownername,age=age,address=address,email=email,password=password,confirm_password=confirm_password).save()
            return redirect('shoplogin')
        return render(request,'shopregister.html',{'error':'password error'})
    return render(request,'shopregister.html')
   

def shoplogin(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        cr=shopowner.objects.filter(email=email,password=password)
        if cr:
            u=shopowner.objects.get(email=email,password=password)
            email=u.email
            password=u.password
            request.session['email']=email
            request.session['password']=password
            return redirect ('shophome')
        return render(request,'shoplogin.html')
    return render(request,'shoplogin.html') 


import random
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import addproduct

def addproducts(request):
    if 'email' not in request.session:
        alert = "<script>alert('Please Login'); window.location.href='/shoplogin/'; </script>"
        return HttpResponse(alert)
    else:
        semail = request.session.get('email')

        if request.method == "POST":
            productname = request.POST.get('productname')
            category = request.POST.get('category')
            price = request.POST.get('price')
            size = request.POST.get('size')
            description = request.POST.get('description')
            stock = request.POST.get('stock')
            status = request.POST.get('status')
            image = request.FILES.get('image')
            gender=request.POST.get('gender')



            if not productname or not category or not price or not stock or not status:
                alert = "<script>alert('Please fill all the required fields'); window.location.href='/addproduct/'; </script>"
                return HttpResponse(alert)

            while True:
                product_id = random.randint(1000, 9999)
                if not addproduct.objects.filter(product_id=product_id).exists():
                    break

            try:
                pr = addproduct(
                    productname=productname,
                    category=category,
                    price=price,
                    size=size,
                    description=description,
                    stock=stock,
                    status=status,
                    image=image,
                    product_id=product_id,
                    email=semail,
                    gender=gender
                )
                pr.save()
                alert = "<script>alert('Added successfully'); window.location.href='/productmanage/'; </script>"
                return HttpResponse(alert)
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return render(request, 'addproduct.html')

        return render(request, 'addproduct.html')






from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import addproduct

def productmanage(request):
    if 'email' in request.session:
        email=request.session['email']
        products = addproduct.objects.filter(email=email)
        return render(request, 'productmanage.html', {'gt': products})
    return redirect('login')


def delete_product(request,id):
    pr=get_object_or_404(addproduct,id=id)
    pr.delete()
    return render(request,'shophome.html')
from django.shortcuts import render

def productlist(request):
    if 'email' in request.session:
        products=models.addproduct.objects.all()  
        return render(request,'productlist.html', {'gt': products})



def adminlist(request):
    br=addproduct.objects.all()
    return render(request,'adminlist.html',{'ht':br})

def deleteproduct(request,pid):
    pr=addproduct.objects.get(id=pid)
    pr.delete()
    return redirect('adminlist')

def productedit(request,eid):
    edit=addproduct.objects.get(id=eid)
    if request.method =="POST":
        productname=request.POST.get('productname')
        category=request.POST.get('category')
        price=request.POST.get('price') 
        size=request.POST.get('size')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        edit.productname=productname
        edit.category=category
        edit.price=price
        edit.size=size
        edit.description=description
        if image is not None:
            edit.image=image
        im=edit.image
        edit.image=im
        edit.save()
        return redirect('productmanage')
    return render(request,'productedit.html',{'edt':edit})

def feedback(request,tid):
    transaction=Transaction.objects.get(id=tid)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        rating=request.POST.get('rating')
        
        feed=models.Feedback(transaction=transaction, name=name, email=email, feedback=feedback, rating=rating)
        feed.save()
        return redirect('home')
    else:
        return render(request,'feedback.html')

def feedbacklist(request):
    br=Feedback.objects.all()
    return render(request,'feedbacklist.html',{'feed':br}) 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def add_cart(request, product_id):
    if 'email' in request.session:
        semail = request.session['email']
        user = models.usregister.objects.get(email=semail)
        product = models.addproduct.objects.get(id=product_id)

        if request.method == 'POST':
            quantity = int(request.POST.get('quantity'))
            total = product.price * quantity

            # Use defaults argument correctly
            cart_item, created = models.Addcart.objects.get_or_create(
                user=user,
                product=product,
                defaults={'quantity': quantity, 'total': total}
            )
            
            if not created:
                # If the item was already in the cart, update the quantity and total
                cart_item.quantity = quantity
                cart_item.total = product.price * quantity
                cart_item.save()

            return redirect('user_cart')
        
        else:
            return render(request, 'add_cart.html', {'prod': product})
    else:
        alert = "<script>alert('please login'); window.location.href='/login/';</script>"
        return HttpResponse(alert)

def user_cart(request):
    if 'email' in request.session:
        user = models.usregister.objects.get(email=request.session['email'])
        cart_items = models.Addcart.objects.filter(user=user)
        total_price = sum(item.total for item in cart_items)  # Corrected to cart_items
        return render(request, 'user_cart.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        alert = "<script>alert('please login'); window.location.href='/login/';</script>"
        return HttpResponse(alert)



#payment section

import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import usregister, addproduct, Addcart, Transaction
from decimal import Decimal

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def initiate_payment(request,cid):
    if 'email' in request.session:
        email = request.session.get('email')
        print(email)
        
        if email:
            try:
                # Get the product details
                product = Addcart.objects.get(id=cid)
                amount = int(product.total) * 100  # Razorpay expects the amount in paise (1 INR = 100 paise)

                # Create Razorpay order
                payment_order = client.order.create({
                    'amount': amount,
                    'currency': 'INR',
                    'payment_capture': '1'
                })
                order_id = payment_order['id']

                # Get user details
                user = models.usregister.objects.get(email=email)

                # Prepare buyer data to send with payment
                buyer_data = {
                    'buyer': {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'phone': user.phone_number,
                        'product_dtls': product.id  # Link product to buyer
                    }
                }

                # Return the Razorpay order details and buyer data
                response_data = {
                    'order_id': order_id,
                    'amount': amount,
                }
                response_data.update(buyer_data)

                return JsonResponse(response_data)

            except Addcart.DoesNotExist:
                return JsonResponse({'error': 'Product not found'}, status=404)
            except usregister.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

        return redirect('login')


# Confirm payment after Razorpay completes the payment
# def confirm_payment(request, order_id, payment_id, crti_id):
#     try:
#         # Fetch payment details
#         payment = client.payment.fetch(payment_id)
        
#         if payment['order_id'] == order_id and payment['status'] == 'captured':
#             pemail = payment.get('email')
#             amount = payment.get('amount')
#             crt_id = crti_id
            
#             # Convert amount to rupees
#             amount_in_rupees = Decimal(amount) / Decimal(100)
            
#             if pemail:
#                 # Fetch user and cart item details
#                 user = usregister.objects.get(email=pemail)
#                 cart_item = Addcart.objects.get(id=crt_id)
#                 product = cart_item.product 
#                 prd=addproduct.objects.get(id=cart_item.product.id) # Associated product

#                 # Create a transaction record
#                 transaction = Transaction(
#                     user=user,
#                     products=product,
#                     amount=amount_in_rupees,
#                     quantity=cart_item.quantity,
#                     order_id=order_id
#                 )
#                 transaction.save()
#                 q=prd.stock - cart_item.quantity
#                 prd.stock=q
#                 prd.save()

#                 # Remove the cart item after payment
#                 cart_item.delete()

#                 # Redirect to product list after payment success
#                 return redirect('productlist')
#             else:
#                 return JsonResponse({'status': 'failure', 'error': 'User email not found'})
#         else:
#             return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order ID mismatch'})

#     except Exception as e:
#         print('Error:', str(e))
#         return redirect('home')  # In case of error, redirect to the homepage



# Added Send mail function 
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import redirect

def confirm_payment(request, order_id, payment_id, crti_id):
    try:
        
        payment = client.payment.fetch(payment_id)
        
        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            crt_id = crti_id
            
            
            amount_in_rupees = Decimal(amount) / Decimal(100)
            
            if pemail:
                
                user = usregister.objects.get(email=pemail)
                cart_item = Addcart.objects.get(id=crt_id)
                product = cart_item.product
                
                prd = addproduct.objects.get(id=cart_item.product.id)
                
                
                transaction = Transaction(
                    user=user,
                    products=product,
                    amount=amount_in_rupees,
                    quantity=cart_item.quantity,
                    order_id=order_id
                )
                transaction.save()
                
                q = prd.stock - cart_item.quantity
                prd.stock = q
                prd.save()
                
                
                subject = 'Payment Confirmation - Order #{}'.format(order_id)
                message = f"""
                Dear {user.name},

                Thank you for your purchase! Your payment has been successfully processed.

                Order Details:
                - Order ID: {order_id}
                - Product: {product.productname}
                - Quantity: {cart_item.quantity}
                - Amount Paid: ₹{amount_in_rupees}

                Your order will be processed shortly.

                If you have any questions, please don't hesitate to contact us.

                Best regards,
                Your Store Team
                """
                
                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,  
                        [pemail],  
                        fail_silently=False,
                    )
                except Exception as email_error:
                    print('Email sending failed:', str(email_error))
                    
                
                
                cart_item.delete()
                
                return redirect('productlist')
            else:
                return JsonResponse({'status': 'failure', 'error': 'User email not found'})
        else:
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order ID mismatch'})
            
    except Exception as e:
        print('Error:', str(e))
        return redirect('home')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Addcart, id=cart_item_id)
    cart_item.delete()
    return redirect('user_cart')


from django.shortcuts import render, redirect
from .models import Transaction

def my_orders(request):
    if 'email' in request.session:
        semail = request.session['email']
        try:
            user = models.usregister.objects.get(email=semail)
        except models.usregister.DoesNotExist:
            return redirect('login')
        
        orders = Transaction.objects.filter(user=user).order_by('-created_at')
        return render(request, 'my_orders.html', {'orders': orders})
    return redirect('login')


    
def cancel_order(request, tid):
    tid = get_object_or_404(Transaction, id=tid)
    tid.delete()
    messages.success(request, "The product fund will be refunded in 2-3 days")
    return redirect('my_orders')


def imageupld(request):
    if 'email' in request.session:
        semail = request.session.get('email')
        if not semail:
            alert = "<script> alert('Please log in again.'); window.location.href='/userlogin/'; </script>"
            return HttpResponse(alert)
        
        if request.method == 'POST' and request.FILES.get('image'):
            image = request.FILES.get('image')
            models.fileupload.objects.create(
                image=image
                )
            return HttpResponse("<script> alert('File uploaded successfully!'); window.location.href='/home/'; </script>")
        return render(request,'imageupld.html')
    

def shoplist(request):
    sh=models.shopowner.objects.all()
    return render(request,'shoplist.html',{'sh':sh})

def shopdelete(request,sid):
    sh=models.shopowner.objects.get(id=sid)
    return redirect('shoplist')

def logout(request):
    request.session.flush()
    return redirect('index')

def sprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        shop=shopowner.objects.get(email=email) 
    return render(request,'sprofile.html',{'s':shop})

def orderlist(request):
    od=models.Order.objects.all()
    return render(request,'orderlist.html',{'od':od})

def plist(request):
    pr = models.addproduct.objects.filter(category__in=['watch', 'glass', 'cap'])
    print('products',pr)
    return render(request, 'plist.html', {'pr': pr})






# Try On

# from .utils import search_dresses  # assuming search_dresses is in utils.py

# def dress_search(request):
#     if request.method == 'POST':
#         style = request.POST.get('style')
#         gender = request.POST.get('gender')
#         api_key = settings.SEPAPI_KEY
        
#         # Pass gender to search_dresses
#         dresses = search_dresses(style, api_key, gender)
        
#         return render(request, 'dress_results.html', {'dresses': dresses})
    
#     return render(request, 'dress_search.html')

# tryon/views.py
# import http.client
# import os
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import requests
# from django.conf import settings
# # tryon/views.py
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# import requests
# import os
# from django.conf import settings


import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name=settings.CLOUDINARY_CLOUD_NAME,
  api_key=settings.CLOUDINARY_API_KEY,
  api_secret=settings.CLOUDINARY_API_SECRET,
)

def upload_to_cloudinary(image_file):
    # Perform transformation (resize to 1280x1920 and convert to .jpg)
    response = cloudinary.uploader.upload(
        image_file,
        transformation=[
            {'width': 1280, 'height': 1920, 'crop': 'fill', 'format': 'jpg'}
        ]
    )
    print("Upload", response)
    return response['secure_url']

# def try_on_page(request):
#     dress_url = request.GET.get('dress_url')
#     print('hi',dress_url)
#     if request.method == 'POST':
#         avatar_image = request.FILES.get('avatar_image')
#         print('hello',avatar_image)
        
#         if not dress_url or not avatar_image:
#             return JsonResponse({'error': 'Both dress URL and avatar image are required.'}, status=400)

#         try:
#             avatar_url = upload_to_cloudinary(avatar_image)
#             print('Uploading', avatar_url)
            
#             # Proceed with the rest of your logic here
#             params = {
#                 'clothing_image_url': dress_url,
#                 'avatar_image_url': avatar_url
#             }
            
#             headers = {
#                 'Content-Type': 'application/x-www-form-urlencoded',
#                 'X-RapidAPI-Key': '9bd34ee83cmsh69c6bd12dc44d51p10a711jsnf37f1fc21a7e',
#                 'X-RapidAPI-Host': 'try-on-diffusion.p.rapidapi.com'
#             }

#             # Make the API request as before
#             response = requests.post(
#                 'https://try-on-diffusion.p.rapidapi.com/try-on-url',
#                 headers=headers,
#                 data=params
#             )
            
#             content_type = response.headers.get('Content-Type')
#             if content_type == 'image/jpeg':
#                 # Save the image result in media directory
#                 result_dir = os.path.join(settings.BASE_DIR, 'media', 'tryon')
#                 os.makedirs(result_dir, exist_ok=True)
#                 result_path = os.path.join(result_dir, 'result.jpg')

#                 with open(result_path, 'wb') as output_file:
#                     output_file.write(response.content)
                
#                 # Use relative URL for media file
#                 result_image_url = f'/media/tryon/result.jpg'

#                 # Return the relative URL of the saved image
#                 return render(request, 'try_on_result.html', {'result_image': result_image_url})

#             elif content_type == 'application/json':
#                 print("herty")
#                 # Handle JSON error response
#                 response_json = response.json()
#                 print('drt',response_json)
#                 return JsonResponse({'error': response_json.get('error', 'Unknown error occurred')}, status=500)

#             else:
#                 print("fret")
#                 response_json = response.json()
#                 print(response_json)
#                 # Handle unexpected content types
#                 return JsonResponse({'error': 'Unexpected response format received.'}, status=500)
        
#         except requests.exceptions.RequestException as error:
#             return JsonResponse({'error': f'Network error occurred: {str(error)}'}, status=500)

#     return render(request, 'try_on_page.html', {'dress_url': dress_url})

import requests
import os
import time
def try_on_page(request):
    # Get available shirts and t-shirts
    products = addproduct.objects.filter(
        status='available',
        category__in=['tshirt', 'shirt','westernwear','casualwear','coat','gown']
    )
    
    selected_product_id = request.GET.get('product_id')
    selected_product = None
    
    if selected_product_id:
        try:
            selected_product = addproduct.objects.get(product_id=selected_product_id)
        except addproduct.DoesNotExist:
            pass

    if request.method == 'POST':
        avatar_image = request.FILES.get('avatar_image')
        product_id = request.POST.get('product_id')
        
        try:
            product = addproduct.objects.get(product_id=product_id)
            dress_url = request.build_absolute_uri(product.image.url)
            
            if not avatar_image:
                return JsonResponse({'error': 'Avatar image is required.'}, status=400)

            # Upload avatar to Cloudinary
            avatar_url = upload_to_cloudinary(avatar_image)
            dress_url = upload_to_cloudinary(product.image.file)
            print(f"Avatar URL: {avatar_url}")
            print(f"Dress URL: {dress_url}")
            
            # API request parameters
            params = {
                'clothing_image_url': dress_url,
                'avatar_image_url': avatar_url
            }
            
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-RapidAPI-Key': '9bd34ee83cmsh69c6bd12dc44d51p10a711jsnf37f1fc21a7e',
                'X-RapidAPI-Host': 'try-on-diffusion.p.rapidapi.com'
            }

            # Make API request
            response = requests.post(
                'https://try-on-diffusion.p.rapidapi.com/try-on-url',
                headers=headers,
                data=params
            )
            
            print(f"API Response Status: {response.status_code}")
            print(f"API Response Headers: {response.headers}")
            
            if response.status_code != 200:
                error_message = "API request failed"
                try:
                    error_data = response.json()
                    error_message = error_data.get('error', error_message)
                except:
                    pass
                return render(request, 'try_on_page.html', {
                    'products': products,
                    'error': error_message,
                    'selected_product': selected_product
                })

            content_type = response.headers.get('Content-Type', '')
            
            if 'image' in content_type.lower():
                # Save result image
                result_dir = os.path.join(settings.MEDIA_ROOT, 'tryon')
                os.makedirs(result_dir, exist_ok=True)
                timestamp = int(time.time())
                result_filename = f'result_{timestamp}.jpg'
                result_path = os.path.join(result_dir, result_filename)

                with open(result_path, 'wb') as output_file:
                    output_file.write(response.content)

                result_url = f'/media/tryon/{result_filename}'
                return render(request, 'try_on_result.html', {
                    'result_image': result_url,
                    'product': product
                })
            else:
                error_message = "Invalid response format"
                try:
                    error_data = response.json()
                    error_message = error_data.get('error', error_message)
                except:
                    pass
                return render(request, 'try_on_page.html', {
                    'products': products,
                    'error': error_message,
                    'selected_product': selected_product
                })

        except addproduct.DoesNotExist:
            return render(request, 'try_on_page.html', {
                'products': products,
                'error': 'Selected product not found',
                'selected_product': selected_product
            })
        except Exception as e:
            print(f"Error: {str(e)}")
            return render(request, 'try_on_page.html', {
                'products': products,
                'error': f'An error occurred: {str(e)}',
                'selected_product': selected_product
            })

    return render(request, 'try_on_page.html', {
        'products': products,
        'selected_product': selected_product
    })

from django.shortcuts import render
from .models import addproduct, shopowner
import random
from django.http import HttpResponse
from django.contrib import messages

def admin_addproduct(request):
    # Check if the user is logged in
    if 'uname' not in request.session:
        alert = "<script>alert('Please Login'); window.location.href='/adminlogin/'; </script>"
        return HttpResponse(alert)
    
    # Get all shop owners from the shopowner table
    shops = shopowner.objects.all()

    if request.method == "POST":
        productname = request.POST.get('productname')
        category = request.POST.get('category')
        price = request.POST.get('price')
        size = request.POST.get('size')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        gender = request.POST.get('gender')
        shop_email = request.POST.get('shop_email')  # Get the shop email

        # Validate required fields
        if not productname or not category or not price or not stock or not status or not shop_email:
            alert = "<script>alert('Please fill all the required fields'); window.location.href='/admin_addproduct/'; </script>"
            return HttpResponse(alert)

        # Generate unique product_id
        while True:
            product_id = random.randint(1000, 9999)
            if not addproduct.objects.filter(product_id=product_id).exists():
                break

        try:
            # Create and save the new product
            pr = addproduct(
                productname=productname,
                category=category,
                price=price,
                size=size,
                description=description,
                stock=stock,
                status=status,
                image=image,
                product_id=product_id,
                email=shop_email,  # Store the shop's email in the product
                gender=gender
            )
            pr.save()

            alert = "<script>alert('Product added successfully'); window.location.href='/adminlist/'; </script>"
            return HttpResponse(alert)
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'admin_addproduct.html', {'shops': shops})

    return render(request, 'admin_addproduct.html', {'shops': shops})
