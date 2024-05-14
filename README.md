# Customer360 Project

Customer360 is a Django web application designed for managing customer interactions. It allows users to create and view customer profiles, record interactions with customers, and generate summaries of recent interactions.

## Installation

1. **Clone the repository:**
   git clone <repository-url>
   cd Customer360

2. **Install dependencies:**
    pip install -r requirements.txt

3. **Run migrations:**
    python manage.py migrate

## Usage

1. **Run the development server:**
    python manage.py runserver
    
2. **Access the application in your web browser at http://localhost:8000/.**

## Features
- Customer Management: Create, view, and manage customer profiles.
- Interaction Recording: Record interactions with customers, including the channel used, direction of communication, and summary.
- Interaction Summary: View summaries of interactions in the last 30 days, including counts by channel and direction.

## URL Configuration
The project's URL configuration (urls.py) maps URLs to views:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('create/', views.create_customer, name='create_customer'),
    path('interact/<int:cid>', views.interact, name='interact'),
    path('summary/', views.summary, name='summary'),
]