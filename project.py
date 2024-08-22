def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all cricket related things...!" + "|")
    print("+" + "-"*38 + "+")
    print()

def display_main_menu():
    print("+" + "-"*38 + "+")
    print("|" + " " * 14 + "Cricbuzz Menu" + " " * 14 + "|")
    print("|" + " " * 38 + "|")
    print("| 1. Live Scores" + " " * 23 + "|")
    print("| 2. Schedule" + " " * 26 + "|")
    print("| 3. News" + " " * 30 + "|")
    print("| 4. Series" + " " * 28 + "|")
    print("| 5. Teams" + " " * 29 + "|")
    print("| 6. Rankings" + " " * 26 + "|")
    print("| 7. Exit" + " " * 31 + "|")
    print("+" + "-"*38 + "+")

def display_teams_menu():
    print("\nTeams Menu:")
    print("1. International Teams")
    print("2. Domestic Teams")
    print("3. Back to Main Menu")

def display_stats():
    # Most Runs
    print("\nMost Runs:")
    print("|" + "-"*81 + "|")
    print("| Player                  | Matches | Innings | Runs   | Avg   | SR    | 4s   | 6s   |")
    print("|-------------------------|---------|---------|--------|-------|-------|------|------|")
    most_runs = [
        ("Sachin Tendulkar", 200, 329, 15921, 54.0, 54.0, 2058, 69),
        ("Rahul Dravid", 163, 284, 13265, 53.0, 43.0, 1652, 21),
        ("Sunil Gavaskar", 125, 214, 10122, 51.0, 66.0, 1016, 26),
        ("Virat Kohli", 113, 191, 8848, 49.0, 56.0, 991, 26),
        ("VVS Laxman", 134, 225, 8781, 46.0, 49.0, 1135, 5),
        ("Virender Sehwag", 103, 178, 8503, 49.0, 82.0, 1219, 90),
        ("Sourav Ganguly", 113, 188, 7212, 42.0, 51.0, 900, 57),
        ("Cheteshwar Pujara", 103, 176, 7195, 44.0, 44.0, 863, 16),
        ("Dilip Vengsarkar", 116, 185, 6868, 42.0, 60.0, 560, 17),
        ("Mohammad Azharuddin", 99, 147, 6215, 45.0, 63.0, 720, 19)
    ]
    for player, matches, innings, runs, avg, sr, fours, sixes in most_runs:
        print(f"| {player:<23} | {matches:>7} | {innings:>7} | {runs:>6} | {avg:>5.1f} | {sr:>5.1f} | {fours:>4} | {sixes:>4} |")

    # Most Wickets
    print("\nMost Wickets:")
    print("|" + "-"*77 + "|")
    print("| Player                  | Matches | Overs   | Balls  | Wkts  | Avg   | Runs  | 4-fers | 5-fers |")
    print("|-------------------------|---------|---------|--------|-------|-------|-------|--------|--------|")
    most_wickets = [
        ("Anil Kumble", 132, 236, 18355, 619, 29.7, 1013, 5, 8),
        ("Kapil Dev", 131, 227, 12867, 434, 29.6, 1044, 5, 2),
        ("Harbhajan Singh", 103, 190, 12075, 417, 32.3, 1045, 5, 5),
        ("Ravichandran Ashwin", 72, 140, 7266, 365, 26.9, 1181, 6, 5),
        ("Zaheer Khan", 92, 165, 9681, 311, 32.1, 1121, 5, 8),
        ("Bishan Bedi", 67, 121, 5549, 266, 28.1, 849, 6, 1),
        ("Bhagwath Chandrasekhar", 58, 97, 4285, 242, 29.8, 673, 5, 2),
        ("Vinoo Mankad", 44, 79, 3571, 162, 24.1, 594, 5, 1),
        ("Javagal Srinath", 67, 121, 5154, 151, 34.1, 614, 5, 3),
        ("Ravindra Jadeja", 49, 93, 4216, 151, 28.0, 754, 5, 5)
    ]
    for player, matches, overs, balls, wkts, avg, runs, four_fers, five_fers in most_wickets:
        print(f"| {player:<23} | {matches:>7} | {overs:>7} | {balls:>6} | {wkts:>5} | {avg:>5.1f} | {runs:>5} | {four_fers:>6} | {five_fers:>6} |")
    
    print("+" + "-"*81 + "+")

def main():
    display_welcome_message()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '5':
            while True:
                display_teams_menu()
                sub_choice = input("Enter your choice (1-3): ").strip()
                
                if sub_choice == '1':
                    print("Displaying International Teams...")
                    print("1. India")
                    print("2. Australia")
                    print("3. England")
                    print("4. Pakistan")
                    print("5. South Africa")
                    print("6. New Zealand")
                    print("7. Sri Lanka")
                    print("8. West Indies")
                    print("9. Bangladesh")
                    print("10. Afghanistan")
                    
                    team_choice = input("\nSelect a team to view details (1-10): ").strip()
                    if team_choice == '1':  # India team selected
                        while True:
                            print("\nTeam India Options:")
                            print("1. Schedule")
                            print("2. Result")
                            print("3. Players")
                            print("4. Stats")
                            print("5. Back to Team Menu")
                            
                            team_option = input("Enter your choice (1-5): ").strip()
                            
                            if team_option == '1':
                                print("\nDisplaying Schedule for Team India...")
                                schedule = [
                                    ("Sep 19, Thu - Sep 23, Mon", "India vs Bangladesh, 1st Test", "MA Chidambaram Stadium, Chennai", "04:00 AM GMT / 09:30 AM LOCAL"),
                                    ("Sep 27, Fri - Oct 01, Tue", "India vs Bangladesh, 2nd Test", "Green Park, Kanpur", "04:00 AM GMT / 09:30 AM LOCAL"),
                                    ("Oct 06, Sun", "India vs Bangladesh, 1st T20I", "New Madhavrao Scindia Cricket Stadium, Gwalior", "01:30 PM GMT / 07:00 PM LOCAL"),
                                    ("Oct 09, Wed", "India vs Bangladesh, 2nd T20I", "Arun Jaitley Stadium, Delhi", "01:30 PM GMT / 07:00 PM LOCAL"),
                                    ("Oct 12, Sat", "India vs Bangladesh, 3rd T20I", "Rajiv Gandhi International Stadium, Hyderabad", "01:30 PM GMT / 07:00 PM LOCAL"),
                                    ("Oct 16, Wed - Oct 20, Sun", "India vs New Zealand, 1st Test", "M.Chinnaswamy Stadium, Bengaluru", "04:00 AM GMT / 09:30 AM LOCAL")
                                ]
                                for date, match, venue, time in schedule:
                                    print(f"{date}: {match} at {venue} ({time})")
                                    
                            elif team_option == '2':
                                print("\nDisplaying Results for Team India...")
                                results = [
                                    ("Aug 07, Wed", "Sri Lanka vs India, 3rd ODI", "Sri Lanka won by 110 runs"),
                                    ("Aug 04, Sun", "Sri Lanka vs India, 2nd ODI", "Sri Lanka won by 32 runs"),
                                    ("Aug 02, Fri", "Sri Lanka vs India, 1st ODI", "Match tied"),
                                    ("Jul 30, Tue", "India vs Sri Lanka, 3rd T20I", "Match tied (India won the super over)"),
                                    ("Jul 28, Sun", "Sri Lanka vs India, 2nd T20I", "India won by 7 wkts (2nd innings reduced to 8 ovs due to rain, DLS target 78)"),
                                    ("Jul 27, Sat", "India vs Sri Lanka, 1st T20I", "India won by 43 runs"),
                                    ("Jul 14, Sun", "India vs Zimbabwe, 5th T20I", "India won by 42 runs"),
                                    ("Jul 13, Sat", "Zimbabwe vs India, 4th T20I", "India won by 10 wkts"),
                                    ("Jul 10, Wed", "India vs Zimbabwe, 3rd T20I", "India won by 23 runs"),
                                    ("Jul 07, Sun", "India vs Zimbabwe, 2nd T20I", "India won by 100 runs")
                                ]
                                for date, match, result in results:
                                    print(f"{date}: {match} - {result}")
                                    
                            elif team_option == '3':
                                print("\nDisplaying Players for Team India...")
                                
                                print("\nBATSMEN:")
                                batsmen = [
                                    "Virat Kohli", "Rohit Sharma", "Shikhar Dhawan", "Shubman Gill",
                                    "Shreyas Iyer", "Manish Pandey", "Mayank Agarwal", "Prithvi Shaw",
                                    "Cheteshwar Pujara", "Ajinkya Rahane", "Ruturaj Gaikwad"
                                ]
                                for i, player in enumerate(batsmen, start=1):
                                    print(f"{i}. {player}")
                                
                                print("\nALL ROUNDER:")
                                all_rounders = [
                                    "Hardik Pandya", "Hanuma Vihari", "Ravindra Jadeja", "Ravichandran Ashwin"
                                ]
                                for i, player in enumerate(all_rounders, start=1):
                                    print(f"{i}. {player}")
                                
                                print("\nWICKET KEEPER:")
                                wicket_keepers = [
                                    "KL Rahul", "Sanju Samson", "Wriddhiman Saha", "Rishabh Pant"
                                ]
                                for i, player in enumerate(wicket_keepers, start=1):
                                    print(f"{i}. {player}")
                                
                                print("\nBOWLER:")
                                bowlers = [
                                    "Mohammed Shami", "Jasprit Bumrah", "Kuldeep Yadav", "Yuzvendra Chahal",
                                    "Navdeep Saini", "Shardul Thakur", "Umesh Yadav", "Mohammed Siraj"
                                ]
                                for i, player in enumerate(bowlers, start=1):
                                    print(f"{i}. {player}")
                                
                            elif team_option == '4':
                                display_stats()

                            elif team_option == '5':
                                break  # Back to team menu
                    
                elif sub_choice == '2':
                    print("Displaying Domestic Teams...")
                    # Add similar options for domestic teams if needed
                    
                elif sub_choice == '3':
                    break  # Back to main menu
                
        elif choice == '7':
            print("Exiting Cricbuzz... Goodbye!")
            break  # Exit the application
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":    
    main()

