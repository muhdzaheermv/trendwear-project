from django.urls import path
from virtualfitting import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('edit/<int:eid>/',views.edit_profile,name='edit_profile'),
    path('userlist/', views.user_list, name='user_list'),
    path('delete_user/<int:did>/',views.delete_user,name='delete_user'),
    path('adminindex/', views.adminindex, name='adminindex'),
    path('adminlogin/', views.adminlog, name='adminlog'),
    path('adminlist/',views.adminlist,name='adminlist'),
    path('deleteproduct/<int:pid>/',views.deleteproduct,name='deleteproduct'),
    path('shopregister/', views.shopregister, name='shopregister'),
    path('shoplogin/', views.shoplogin, name='shoplogin'),
    path('shophome/',views.shophome,name='shophome'),
    path('shop/',views.shopindex,name='shopindex'),
    path('addproduct/',views.addproducts,name='addproduct'),
    path('delete/<int:id>/',views.delete_product,name='delete_product'),
    path('productlist/',views.productlist,name='productlist'),
    path('productedit/<int:eid>/',views.productedit,name='productedit'),
    path('feedback/<int:tid>/',views.feedback,name='feedback'),
    
    path('cancel_order/<int:tid>/',views.cancel_order,name='cancel_order'),
    
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('user_cart/', views.user_cart, name='user_cart'),
    path('shopdbrd/', views.shopdbrd, name='shopdbrd'),
    path('productmanage/',views.productmanage,name='productmanage'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('initiate_payment/<int:cid>/', views.initiate_payment, name='initiate_payment'),
    path('confirm-payment/<str:order_id>/<str:payment_id>/<int:crti_id>/', views.confirm_payment, name='confirm_payment'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('imageupld/',views.imageupld,name='imageupld'),
    path('shoplist/',views.shoplist,name='shoplist'),
    path('shopdelete/<int:sid>/',views.shopdelete,name='shopdelete'),
    path('logout/',views.logout,name='logout'),
    path('sprofile/',views.sprofile,name='sprofile'),
    path('orderlist/',views.orderlist,name='orderlist'),
    path('plist/',views.plist,name='plist'),


    # path('dress_search/',views.dress_search, name='dress_search'),
    # path('dress-search/',views.dress_search, name='dress_search'),
    path('try_on_page/',views.try_on_page, name='try_on_page'),
    path('admin_addproduct/', views.admin_addproduct, name='admin_addproduct'),



]