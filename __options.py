import random

global fatquotes
global namereplace
namereplace = "*[77687920776f756c64207520646f2074686973]*"
fatquotes = [
	"%s is fat lmao\n" % namereplace,
	"%s has a double chin lmao\n" % namereplace,
	"%s is like my mom\n" % namereplace,
	"%s is way too thicc\n" % namereplace,
	"%s needs to workout more\n" % namereplace,
	"%s can only roll down hills\n" % namereplace,
	"%s is so fat, McDonalds won't serve them\n" % namereplace,
	"%s is so fat, he's %s\n" % namereplace,
	"%s is round\n" % namereplace,
	"%s does not lift\n" % namereplace,
	"i just hate %s because he's fat\n" % namereplace

]

def fatgenerate(username):
	return fatquotes[int(random.uniform(0, len(fatquotes)))].replace(namereplace, username)
