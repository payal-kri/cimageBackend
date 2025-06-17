from django.db import models


class userDetails(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(primary_key=True)
    mobile= models.IntegerField(unique=True)
    password= models.CharField(max_length=20)
    adress= models.CharField(max_length=100,null=True,blank=True)


MembershipName=      (
                          ("Silver","Silver"),
                          ("Gold","Gold"),
                          ("Plantinum","Platinum")

                      )
class membershipDetails(models.Model):
    membershipCategory=models.CharField(max_length=20, choices=MembershipName)
    membershipID=models.AutoField(primary_key=True)
    email=models.ForeignKey(userDetails,on_delete=models.CASCADE)
    validity=models.DateField()

class eventDetails(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName=models.CharField(max_length=50,unique=True)
    eventDescription=models.CharField(max_length=100)
    eventDate=models.DateTimeField()
    eventVenue=models.CharField(max_length=50)

class registrationDetails(models.Model):
    RegistrationId = models.AutoField(primary_key=True)
    eventId = models.ForeignKey(eventDetails, on_delete=models.CASCADE)
    email=models.ForeignKey(userDetails,on_delete=models.CASCADE)
