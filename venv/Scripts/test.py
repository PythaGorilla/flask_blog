import random
a=[3,1,2,10,5,6,7,6,9,4]


def bubble_sort(a):
	temp=0
	for i in xrange(0,9):		
		if a[i]<a[i+1]:
			pass
		temp=a[i+1]
		a[i+1]=a[i]
		a[i]=temp
	return a
print bubble_sort(a)