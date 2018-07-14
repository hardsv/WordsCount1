
#os import to delete temp files
import os
#timeit gives timre to get code execution time. Could remove it
from timeit import default_timer as timer


#time to check 
start = timer()

#check the word is present and add counter 
def word_if_present(word):
	with open('word_count_temp.txt','r+') as f1:
		word_found = False
		with open('deleteme.txt','a+') as f2:
			for line in f1:
				linetemp = line.split()
				if  (linetemp[0] == word) :
				#with open('deleteme.txt','a+') as f2:
					word_found = True
					# print('Found Word ' + word)
					linetemp[1] = str(int(linetemp[1]) + 1)
					f2.write(' '.join(linetemp) + '\n')
#					f2.close()
					# break
				else:
				#with open('deleteme.txt','a+') as f2:
					f2.write(line)
			f2.close()
	f1.close()
	os.remove('word_count_temp.txt')
	os.rename('deleteme.txt','word_count_temp.txt')
				
	if (not word_found):
		f3 =  open('word_count_temp.txt','a')
		f3.write(word + ' 1' + '\n')
		f3.close()


		
tempfilr = open('word_count_temp.txt','w+')
tempfilr.close()
tempfilr = open('deleteme.txt','w+')
tempfilr.close()

#with open('CEO.txt','r') as f:
#Edit the file name to open
with open('SampleTextFile_10kb.txt','r') as f:

	for line in f:
		for word in line.split():
			print(word)
			if word:
				word = word.lower()
				word_if_present(word)
			
f.close()

end = timer()

#print the excution time
print(end - start)
