import csv
from os.path import exists as does_file_exist
col_name =["name", "score"]
default_rows= [['a', 55], ['b', 50] , ['c', 45], ['d',35], ['e',30]]
print("if file does not exist fill this default_rows= [['a', 55], ['b', 50] , ['c', 45], ['d',35], ['e',30]] ")
if does_file_exist("High_Score.csv"):

	with open("High_Score.csv", 'r') as game_high_score:
			high_score_csv= list(csv.reader(game_high_score))
			#print(high_score_csv)		
			
	high_score_csv.remove(high_score_csv[0])

	for scores in high_score_csv:
		scores[1] = int(scores[1])
else:
	#print(high_score_csv)
	with open("High_Score.csv", 'w') as High_Score_file:
		high_score_csv =csv.writer(High_Score_file)
		high_score_csv.writerow(col_name)
		high_score_csv.writerows(default_rows)
	
	with open("High_Score.csv", 'r') as game_high_score:
		high_score_csv= list(csv.reader(game_high_score))
	high_score_csv.remove(high_score_csv[0])
	for i in range(len(high_score_csv)):
		high_score_csv[i][1] = int(high_score_csv[i][1])
			
print(high_score_csv)

		#high_score_csv = high_score_csv.next()
	

print("---------------------******")
high_score_l = [ 55,50,45,35,30]

scorer_name = "tommy-0kit"
score = 40
# from tje game itself
#high_score_csv = [['tom', 55], ['kit', 50] , ['aba', 45], ['cat',35], ['dpg',30]]
print(high_score_csv)
#print(list(high_score_d[0].values()))
insert_position = -1 # last posotion
# find index to insert 

print(insert_position)
print(score)

for i in range(len(high_score_csv)):
	if score >= high_score_csv[i][1]:
		insert_position = i 
		break
print(insert_position)

#insert_position = 1		

print("______________________")

for j in range(1,5):
	
	if insert_position == len(high_score_csv) - 1:
		high_score_csv[insert_position][0] = scorer_name
		high_score_csv[insert_position][1] = score
		
	else:
		high_score_csv[len( high_score_csv) - j][0] = high_score_csv[len( high_score_csv ) - j - 1][0]
		high_score_csv[len( high_score_csv) - j][1] = high_score_csv[len( high_score_csv ) - j - 1][1]
		
		if len(high_score_csv) - j-1 == insert_position:
			high_score_csv[insert_position][0] = scorer_name
			high_score_csv[insert_position][1] = score
		
			break
		
print(high_score_csv)

with open("High_Score.csv", 'w') as High_Score_file:
		new_high_score = csv.writer(High_Score_file)
		new_high_score.writerow(col_name)
		new_high_score.writerows(high_score_csv)
		
with open("High_Score.csv", 'r') as game_high_score:
		high_score_csv = list(csv.reader(game_high_score))
print(high_score_csv)	

print("______________________")
print("______________________")
print("______________________")
for i in range(len(high_score_l)):
	if score >= high_score_l[i]:
		insert_position = i 
		break
print(insert_position)

#insert_position = 1		
for j in range(1,5):
	
	if insert_position == len(high_score_l) - 1:
		high_score_l[insert_position] = score
	else:
		high_score_l[len( high_score_l) - j] = high_score_l[len( high_score_l ) - j - 1] 
		if len(high_score_l) - j-1 == insert_position:
			high_score_l[insert_position] = score
			break
		
print(high_score_l)

