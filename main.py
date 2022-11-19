import ner
import pre
import pos
import csv
import re
import semantic_map
def event_num():
	user = []
	csv_no = -1
	l = []
	with open('input.csv',) as csvfile:
		csvreader = csv.DictReader(csvfile,delimiter='#')
		for row in csvreader:
			global l 	
			csv_no = csv_no + 1
			#print(row)
			word = row['Input']
			word = re.sub('[.,!"]','',word)	
			print (word)
			token = pre.pre_processing(word)
			print(token)
			part_of_speech = []
			part_of_speech = pos.pos_tagging(token)
			print(part_of_speech)
			#print(part_of_speech[0][1])
			#print(g)
			#print(g.startswith("NN"))
			ner_tag = ner.ner_tagging(part_of_speech)
			print(ner_tag)
			k = len(part_of_speech)
			i = 0
			flag1=0
			flag2=0
			while( i < k):
				g = part_of_speech[i][1]
				while( i < k and g.startswith("NN")):
					flag1 = 1
					g = part_of_speech[i][1]
					while(i < k ):
						g = part_of_speech[i][1]
						if(g.startswith("VB")):
							flag2 = 1
							break
						i = i + 1
					break
				if(flag1 == 1 and flag2 == 1):
					print("an event")
					print(csv_no)
					print(l)
					l.append(csv_no)
					break
				i = i + 1
	return l
