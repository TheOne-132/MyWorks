#This is a code created to honour football.
#I am trying to virtually create random selections for clubs in the champions league format.
#I am starting from the quarter finals part.

import random
import time

tournament_history = {
    "Quarterfinals": [],
    "Semifinals": [],
    "Final": []
}

def store_match(stage, team1, team2, winner):
    tournament_history[stage].append({"Teams": f"{team1} vs {team2}", "Winner": winner})

#This function was actually the last function I created.
def dramatic_print(message, letter_delay=0.03, word_delay=0.2, line_delay=1.0):
    for line in message.split('\n'):
        for word in line.split():
            for letter in word:
                print(letter, end='', flush=True)
                time.sleep(letter_delay)
            print(' ', end='', flush=True)
            time.sleep(word_delay)
        print()
        time.sleep(line_delay)

#After asking questions and learning and unlearning, I was finally able to define this function.
def simulate_score():
    chances = random.randint(3, 8)
    goals = 0
    for _ in range(chances):
        if random.random() < random.uniform(0.15, 0.35):
            goals += 1
    return goals

#This function was the first function I created.
def clublist():
    global tournament_history
    tournament_history = {key: [] for key in tournament_history}
    
    while True:
        ucl_clubs = []
        dramatic_print("🏆 Welcome to the UEFA Champions League Simulator!")
        dramatic_print("Please enter 8 unique clubs for your simulation")

        while len(ucl_clubs) < 8:
            club = input(f"Enter club {len(ucl_clubs) + 1}: ").strip().title()
            if not club:
                print("Club name cannot be empty. Try again.")
            elif club in ucl_clubs:
                print("This club is already added. Enter a different club.")
            else:
                ucl_clubs.append(club)

        while True:
            random.shuffle(ucl_clubs)
            dramatic_print(f"\n 🎲 These are the clubs that made it to the quarter-finals:\n{ucl_clubs}")
            loop = input("Are you satisfied with your clublist? (yes / reshuffle / restart): ").strip().lower()
            if loop == "yes":
                break
            elif loop == "reshuffle":
                continue
            elif loop == "restart":
                return "restart"
            else:
                print("Please respond with 'yes', 'reshuffle', or 'restart'.")

        quarterfinal(ucl_clubs)
        return "finished"

def quarterfinal(clubs):
    print()
    dramatic_print("=== Quarterfinal Matchups and Results (Home and Away) ===")
    winners = []

    for i in range(0, len(clubs), 2):
        team1 = clubs[i]
        team2 = clubs[i+1]

        score1_leg1 = simulate_score()
        score2_leg1 = simulate_score()
        dramatic_print(f"First Leg: {team1} {score1_leg1} - {score2_leg1} {team2}")

        score2_leg2 = simulate_score()
        score1_leg2 = simulate_score()
        dramatic_print(f"Second Leg: {team2} {score2_leg2} - {score1_leg2} {team1}")

        total1 = score1_leg1 + score1_leg2
        total2 = score2_leg1 + score2_leg2

        away1 = score1_leg2
        away2 = score2_leg1
        
        dramatic_print(f"Aggregate: {team1} {total1} - {total2} {team2}")

        if total1 > total2:
            winner = team1
        elif total2 > total1:
            winner = team2
        else:
            if away1 > away2:
                dramatic_print(f"{team1} qualifies on away goals")
                winner = team1
            elif away2 > away1:
                dramatic_print(f"{team2} qualifies on away goals")
                winner = team2
            else:
                dramatic_print("The tie is level on aggregate and away goals! They're going to penalties...")
                winner = random.choice([team1, team2])
                dramatic_print(f"{winner} wins on penalties")

        store_match("Quarterfinals", team1, team2, winner)
        winners.append(winner)
        print()

    dramatic_print(f" 🎲 The clubs advancing to the semifinals are: {winners}")
    loop = input("Do you want to continue simulating? (yes/no): ").strip().lower()
    if loop == "no":
        return
    else:
        random.shuffle(winners)
        semifinal(winners)

def semifinal(clubs):
    print()
    dramatic_print("=== Semifinal Matchups and Results (Home and Away) ===")
    winners = []

    for i in range(0, len(clubs), 2):
        team1 = clubs[i]
        team2 = clubs[i+1]

        score1_leg1 = simulate_score()
        score2_leg1 = simulate_score()
        dramatic_print(f"First Leg: {team1} {score1_leg1} - {score2_leg1} {team2}")

        score2_leg2 = simulate_score()
        score1_leg2 = simulate_score()
        dramatic_print(f"Second Leg: {team2} {score2_leg2} - {score1_leg2} {team1}")

        total1 = score1_leg1 + score1_leg2
        total2 = score2_leg1 + score2_leg2

        away1 = score1_leg2
        away2 = score2_leg1

        dramatic_print(f"Aggregate: {team1} {total1} - {total2} {team2}")

        if total1 > total2:
            winner = team1
        elif total2 > total1:
            winner = team2
        else:
            if away1 > away2:
                dramatic_print(f"{team1} qualifies on away goals")
                winner = team1
            elif away2 > away1:
                dramatic_print(f"{team2} qualifies on away goals")
                winner = team2
            else:
                dramatic_print("The tie is level on aggregate and away goals! They're going to penalties...")
                winner = random.choice([team1, team2])
                dramatic_print(f"{winner} wins on penalties")

        store_match("Semifinals", team1, team2, winner)
        winners.append(winner)
        print()

    dramatic_print(f" 🎲 The clubs advancing to the finals are: {winners}")
    loop = input("Do you want to continue simulating? (yes/no): ").strip().lower()
    if loop == "no":
        return
    else:
        random.shuffle(winners)
        final(winners)

def final(clubs):
    print()
    dramatic_print("=== Final Matchup and Result ===")
    team1 = clubs[0]
    team2 = clubs[1]
    score1 = simulate_score()
    score2 = simulate_score()
    dramatic_print(f"{team1} {score1} - {score2} {team2}")

    if score1 > score2:
        winner = team1
    elif score2 > score1:
        winner = team2
    else:
        dramatic_print(f"It's a draw between {team1} and {team2}. They're going to penalties!")
        winner = random.choice([team1, team2])
        dramatic_print(f"{winner} wins on penalties")

    if winner.lower() == "arsenal":
        dramatic_print("Arsenal will never win the Champions League\nEven in a game!")
        dramatic_print("❌ Tournament Cancelled!")
        return 
    
    dramatic_print(f"\n 🎲 The winner of this tournament is: {winner}")
    dramatic_print(f"🥳🥳  {winner} are the Champions of Europe this season!🏆 ")
    print()
    store_match("Final", team1, team2, winner)

    display_tournament_history()

def display_tournament_history():
    dramatic_print("\n🏆 Tournament History 🏆\n")
    for stage, matches in tournament_history.items():
        dramatic_print(f"=== {stage} ===")
        for match in matches:
            dramatic_print(f"{match['Teams']} → Winner: {match['Winner']}")
        print()

while True:
    result = clublist()
    if result == "restart":
        continue

    loop = input("Do you want to play the UCL Simulator again? (yes/no): ").strip().lower()
    if loop != "yes":
        print()
        dramatic_print("Thanks for using the UCL Simulator")
        dramatic_print("TheOne made it!")
        break
