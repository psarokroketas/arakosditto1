import urllib
import urllib2
splitted_page=[]
terminate=1
x="True"
w="True"
while w=="True" :
    c = (raw_input("Enter zip code (only 5 numbers): "))
    try:
        int(c)
    except ValueError:
        w="True"
        print " You have to put numbers"
    else:
        w="False"
while x=="True":
	y = int(raw_input("Retype zipcode: "))   
	if y==int(c) :
		print "ok"
		x="False"
	else :
		print "you pressed diferent zipcodes"
		terminate=int(raw_input("To terminate programm press 0: ")) 
		if terminate==0:
			x="False"
if terminate==0 :
	print "The programm has been terminated"
else :	
	request=urllib2.Request('http://www.uszip.com/zip/%s'%y)
	handle=urllib2.urlopen(request)
	content=handle.read()
	splitted_page=content.split("Total population")
	print "Population:",splitted_page[1].split("span",1)[0].replace("</dt><dd>","").replace("<","")
	splitted_page=content.split("Housing units")
	print "Housing units:",splitted_page[1].split("span",1)[0].replace("</dt><dd>","").replace("<","")
	splitted_page=content.split("Land area")
	print "Land area:",splitted_page[1].split("span")[2].replace("></dt><dd>","").replace("</dd><dt>Density<br><","")
	splitted_page=content.split("Density")
	print "Density:",splitted_page[1].split("span")[2].replace("></dt><dd>","").replace("<","")