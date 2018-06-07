input urllib2

response = urllib2.urlopen('http://github.com/swissChili/ProjectLemming/Chrome.app')
app = response.read()
