from datetime import datetime
start_time = datetime.now()
def getBatsman(player):
	for person in all_players:
		if player in person:
			return person
def getBowler(player):
	for person in all_players:
		if player in person:
			return person
def scorecard():
	#made two lists which contain all the players of team India and team pakistan
	team_india = ['Rohit Sharma (c)', 'KL Rahul', 'Virat Kohli', 'Suryakumar Yadav', 'Dinesh Karthik (wk)', 'Hardik Pandya', 'Ravindra Jadeja', 'Bhuvneshwar Kumar', 'Avesh Khan', 'Yuzvendra Chahal', 'Arshdeep Singh']
	team_pakistan = ['Babar Azam (c)', 'Mohammad Rizwan (wk)', 'Fakhar Zaman', 'Iftikhar Ahmed', 'Khushdil Shah', 'Asif Ali', 'Shadab Khan', 'Mohammad Nawaz', 'Naseem Shah', 'Haris Rauf', 'Shahnawaz Dahani']
	global all_players
	all_players = team_india + team_pakistan
	#Dictionary containing details of innings1 and innings2
	#the total team run,wicket and balls are there inside dictionary.
	#other than above mentioned there is a bowling,batting and extras dictionary foe storing details of bowling,batting and extras details.
	inns1 = {'run': 0, 'wicket': 0, 'balls': 0, 'bowling': {player : {'run': 0, 'balls': 0, 'maiden': 0, 'wicket': 0, 'nb': 0, 'wide': 0} for player in team_india},'batting': {player : {'balls': 0,'run': 0, '4s': 0, '6s': 0, 'status': ''} for player in team_pakistan}, 'extras': {'bye': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'p': 0}, 'did_not_bat': team_pakistan.copy(), 'fall_of_wicket': [], 'powerplay': 0}
	inns2 = {'run': 0, 'wicket': 0, 'balls': 0, 'bowling': {player : {'run': 0, 'balls': 0, 'maiden': 0, 'wicket': 0, 'nb': 0, 'wide': 0} for player in team_pakistan},'batting': {player : {'balls': 0,'run': 0,'4s': 0, '6s': 0, 'status': ''} for player in team_india}, 'extras': {'bye': 0, 'nb': 0, 'lb': 0, 'wide': 0, 'p': 0}, 'did_not_bat': team_india.copy(), 'fall_of_wicket': [], 'powerplay': 0}
	run_initial=-1
	with open('india_inns2.txt', 'r') as innings2, open('pak_inns1.txt', 'r') as innings1:
		#reading the commentary text files
		commentary1 = innings1.readlines()
		commentary2 = innings2.readlines()
		for inns, lines in zip([inns1, inns2], [commentary1, commentary2]):	
			for info in [line for line in lines if line.strip()]:
				#finding the batsmans name from the lines
				batter = getBatsman(info.split(",")[0].split(" ", 1)[1].split("to")[1].strip())
				#removing batsman from the whole list of batsman if he came for batting
				if batter in inns['did_not_bat']:
					inns['did_not_bat'].remove(batter)
				#finding the bowler from commentary lines
				bowler = getBowler(info.split(",")[0].split(" ", 1)[1].split("to")[0].strip())
				#finding maiden over. If the runs remains same as that of initial runs, maiden over count is increased by 1
				if inns['bowling'][bowler]['balls']%6==1:
					run_initial=inns['bowling'][bowler]['run']
				if inns['bowling'][bowler]['balls']%6==0:
					if inns['bowling'][bowler]['run']==run_initial:
						inns['bowling'][bowler]['maiden']+=1	
				#finding the runs scored from commentary 
				runs = info.split(",")[1].strip()
				#if the commentary says no run, number of balls is increased by 1,
				#no.of balls faced by batsman is increased by 1, his batting status is not out and no.of bowls by bowlwer also increased by 1
				if runs == "no run":
					inns['balls']+=1
					inns['batting'][batter]['balls']+=1
					inns['batting'][batter]['status']="not out"
					inns['bowling'][bowler]['balls']+=1
				#when number of runs is 1,2 or other integers, the number of runs scored is added to the total, batsmans and bowlers dictionary
				elif runs.find('run')!= -1:
					for n in range(0,7):
						if runs == str(n)+" run":
							inns['balls'] += 1
							inns['run'] += n
							inns['bowling'][bowler]['run'] += n
							inns['bowling'][bowler]['balls'] += 1
							inns['batting'][batter]['run'] += n
							inns['batting'][batter]['balls'] += 1
							inns['batting'][batter]['status']="not out"
				#when the commentary says four, 4 runs is added
				elif runs == "FOUR":
					inns['balls'] += 1
					inns['run'] += 4
					inns['bowling'][bowler]['run'] += 4
					inns['bowling'][bowler]['balls'] += 1
					inns['batting'][batter]['run'] += 4
					inns['batting'][batter]['balls'] += 1
					inns['batting'][batter]['4s'] += 1
					inns['batting'][batter]['status']="not out"
				#when the commentary says six, 6 runs is added to the total runs
				elif runs == "SIX":
					inns['balls'] += 1
					inns['run'] += 6
					inns['bowling'][bowler]['run'] += 6
					inns['bowling'][bowler]['balls'] += 1					
					inns['batting'][batter]['run'] += 6
					inns['batting'][batter]['status']="not out"
					inns['batting'][batter]['balls'] += 1
					inns['batting'][batter]['6s'] += 1
from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

scorecard()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))