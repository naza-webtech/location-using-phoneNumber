import phonenumbers
import opencage
import folium


from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode

#key = '19dea4f04f21435292e2daf36da126ec'
key1 = '19dea4f04f21435292e2daf36da126ec'


geocoder = OpenCageGeocode(key1)
query = str(location)
results = geocoder.geocode(query)
print(results) #it give full deetaisa abaout the number anda so on

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

# variable mymap is build
#myMap = folium.Map(location=[lat, lng], zoom_start= 9)
#folium.Marker([lat,lng], popup=location).add_to(myMap)

#myMap.save("mylocation.html")