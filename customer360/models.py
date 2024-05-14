from django.db import models

class Customer(models.Model):
    # Define fields for the Customer model
    id = models.AutoField(primary_key=True)  # AutoField for unique identifier
    name = models.CharField(max_length=100)  # CharField for name with maximum length 100
    email = models.EmailField(max_length=100)  # EmailField for email with maximum length 100
    phone = models.CharField(max_length=20)  # CharField for phone with maximum length 20
    address = models.CharField(max_length=200)  # CharField for address with maximum length 200
    social_media = models.CharField(max_length=100, blank=True)  # CharField for social media with maximum length 100 (optional)
    
    # String representation of the Customer model
    def __str__(self):
        return str(self.id)  # Return the id as string representation

class Interaction(models.Model):
    # Choices for the channel field
    CHANNEL_CHOICES = [
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('letter', 'Letter'),
        ('social_media', 'Social Media'),
    ]
    # Choices for the direction field
    DIRECTION_CHOICES = [
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]
    # Define fields for the Interaction model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey to Customer model, on_delete specifies what happens when related Customer is deleted
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)  # CharField for channel with predefined choices
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)  # CharField for direction with predefined choices
    interaction_date = models.DateField(auto_now_add=True)  # DateField for interaction date, auto_now_add sets the value to the current date automatically on creation
    summary = models.TextField()  # TextField for interaction summary