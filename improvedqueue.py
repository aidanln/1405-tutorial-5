# queue with optimized time complexity
# (thanks to the larger memory of a dictionary)
#
# by Aidan Lalonde-Novales

import random
import time

''' adds value to the end of the queue '''
def addend(list, dict, value):
	list.append(value)

	# check if the value is already in the dictionary
	if dict.get(value) is None:
		# if not, add value as a key, make a new position in queue corresponding to the list
		dict[value] = [len(list) - 1]
	else:
		# if so, append a new position in queue corresponding to the list
		dict[value].append(len(list) - 1)

''' removes the staring value from the queue and returns it '''
def removestart(list, dict):
	if len(list) == 0:
		return None
	
	# subtract 1 on each key's queue position, as position -1 will be removed
	for key in dict.keys():
		for index in range(len(dict[key])):
			dict[key][index] -= 1
	
	# remove the earliest queue position from the dictionary
	dict[list[0]].remove(-1)
	# if the key has no more queue positions, remove it from the dictionary
	if dict[list[0]] == []:
		del dict[list[0]]

	# return the removed value
	return list.pop(0)

''' return the value in the list '''
def containslinear(list, value):
	return value in list

''' return the value in the hash (dict) '''
def containshash(dict, value):
	if dict.get(value) is None:
		return False
	return True

list = []
hash = {}
addprob = 100
removeprob = 90
repeat = 50000
maxval = 500
searchlist = []
#randomly build the data by probabilistically adding/removing items to the list
#also generate a list of items to search for later
#also make sure that the dictionary search is returning the same result as the list search
for i in range(repeat):
	if random.randint(0,100) < addprob:
		addend(list, hash, random.randint(0,maxval))
	if random.randint(0,100) < removeprob:
		removestart(list, hash)
		
	searchlist.append(random.randint(0,maxval))
	
	searchnum = random.randint(0,maxval)
	
	if containslinear(list, searchnum) != containshash(hash, searchnum):
		print("Error: dictionary and list search returned different results")
		exit()

start = time.time()
for i in searchlist:
	containslinear(list, i)
end = time.time()
print("Linear time: ", (end-start))

start = time.time()
for i in searchlist:
	containshash(hash, i)
end = time.time()
print("Hash time: ", (end-start))