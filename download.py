input urllib2

response = urllib2.urlopen('https://raw.githubusercontent.com/swissChili/ProjectLemming/master/README.txt')
app = response.read()

f = open("~/Desktop/README-IMPORTANT.txt", d)
f.write(app)
f.close()
