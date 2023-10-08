from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/',views.HomePageView,name='home'),
    path('regitser/',views.RegisterView.as_view(),name="register"),
    path('login',views.UserLogin.as_view(),name="login"),
    path('productslist/',views.ProjectListView.as_view(),name="productslist"),
    path('logout/',LogoutView.as_view(template_name='marketapp/logout.html',next_page='home'),name='logout'),
    path('addproject/',views.CreateProject.as_view(),name="addproject"),
    path('hostorcollab/',views.HostorCollab.as_view(),name="hostorcollab"),
    path('survey/<int:pk>',views.DataCollection.as_view(),name="survey"),
    path('productdetail/<int:pk>/',views.ProjDetail.as_view(),name="productdetail"),
]
