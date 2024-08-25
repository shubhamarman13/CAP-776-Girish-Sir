# Function to display the welcome message
def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all cricket related things...!" + "|")
    print("+" + "-"*38 + "+")
    print()

# Function to display the main menu
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

# Function to display the teams menu
def display_teams_menu():
    print("\nTeams Menu:")
    print("1. International Teams")
    print("2. Domestic Teams")
    print("3. Back to Main Menu")

# Function to display stats (Most Runs and Most Wickets)
def display_stats(most_runs, most_wickets):
    # Most Runs
    print("\nMost Runs:")
    print("|" + "-"*81 + "|")
    print("| Player                  | Matches | Innings | Runs   | Avg   | SR    | 4s   | 6s   |")
    print("|-------------------------|---------|---------|--------|-------|-------|------|------|")
    for player, matches, innings, runs, avg, sr, fours, sixes in most_runs:
        print(f"| {player:<23} | {matches:>7} | {innings:>7} | {runs:>6} | {avg:>5.1f} | {sr:>5.1f} | {fours:>4} | {sixes:>4} |")

    # Most Wickets
    print("\nMost Wickets:")
    print("|" + "-"*77 + "|")
    print("| Player                  | Matches | Overs   | Balls  | Wkts  | Avg   | Runs  | 4-fers | 5-fers |")
    print("|-------------------------|---------|---------|--------|-------|-------|-------|--------|--------|")
    for player, matches, overs, balls, wkts, avg, runs, four_fers, five_fers in most_wickets:
        print(f"| {player:<23} | {matches:>7} | {overs:>7} | {balls:>6} | {wkts:>5} | {avg:>5.1f} | {runs:>5} | {four_fers:>6} | {five_fers:>6} |")
    
    print("+" + "-"*81 + "+")

# Function to display the full menu for a specific team
def display_team_menu(team_name, team_data):
    while True:
        print(f"\nTeam {team_name} Options:")
        print("1. Schedule")
        print("2. Result")
        print("3. Players")
        print("4. Stats")
        print("5. Back to Team Menu")

        team_option = input("Enter your choice (1-5): ").strip()

        if team_option == '1':
            print(f"\nDisplaying Schedule for Team {team_name}...")
            for date, match, venue, time in team_data["schedule"]:
                print(f"{date}: {match} at {venue} ({time})")
                
        elif team_option == '2':
            print(f"\nDisplaying Results for Team {team_name}...")
            for date, match, result in team_data["results"]:
                print(f"{date}: {match} - {result}")
                
        elif team_option == '3':
            print(f"\nDisplaying Players for Team {team_name}...")
            print("\nBATSMEN:")
            for player in team_data["players"]["batsmen"]:
                print(player)
            
            print("\nALL ROUNDER:")
            for player in team_data["players"]["all_rounders"]:
                print(player)
            
            print("\nWICKET KEEPER:")
            for player in team_data["players"]["wicket_keepers"]:
                print(player)
            
            print("\nBOWLER:")
            for player in team_data["players"]["bowlers"]:
                print(player)
            
        elif team_option == '4':
            display_stats(team_data["most_runs"], team_data["most_wickets"])

        elif team_option == '5':
            break  # Back to team menu

# Main program
def main():
    display_welcome_message()
    cricket_teams = {
        "India": {
            "schedule": [
                ("Sep 19, Thu - Sep 23, Mon", "India vs Bangladesh, 1st Test", "MA Chidambaram Stadium, Chennai", "04:00 AM GMT / 09:30 AM LOCAL"),
                ("Sep 27, Fri - Oct 01, Tue", "India vs Bangladesh, 2nd Test", "Green Park, Kanpur", "04:00 AM GMT / 09:30 AM LOCAL"),
                ("Oct 06, Sun", "India vs Bangladesh, 1st T20I", "New Madhavrao Scindia Cricket Stadium, Gwalior", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 09, Wed", "India vs Bangladesh, 2nd T20I", "Arun Jaitley Stadium, Delhi", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 12, Sat", "India vs Bangladesh, 3rd T20I", "Rajiv Gandhi International Stadium, Hyderabad", "01:30 PM GMT / 07:00 PM LOCAL"),
                ("Oct 16, Wed - Oct 20, Sun", "India vs New Zealand, 1st Test", "M.Chinnaswamy Stadium, Bengaluru", "04:00 AM GMT / 09:30 AM LOCAL")
            ],
            "results": [
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
            ],
            "players": {
                "batsmen": [
                    "Virat Kohli", "Rohit Sharma", "Shikhar Dhawan", "Shubman Gill",
                    "Shreyas Iyer", "Manish Pandey", "Mayank Agarwal", "Prithvi Shaw",
                    "Cheteshwar Pujara", "Ajinkya Rahane", "Ruturaj Gaikwad"
                ],
                "all_rounders": [
                    "Hardik Pandya", "Hanuma Vihari", "Ravindra Jadeja", "Ravichandran Ashwin"
                ],
                "wicket_keepers": [
                    "KL Rahul", "Sanju Samson", "Wriddhiman Saha", "Rishabh Pant"
                ],
                "bowlers": [
                    "Mohammed Shami", "Jasprit Bumrah", "Kuldeep Yadav", "Yuzvendra Chahal",
                    "Navdeep Saini", "Shardul Thakur", "Umesh Yadav", "Mohammed Siraj"
                ]
            },
            "most_runs": [
        ("Sachin Tendulkar", 200, 329, 15921, 54.0, 54.0, 2058, 69),
        ("Rahul Dravid", 163, 284, 13265, 53.0, 43.0, 1652, 21),
        ("Sunil Gavaskar", 125, 214, 10122, 51.0, 66.0, 1016, 26),
        ("Virat Kohli", 113, 191, 8848, 49.0, 56.0, 991, 26),
        ("VVS Laxman", 134, 225, 8781, 46.0, 49.0, 1135, 5),
        ("Virender Sehwag", 103, 178, 8503, 49.0, 82.0, 1219, 90),
        ("Sourav Ganguly", 113, 188, 7212, 42.0, 51.0, 900, 57),
        ("Cheteshwar Pujara", 103, 176, 7195, 44.0, 44.0, 863, 16),
        ("Dilip Vengsarkar", 116, 185, 6868, 42.0, 60.0, 560, 17),
        ("Mohammad Azharuddin", 99, 147, 6215, 45.0, 63.0, 720, 19),
        ("Gundappa Viswanath", 91, 155, 6080, 42.0, 76.0, 616, 6),
        ("Kapil Dev", 131, 184, 5248, 31.0, 95.0, 587, 61),
        ("Ajinkya Rahane", 85, 144, 5077, 38.0, 50.0, 579, 35),
        ("MS Dhoni", 90, 144, 4876, 38.0, 59.0, 544, 78),
        ("Mohinder Amarnath", 69, 113, 4378, 43.0, 86.0, 330, 21),
        ("Gautam Gambhir", 58, 104, 4154, 42.0, 51.0, 517, 10),
        ("Rohit Sharma", 59, 101, 4138, 45.0, 57.0, 452, 84)
    ],
    "most_wickets": [
        ("Anil Kumble", 132, 6808, 40850, 619, 30.0, 18355, 31, 35),
        ("Ravichandran Ashwin", 100, 4361, 26166, 516, 24.0, 12255, 25, 36),
        ("Kapil Dev", 131, 4623, 27740, 434, 30.0, 12867, 17, 23),
        ("Harbhajan Singh", 103, 4763, 28580, 417, 32.0, 13537, 16, 25),
        ("Ishant Sharma", 105, 3193, 19160, 311, 32.0, 10078, 10, 11),
        ("Zaheer Khan", 92, 3131, 18785, 311, 33.0, 10247, 15, 11),
        ("Ravindra Jadeja", 72, 2872, 17233, 294, 24.0, 7096, 13, 13),
        ("Bishan Bedi", 67, 3441, 20650, 266, 29.0, 7637, 13, 14),
        ("Bhagwath Chandrasekhar", 58, 2550, 15299, 242, 30.0, 7199, 12, 16),
        ("Javagal Srinath", 67, 2517, 15104, 236, 30.0, 7196, 8, 10),
        ("Mohammed Shami", 64, 1919, 11515, 229, 28.0, 6346, 12, 6),
        ("Erapalli Prasanna", 49, 2262, 13575, 189, 30.0, 5742, 17, 10),
        ("Umesh Yadav", 57, 1496, 8979, 170, 31.0, 5263, 6, 3),
        ("Vinoo Mankad", 44, 2389, 14338, 162, 32.0, 5236, 10, 8),
        ("Jasprit Bumrah", 36, 1197, 7182, 159, 21.0, 3291, 4, 10)
    ]

        },
        "Australia": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "Australia vs New Zealand, 1st Test", "Gabba, Brisbane", "08:00 AM GMT / 06:00 PM LOCAL"),
                ("Sep 23, Mon - Sep 27, Fri", "Australia vs New Zealand, 2nd Test", "Adelaide Oval, Adelaide", "08:00 AM GMT / 06:00 PM LOCAL"),
                ("Oct 05, Sat", "Australia vs England, 1st T20I", "Sydney Cricket Ground, Sydney", "09:00 AM GMT / 07:00 PM LOCAL"),
                ("Oct 08, Tue", "Australia vs England, 2nd T20I", "Melbourne Cricket Ground, Melbourne", "09:00 AM GMT / 07:00 PM LOCAL"),
                ("Oct 11, Fri", "Australia vs England, 3rd T20I", "Perth Stadium, Perth", "09:00 AM GMT / 07:00 PM LOCAL")
            ],
            "results": [
                ("Aug 10, Sat", "Australia vs South Africa, 1st ODI", "South Africa won by 8 wickets"),
                ("Aug 07, Wed", "Australia vs South Africa, 2nd ODI", "Australia won by 4 wickets"),
                ("Jul 30, Tue", "Australia vs South Africa, 3rd ODI", "Australia won by 6 wickets"),
                ("Jul 25, Thu", "Australia vs South Africa, 4th ODI", "Match tied")
            ],
            "players": {
                "batsmen": [
                    "Steve Smith", "David Warner", "Marnus Labuschagne", "Usman Khawaja",
                    "Travis Head", "Will Pucovski", "Aaron Finch", "Matthew Renshaw"
                ],
                "all_rounders": [
                    "Mitchell Marsh", "Glenn Maxwell", "Marcus Stoinis", "James Faulkner"
                ],
                "wicket_keepers": [
                    "Alex Carey", "Josh Inglis"
                ],
                "bowlers": [
                    "Pat Cummins", "Mitchell Starc", "Josh Hazlewood", "Nathan Lyon",
                    "Adam Zampa", "Kane Richardson", "James Pattinson"
                ]
            },
            
    "most_runs": [
        ("Ricky Ponting", 168, 287, 13378, 52.0, 59.0, 1509, 73),
        ("Allan Border", 156, 265, 11174, 51.0, 41.0, 1161, 28),
        ("Steve Waugh", 168, 260, 10927, 51.0, 49.0, 1175, 20),
        ("Steven Smith", 109, 195, 9685, 57.0, 54.0, 1063, 54),
        ("David Warner", 112, 205, 8786, 45.0, 70.0, 1036, 69),
        ("Michael Clarke", 115, 198, 8643, 49.0, 56.0, 977, 39),
        ("Matthew Hayden", 103, 184, 8625, 51.0, 60.0, 1049, 82),
        ("Mark Waugh", 128, 209, 8029, 42.0, 52.0, 844, 41),
        ("Justin Langer", 105, 182, 7696, 45.0, 54.0, 912, 40),
        ("Mark Taylor", 104, 186, 7525, 44.0, 41.0, 727, 9),
        ("David Boon", 107, 190, 7422, 44.0, 41.0, 822, 2),
        ("Greg Chappell", 87, 151, 7110, 54.0, 54.0, 755, 16),
        ("Sir Donald Bradman", 52, 80, 6996, 100.0, 71.0, 681, 6),
        ("Michael Hussey", 79, 137, 6235, 52.0, 50.0, 685, 39),
        ("Adam Gilchrist", 96, 137, 5570, 48.0, 82.0, 677, 100)
    ],
    "most_wickets": [
        ("Shane Warne", 145, 6784, 40705, 708, 25.0, 17995, 48, 37),
        ("Glenn McGrath", 124, 4874, 29248, 563, 22.0, 12186, 28, 29),
        ("Nathan Lyon", 129, 5460, 32761, 530, 30.0, 16052, 24, 24),
        ("Mitchell Starc", 89, 2903, 17417, 358, 28.0, 9932, 20, 14),
        ("Dennis Lillee", 70, 2836, 17017, 355, 24.0, 8493, 23, 23),
        ("Mitchell Johnson", 73, 2667, 16001, 313, 28.0, 8891, 16, 12),
        ("Brett Lee", 76, 2755, 16531, 310, 31.0, 9554, 17, 10),
        ("Craig McDermott", 71, 2764, 16586, 291, 29.0, 8332, 17, 14),
        ("Josh Hazlewood", 70, 2429, 14577, 273, 25.0, 6778, 10, 12),
        ("Pat Cummins", 62, 2102, 12614, 269, 23.0, 6063, 16, 12),
        ("Jason Gillespie", 71, 2372, 14234, 259, 26.0, 6770, 8, 8),
        ("Richie Benaud", 63, 2729, 16374, 248, 27.0, 6704, 16, 16),
        ("Garth McKenzie", 60, 2631, 15785, 246, 30.0, 7328, 7, 16),
        ("Ray Lindwall", 61, 1971, 11828, 228, 23.0, 5251, 8, 12),
        ("Peter Siddle", 67, 2318, 13907, 221, 31.0, 6777, 8, 8),
        ("Clarrie Grimmett", 37, 2409, 14453, 216, 24.0, 5231, 7, 21),
        ("Merv Hughes", 53, 2047, 12285, 212, 28.0, 6017, 14, 7),
        ("Stuart MacGill", 44, 1873, 11237, 208, 29.0, 6038, 9, 12)
    ]


        },
        "England": {
            "schedule": [
                ("Sep 19, Thu - Sep 23, Mon", "England vs India, 1st Test", "Lord's, London", "10:00 AM GMT"),
                ("Sep 27, Fri - Oct 01, Tue", "England vs India, 2nd Test", "Old Trafford, Manchester", "10:00 AM GMT"),
                ("Oct 05, Sat", "England vs South Africa, 1st T20I", "The Rose Bowl, Southampton", "05:00 PM GMT"),
                ("Oct 08, Tue", "England vs South Africa, 2nd T20I", "Edgbaston, Birmingham", "05:00 PM GMT"),
                ("Oct 11, Fri", "England vs South Africa, 3rd T20I", "Trent Bridge, Nottingham", "05:00 PM GMT")
            ],
            "results": [
                ("Aug 12, Mon", "England vs Australia, 1st ODI", "England won by 2 runs"),
                ("Aug 15, Thu", "England vs Australia, 2nd ODI", "Australia won by 8 wickets"),
                ("Aug 18, Sun", "England vs Australia, 3rd ODI", "England won by 5 wickets"),
                ("Jul 20, Sat", "England vs Pakistan, 5th ODI", "England won by 11 runs"),
                ("Jul 17, Wed", "England vs Pakistan, 4th ODI", "Pakistan won by 2 wickets"),
                ("Jul 14, Sun", "England vs Pakistan, 3rd ODI", "England won by 5 runs")
            ],
            "players": {
                "batsmen": [
                    "Joe Root", "Ben Stokes", "Jos Buttler", "Jonny Bairstow",
                    "Ollie Pope", "Dom Sibley", "Rory Burns", "Haseeb Hameed"
                ],
                "all_rounders": [
                    "Ben Stokes", "Chris Woakes", "Sam Curran", "Moeen Ali"
                ],
                "wicket_keepers": [
                    "Jos Buttler", "Jonny Bairstow", "Ben Foakes"
                ],
                "bowlers": [
                    "James Anderson", "Stuart Broad", "Jofra Archer", "Mark Wood",
                    "Chris Woakes", "Sam Curran", "Olly Stone"
                ]
            },
            "most_runs": [
        ("Sir Alastair Cook", 161, 291, 12472, 45.0, 47.0, 1441, 11),
        ("Joe Root", 144, 263, 12131, 50.0, 57.0, 1312, 44),
        ("Graham Gooch", 118, 215, 8900, 43.0, 49.0, 1079, 25),
        ("Alec Stewart", 133, 235, 8463, 40.0, 49.0, 1121, 10),
        ("David Gower", 117, 204, 8231, 44.0, 51.0, 979, 10),
        ("Kevin Pietersen", 104, 181, 8181, 47.0, 62.0, 985, 81),
        ("Sir Geoff Boycott", 108, 193, 8114, 48.0, 40.0, 771, 8),
        ("Mike Atherton", 115, 212, 7728, 38.0, 37.0, 904, 4),
        ("Ian Bell", 118, 205, 7727, 43.0, 49.0, 918, 39),
        ("Sir Colin Cowdrey", 114, 188, 7624, 44.0, 131.0, 752, 13),
        ("Wally Hammond", 85, 140, 7249, 58.0, 97.0, 512, 27),
        ("Sir Andrew Strauss", 100, 178, 7037, 41.0, 49.0, 867, 10),
        ("Graham Thorpe", 100, 179, 6744, 45.0, 46.0, 778, 9),
        ("Ben Stokes", 105, 190, 6508, 36.0, 60.0, 759, 131),
        ("Jonny Bairstow", 100, 178, 6042, 36.0, 59.0, 721, 56)
    ],
    "most_wickets": [
        ("James Anderson", 188, 6673, 40037, 704, 26.0, 18627, 32, 32),
        ("Stuart Broad", 167, 5616, 33698, 604, 28.0, 16719, 28, 20),
        ("Sir Ian Botham", 102, 3550, 21303, 383, 28.0, 10878, 17, 27),
        ("Bob Willis", 90, 2700, 16201, 325, 25.0, 8190, 12, 16),
        ("Fred Trueman", 67, 2448, 14690, 307, 22.0, 6625, 19, 17),
        ("Derek Underwood", 86, 3464, 20784, 297, 26.0, 7674, 13, 17),
        ("Graeme Swann", 60, 2558, 15349, 255, 30.0, 7642, 14, 17),
        ("Brian Statham", 70, 2495, 14972, 252, 25.0, 6261, 9, 9),
        ("Matthew Hoggard", 67, 2318, 13909, 248, 31.0, 7564, 13, 7),
        ("Sir Alec Bedser", 51, 2425, 14554, 236, 25.0, 5876, 11, 15),
        ("Andy Caddick", 62, 2259, 13558, 234, 30.0, 6999, 9, 13),
        ("Darren Gough", 58, 1970, 11821, 229, 28.0, 6503, 14, 9),
        ("Steve Harmison", 62, 2198, 13192, 222, 32.0, 7091, 11, 8),
        ("Andrew Flintoff", 78, 2458, 14747, 219, 33.0, 7303, 10, 3),
        ("Moeen Ali", 68, 2101, 12610, 204, 37.0, 7612, 13, 5),
        ("Ben Stokes", 105, 1966, 11795, 203, 32.0, 6507, 8, 4)
    ]
        },
        "New Zealand": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "New Zealand vs South Africa, 1st Test", "Basin Reserve, Wellington", "10:00 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "New Zealand vs South Africa, 2nd Test", "Hagley Oval, Christchurch", "10:00 AM GMT"),
                ("Oct 05, Sat", "New Zealand vs Bangladesh, 1st T20I", "Eden Park, Auckland", "06:00 AM GMT"),
                ("Oct 08, Tue", "New Zealand vs Bangladesh, 2nd T20I", "Bay Oval, Mount Maunganui", "06:00 AM GMT"),
                ("Oct 11, Fri", "New Zealand vs Bangladesh, 3rd T20I", "Seddon Park, Hamilton", "06:00 AM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "New Zealand vs Pakistan, 1st ODI", "Pakistan won by 5 runs"),
                ("Aug 12, Mon", "New Zealand vs Pakistan, 2nd ODI", "New Zealand won by 2 wickets"),
                ("Aug 15, Thu", "New Zealand vs Pakistan, 3rd ODI", "New Zealand won by 6 wickets"),
                ("Jul 30, Tue", "New Zealand vs Sri Lanka, 1st T20I", "Sri Lanka won by 10 runs"),
                ("Jul 28, Sun", "New Zealand vs Sri Lanka, 2nd T20I", "New Zealand won by 35 runs"),
                ("Jul 25, Thu", "New Zealand vs Sri Lanka, 3rd T20I", "New Zealand won by 7 wickets")
            ],
            "players": {
                "batsmen": [
                    "Kane Williamson", "Ross Taylor", "Martin Guptill", "Tom Latham",
                    "Devdutt Padikkal", "Henry Nicholls", "James Neesham", "Will Young"
                ],
                "all_rounders": [
                    "James Neesham", "Mitchell Santner", "Kyle Jamieson", "Colin de Grandhomme"
                ],
                "wicket_keepers": [
                    "Tom Latham", "Blair Tickner"
                ],
                "bowlers": [
                    "Trent Boult", "Tim Southee", "Kyle Jamieson", "Matt Henry",
                    "Mitchell Santner", "Lockie Ferguson", "Ish Sodhi"
                ]
            },
            "most_runs": [
        ("Kane Williamson", 100, 176, 8743, 55.0, 51.0, 971, 24),
        ("Ross Taylor", 112, 196, 7684, 44.0, 59.0, 932, 55),
        ("Stephen Fleming", 111, 189, 7172, 40.0, 46.0, 917, 26),
        ("Brendon McCullum", 101, 176, 6453, 39.0, 65.0, 776, 107),
        ("Martin Crowe", 77, 131, 5444, 45.0, 45.0, 659, 27),
        ("Tom Latham", 80, 142, 5419, 40.0, 47.0, 617, 19),
        ("John Wright", 82, 148, 5334, 38.0, 36.0, 630, 10),
        ("Nathan Astle", 81, 137, 4702, 37.0, 50.0, 612, 39),
        ("Daniel Vettori", 112, 172, 4523, 30.0, 58.0, 557, 17),
        ("BJ Watling", 75, 117, 3790, 38.0, 43.0, 429, 8),
        ("Bev Congdon", 61, 114, 3448, 32.0, 79.0, 267, 12),
        ("Chris Cairns", 62, 104, 3320, 34.0, 57.0, 365, 87),
        ("Sir Richard Hadlee", 86, 134, 3124, 27.0, 67.0, 343, 33),
        ("Craig McMillan", 55, 91, 3116, 38.0, 55.0, 367, 54),
        ("Glenn Turner", 41, 73, 2991, 45.0, 74.0, 265, 0),
        ("Henry Nicholls", 56, 87, 2973, 37.0, 50.0, 322, 9),
    ],
    "most_wickets": [
    ("Daniel Vettori", 291, 2303, 13820, 297, 32, 9495, 7, 2),
    ("Kyle Mills", 170, 1371, 8230, 240, 27, 6485, 8, 1),
    ("Tim Southee", 161, 1346, 8075, 221, 34, 7447, 5, 3),
    ("Trent Boult", 114, 1030, 6180, 211, 24, 5146, 10, 6),
    ("Chris Harris", 250, 1778, 10667, 203, 38, 7613, 2, 1),
    ("Chris Cairns", 214, 1355, 8132, 200, 33, 6557, 3, 1),
    ("Jacob Oram", 160, 1152, 6911, 173, 29, 5048, 3, 2),
    ("Sir Richard Hadlee", 115, 1019, 6118, 158, 22, 3407, 1, 5),
    ("Shane Bond", 82, 716, 4295, 147, 21, 3070, 7, 4),
    ("Matt Henry", 82, 713, 4277, 141, 26, 3722, 10, 2),
    ("Ewen Chatfield", 114, 1011, 6065, 140, 26, 3618, 3, 1),
    ("Scott Styris", 188, 1019, 6114, 137, 35, 4839, 4, 1),
    ("Danny Morrison", 96, 764, 4586, 126, 28, 3470, 1, 2),
    ("Martin Snedden", 93, 754, 4525, 114, 28, 3237, 1, 0),
    ("Gavin Larsen", 121, 1061, 6368, 113, 35, 4000, 1, 0),
    ("Daryl Tuffey", 94, 722, 4333, 110, 32, 3534, 2, 0),
    ("Mitchell Santner", 104, 812, 4875, 107, 37, 3960, 0, 2),
    ("Chris Pringle", 64, 552, 3314, 103, 24, 2459, 2, 1),
    ("Nathan Astle", 223, 808, 4850, 99, 38, 3809, 1, 0),
    ("Lockie Ferguson", 65, 550, 3300, 99, 32, 3124, 2, 1),
    ("Lance Cairns", 78, 658, 3951, 89, 31, 2717, 2, 1)
]
        },
        "West Indies": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "West Indies vs Pakistan, 1st Test", "Queen's Park Oval, Port of Spain", "10:00 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "West Indies vs Pakistan, 2nd Test", "Sabina Park, Kingston", "10:00 AM GMT"),
                ("Oct 05, Sat", "West Indies vs Sri Lanka, 1st T20I", "Kensington Oval, Bridgetown", "08:00 PM GMT"),
                ("Oct 08, Tue", "West Indies vs Sri Lanka, 2nd T20I", "Warner Park, Basseterre", "08:00 PM GMT"),
                ("Oct 11, Fri", "West Indies vs Sri Lanka, 3rd T20I", "Sir Vivian Richards Stadium, North Sound", "08:00 PM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "West Indies vs South Africa, 1st ODI", "South Africa won by 7 wickets"),
                ("Aug 12, Mon", "West Indies vs South Africa, 2nd ODI", "West Indies won by 8 runs"),
                ("Aug 15, Thu", "West Indies vs South Africa, 3rd ODI", "South Africa won by 4 wickets"),
                ("Jul 30, Tue", "West Indies vs England, 1st T20I", "West Indies won by 12 runs"),
                ("Jul 28, Sun", "West Indies vs England, 2nd T20I", "England won by 6 wickets"),
                ("Jul 25, Thu", "West Indies vs England, 3rd T20I", "West Indies won by 5 runs")
            ],
            "players": {
                "batsmen": [
                    "Chris Gayle", "Kieron Pollard", "Evin Lewis", "Shimron Hetmyer",
                    "Nicholas Pooran", "Darren Bravo", "Jason Holder", "Roston Chase"
                ],
                "all_rounders": [
                    "Jason Holder", "Kieron Pollard", "Roston Chase", "Andre Russell"
                ],
                "wicket_keepers": [
                    "Nicholas Pooran", "Shai Hope"
                ],
                "bowlers": [
                    "Sunil Narine", "Jason Holder", "Kemar Roach", "Alzarri Joseph",
                    "Odean Smith", "Andre Russell", "Shannon Gabriel"
                ]
            },
            "most_runs": [
        ("Brian Lara", 131, 232, 11953, 52.0, 79.0, 1184, 34),
        ("Sir Vivian Richards", 121, 187, 8540, 50.0, 55.0, 784, 35),
        ("Shivnarine Chanderpaul", 164, 268, 10842, 45.0, 69.0, 1170, 30),
        ("Chris Gayle", 103, 162, 10480, 37.0, 91.0, 734, 22),
        ("Desmond Haynes", 116, 238, 7487, 42.0, 49.0, 948, 26),
        ("Sir Garfield Sobers", 93, 179, 8032, 57.0, 85.0, 1420, 26),
        ("Sir Clive Lloyd", 102, 188, 7515, 46.0, 70.0, 929, 19),
        ("Rohan Kanhai", 79, 139, 6331, 51.0, 43.0, 702, 14),
        ("Richie Richardson", 128, 224, 5655, 43.0, 78.0, 812, 19),
        ("Marlon Samuels", 71, 125, 5302, 44.0, 62.0, 548, 22),
        ("Kraigg Brathwaite", 54, 93, 3619, 40.0, 21.0, 362, 10),
        ("Sir Everton Weekes", 48, 114, 4455, 58.0, 32.0, 361, 7),
        ("Carl Hooper", 102, 169, 5462, 36.0, 60.0, 741, 20)
    ],
    "most_wickets": [
        ("Courtney Walsh", 132, 5002, 23621, 519, 28.0, 18120, 43, 15),
        ("Sir Curtly Ambrose", 98, 4051, 20565, 405, 25.0, 14308, 38, 22),
        ("Malcolm Marshall", 81, 3821, 17618, 376, 25.0, 12620, 31, 20),
        ("Joel Garner", 58, 2953, 13752, 259, 26.0, 10607, 22, 15),
        ("Michael Holding", 60, 2457, 11319, 249, 23.0, 7937, 19, 17),
        ("Fidel Edwards", 55, 1873, 8525, 166, 27.0, 6181, 13, 5),
        ("Shannon Gabriel", 55, 1804, 9524, 162, 32.0, 6827, 15, 4),
        ("Devendra Bishoo", 58, 2272, 12112, 152, 29.0, 7351, 11, 5),
        ("Sulieman Benn", 57, 2127, 10267, 144, 30.0, 6145, 7, 2),
        ("Ravi Rampaul", 64, 1990, 10235, 139, 31.0, 7103, 8, 4)
    ]
        },
        "South Africa": {
            "schedule": [
                ("Sep 15, Sun - Sep 19, Thu", "South Africa vs New Zealand, 1st Test", "Newlands, Cape Town", "09:30 AM GMT"),
                ("Sep 23, Mon - Sep 27, Fri", "South Africa vs New Zealand, 2nd Test", "SuperSport Park, Centurion", "09:30 AM GMT"),
                ("Oct 05, Sat", "South Africa vs Bangladesh, 1st T20I", "St George's Park, Port Elizabeth", "05:00 PM GMT"),
                ("Oct 08, Tue", "South Africa vs Bangladesh, 2nd T20I", "Kingsmead, Durban", "05:00 PM GMT"),
                ("Oct 11, Fri", "South Africa vs Bangladesh, 3rd T20I", "Wanderers Stadium, Johannesburg", "05:00 PM GMT")
            ],
            "results": [
                ("Aug 10, Sat", "South Africa vs Australia, 1st ODI", "South Africa won by 8 wickets"),
                ("Aug 12, Mon", "South Africa vs Australia, 2nd ODI", "Australia won by 4 wickets"),
                ("Aug 15, Thu", "South Africa vs Australia, 3rd ODI", "South Africa won by 6 wickets"),
                ("Jul 30, Tue", "South Africa vs Zimbabwe, 1st T20I", "South Africa won by 18 runs"),
                ("Jul 28, Sun", "South Africa vs Zimbabwe, 2nd T20I", "South Africa won by 10 runs"),
                ("Jul 25, Thu", "South Africa vs Zimbabwe, 3rd T20I", "South Africa won by 6 wickets")
            ],
            "players": {
                "batsmen": [
                    "Hashim Amla", "AB de Villiers", "Faf du Plessis", "Quinton de Kock",
                    "Rassie van der Dussen", "Temba Bavuma", "David Miller", "Aiden Markram"
                ],
                "all_rounders": [
                    "Andile Phehlukwayo", "Chris Morris", "Dwaine Pretorius", "Jean-Paul Duminy"
                ],
                "wicket_keepers": [
                    "Quinton de Kock", "Heinrich Klaasen"
                ],
                "bowlers": [
                    "Kagiso Rabada", "Lungi Ngidi", "Dale Steyn", "Anrich Nortje",
                    "Keshav Maharaj", "Tabraiz Shamsi", "Sisanda Magala"
                ]
            },
            "most_runs": [
        ("Jacques Kallis", 165, 278, 13206, 55.0, 46.0, 1477, 96),
        ("Hashim Amla", 124, 215, 9282, 47.0, 50.0, 1170, 14),
        ("Graeme Smith", 116, 203, 9253, 49.0, 60.0, 1164, 24),
        ("AB de Villiers", 114, 191, 8765, 51.0, 55.0, 1024, 64),
        ("Gary Kirsten", 101, 176, 7289, 45.0, 43.0, 922, 12),
        ("Herschelle Gibbs", 90, 154, 6167, 42.0, 50.0, 887, 47),
        ("Mark Boucher", 146, 204, 5498, 31.0, 50.0, 654, 20),
        ("Dean Elgar", 86, 152, 5347, 38.0, 48.0, 684, 26),
        ("Daryll Cullinan", 70, 115, 4554, 44.0, 49.0, 548, 25),
        ("Faf du Plessis", 69, 118, 4163, 40.0, 46.0, 516, 21),
        ("Shaun Pollock", 108, 156, 3781, 32.0, 53.0, 412, 35),
        ("Hansie Cronje", 68, 111, 3714, 36.0, 45.0, 409, 33),
        ("Ashwell Prince", 66, 104, 3665, 42.0, 44.0, 397, 13)
    ],
    "most_wickets": [
    ("Dale Steyn", 93, 3101, 18608, 439, 23, 10077, 27, 26),
    ("Shaun Pollock", 108, 4059, 24353, 421, 23, 9733, 23, 16),
    ("Makhaya Ntini", 101, 3472, 20834, 390, 29, 11242, 19, 18),
    ("Allan Donald", 72, 2586, 15519, 330, 22, 7344, 11, 20),
    ("Morne Morkel", 86, 2749, 16498, 309, 28, 8550, 18, 8),
    ("Kagiso Rabada", 64, 1964, 11788, 299, 22, 6603, 14, 14),
    ("Jacques Kallis", 165, 3362, 20172, 291, 33, 9497, 7, 5),
    ("Vernon Philander", 64, 1898, 11391, 224, 22, 5000, 8, 13),
    ("Keshav Maharaj", 52, 1679, 10075, 171, 31, 5264, 6, 9),
    ("Hugh Tayfield", 37, 1852, 11116, 170, 26, 4405, 5, 14),
    ("Paul Adams", 45, 1475, 8850, 134, 33, 4405, 5, 4),
    ("Trevor Goddard", 41, 1768, 10612, 123, 26, 3226, 2, 5),
    ("Andre Nel", 36, 1271, 7630, 123, 32, 3919, 4, 3),
    ("Peter Pollock", 28, 1034, 6206, 116, 24, 2806, 1, 9),
    ("Neil Adcock", 26, 918, 5507, 104, 21, 2195, 5, 5),
    ("Paul Harris", 37, 1468, 8809, 103, 38, 3901, 3, 3)
]

        }
    }
    
    
       

    while True:
        display_main_menu()
        option = input("Enter your choice (1-7): ").strip()

        if option == '1':
            print("Displaying Live Scores...")
            #

        elif option == '2':
            print("Displaying Schedule...")
           

        elif option == '3':
            print("Displaying News...")
            

        elif option == '4':
            print("Displaying Series...")
            

        elif option == '5':
            while True:
                display_teams_menu()
                team_option = input("Enter your choice (1-6): ").strip()

                if team_option == '1':
                    print("International Teams:")
                    for idx, team in enumerate(cricket_teams.keys(), 1):
                        print(f"{idx}. {team}")
                    
                    team_choice = input("Select a team by number: ").strip()
                    selected_team = list(cricket_teams.keys())[int(team_choice) - 1]
                    display_team_menu(selected_team, cricket_teams[selected_team])
                    
                elif team_option == '2':
                    print("Displaying Domestic Teams...in Maintaince")
                    teams = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Punjab Kings",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad"
]

                    for index, team in enumerate(teams, start=1):
                        print(index, team)
                    
                elif team_option == '3':
                    break  # Back to Main Menu

        elif option == '6':
            print("Displaying Rankings...")
            # You can add functionality to display rankings here

        elif option == '7':
            print("Thank you for using Cricbuzz! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
    
# Run the main program
main()
