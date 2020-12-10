#task10
myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}

def calculateAverage(finalMarks):
	total = 0
	average = 0

	for key in finalMarks:
		total = total+finalMarks[key]
	average = total/len(finalMarks)
	return average

print(calculateAverage(myFinalMarks))

#task 11
csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}

print(csf.get('cw1-weight')*csf.get('cw1-mark')+csf.get('exam-weight')*csf.get('exam-mark'))

#slide 40
def histogram(s): 
	d = dict() 
	for c in s: 
		if c not in d: 
			d[c] = 1 
		else: 
			d[c] += 1 
	return d

def reverse_lookup(d, v):
	for k in d:
		if d[k]==v:
			return k
	raise LookupError()

h = histogram ('parrot')

key = reverse_lookup(h,1)
print(key)
