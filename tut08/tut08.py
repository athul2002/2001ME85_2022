from datetime import datetime
start_time = datetime.now()

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