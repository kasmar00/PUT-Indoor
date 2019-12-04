import pygeoj
from copy import deepcopy

print("Please enter the name of input file: ", end="")
inp=input()
levels=[]
data=pygeoj.load(inp)
for i in data:
	if 'level' in i.properties:
		a=i.properties['level'].split(";")
		for j in a:
			if j not in levels:
				levels.append(j)
levels.sort()
print("levels are:", levels)
for l in levels:
	export=pygeoj.new()
	for i in data:
		if 'level' in i.properties:
			if l in i.properties["level"].split(";"):
				export.add_feature(deepcopy(i))

	for j in export:
		j.properties["level"]=l
	export.save(inp.split(".")[0]+"_level_"+l+".geojson")
	print("exported level:", l)

print("levels:",levels, "were saved to separate files named", inp.split(".")[0]+"_level_x")

export=pygeoj.new()
for i in data:
	if 'level' in i.properties:
		for j in i.properties["level"].split(";"):
			a=deepcopy(i)
			a.properties["level"]=j
			export.add_feature(a)
export.save(inp.split(".")[0]+"_split_on_levels.geojson")
	#if len(i.properties["level"].split(;))>1: