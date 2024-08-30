from django.urls import path
from .views import home, male_clothing, female_clothing, match_clothing

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('male/', male_clothing, name='male_clothing'),  # Male clothing page
    path('female/', female_clothing, name='female_clothing'),  # Female clothing page
    path('match/', match_clothing, name='match_clothing'),  # Matching page
]
