import json
import urllib2
max=-10**3
name=""
#xrhsimpoihsa thn methodo search kai anazhthsa ena sygkekrimeno style (Belgian And French Origin Ales) gia na mou dwsei polla apotelesmata
url=urllib2.urlopen("https://api.brewerydb.com/v2/search?q=Belgian%20And%20French%20Origin%20Ales&type=beer&key=fec0b9bd7c6ea4f30145da0a544aed12&format=json")
apotelesma=json.load(url)
lekseis=raw_input("dwse lekseis xwrismenes me komma")
lekseis=lekseis.split(",")
for i in range(len(lekseis)):
    for k in apotelesma['data']:
        sum=0
        if 'description' in k:
         if lekseis[i] in k['description']:
            sum+=k['description'].count(lekseis[i])
         if 'description' in k['style']:
            if lekseis[i] in k['style']['description']:
             sum+=k['style']['description'].count(lekseis[i])
        if sum>max:
          max=sum
          name=k['name']
print "Symfwna me tis lekseis pou dwsate h katallhlh byra gia esas einai h :",name
