from django.shortcuts import render
from datetime import date, timedelta
from django.db.models import Count
from .models import *

# View to display all customers
def index(request):
    # Retrieve all customers from the database
    customers = Customer.objects.all()
    # Prepare context data to pass to the template
    context = {"customers": customers}
    # Render the index.html template with the context data
    return render(request, "index.html", context=context)


# View to create a new customer
def create_customer(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve customer data from the form submitted by the user
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        social_media = request.POST["social_media"]
        # Create a new Customer object with the retrieved data
        customer = Customer.objects.create(
            name=name, email=email, phone=phone, address=address, social_media=social_media
        )
        # Save the customer object to the database
        customer.save()
        # Prepare a success message
        msg = "Successfully Saved a Customer"
        # Render the add.html template with the success message
        return render(request, "add.html", context={"msg": msg})
    # If the request method is not POST, render the add.html template
    return render(request, "add.html")


# View to display interaction summary
def summary(request):
    # Calculate the date 30 days ago
    thirty_days_ago = date.today() - timedelta(days=30)
    # Query interactions that occurred within the last 30 days
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)
    # Count the total number of interactions
    count = len(interactions)
    # Group interactions by channel and direction and annotate with counts
    interactions = interactions.values("channel", "direction").annotate(count=Count("channel"))
    # Prepare context data to pass to the template
    context = {"interactions": interactions, "count": count}
    # Render the summary.html template with the context data
    return render(request, "summary.html", context=context)


# View to handle interactions with a specific customer
def interact(request, cid):
    # Retrieve available channels and directions from the Interaction model
    channels = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES
    # Prepare context data to pass to the template
    context = {"channels": channels, "directions": directions}
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve customer and interaction data from the form submitted by the user
        customer = Customer.objects.get(id=cid)
        channel = request.POST["channel"]
        direction = request.POST["direction"]
        summary = request.POST["summary"]
        # Create a new Interaction object with the retrieved data
        interaction = Interaction.objects.create(
            customer=customer, channel=channel, direction=direction, summary=summary
        )
        # Save the interaction object to the database
        interaction.save()
        # Add a success message to the context
        context["msg"] = "Interaction Success"
        # Render the interact.html template with the context data
        return render(request, "interact.html", context=context)
    # If the request method is not POST, render the interact.html template
    return render(request, "interact.html", context=context)
    