from django.urls import path
from finance.views import User_register, User_login, create_goal, get_goals , home, logout_view

app_name = "finance"
urlpatterns = [
    path('register/', User_register,name="register"),
    path('login/', User_login,name="login"),
    path('logout/', logout_view,name="logout"),
    path('create-goal/', create_goal,name="create_goal"),
    path('get-goals/', get_goals,name="get_goals"),
    path('home/', home,name="home"),
    
]