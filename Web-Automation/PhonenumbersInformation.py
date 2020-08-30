import phonenumbers
from phonenumbers import geocoder 
  
i=input("enter phn no")
   
phone_number = phonenumbers.parse(i)  

# Get Country Name
print("Country is....",geocoder.description_for_number(phone_number,'en'))    

#Get Service Provider Name

from phonenumbers import carrier 
  
   
service_provider = phonenumbers.parse(i) 

print("Service Provider is...",carrier.name_for_number(service_provider, 'en'))  