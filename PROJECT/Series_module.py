def display_boxed_text(text, width=40):
    border = "*" * (width + 4)
    lines = text.split('\n')
    boxed_text = [border]
    for line in lines:
        boxed_text.append(f"* {line.ljust(width)} *")
    boxed_text.append(border)
    return '\n'.join(boxed_text)

def display_series_menu():
    while True:
        menu_text = (
            "Series Menu\n"
            "1. ICC Mens T20 World Cup 2024\n"
            "2. Indian Premier League 2024\n"
            "3. Exit"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-3): ")

        if choice == '1':
            MensT20()
        elif choice == '2':
            IPL()
        elif choice == '3':
            print(display_boxed_text("Exiting..."))
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_1(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_1()
        elif choice == '2':
            display_table_1()
        elif choice == '3':
            display_t20_blast_squads_1()
        elif choice == '4':
            display_stats_1()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_2(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_2()
        elif choice == '2':
            display_table_2()
        elif choice == '3':
            display_t20_blast_squads_1()
        elif choice == '4':
            display_stats_2()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def display_sub_menu_3(series_name):
    while True:
        menu_text = (
            f"{series_name} Sub-Menu\n"
            "1. Matches\n"
            "2. Table\n"
            "3. Squads\n"
            "4. Stats\n"
            "5. Back to Series Menu"
        )
        print(display_boxed_text(menu_text))

        choice = input("Select an option (1-5): ")

        if choice == '1':
            display_matches_3()
        elif choice == '2':
            display_table_3()
        elif choice == '3':
            display_ipl_squads()
        elif choice == '4':
            display_IPL_stats()
        elif choice == '5':
            break
        else:
            print(display_boxed_text("Invalid choice. Please try again."))

def MensT20():
    display_sub_menu_1("ICC Mens T20 World Cup 2024")

def IPL():
    display_sub_menu_3("Indian Premier League 2024")


def display_matches_1():
    matches = [
        ("1st Match", "Group A", "Lauderhill, Florida", "IND vs USA", "IND won by 8 wickets"),
        ("2nd Match", "Group A", "Edinburgh", "PAK vs CAN", "PAK won by 4 wickets"),
        ("3rd Match", "Group B", "Dubai", "AUS vs ENG", "AUS won by 6 runs"),
        ("4th Match", "Group B", "Dubai", "SCO vs NAM", "SCO won by 5 wickets"),
        ("5th Match", "Group C", "Abu Dhabi", "WI vs AFG", "WI won by 10 wickets"),
        ("6th Match", "Group C", "Abu Dhabi", "NZ vs UGA", "NZ won by 30 runs"),
        ("7th Match", "Group D", "Sharjah", "RSA vs BAN", "RSA won by 7 wickets"),
        ("8th Match", "Group D", "Sharjah", "SL vs NED", "SL won by 2 wickets"),
        ("9th Match", "Group D", "Sharjah", "NEP vs NED", "NED won by 5 wickets"),
        ("10th Match", "Group B", "Dubai", "ENG vs SCO", "ENG won by 12 runs"),
        ("Semi-Final 1", "Group Stage", "Dubai", "IND vs AFG", "IND won by 4 wickets"),
        ("Semi-Final 2", "Group Stage", "Dubai", "RSA vs WI", "RSA won by 6 wickets"),
        ("Final", "Group Stage", "Dubai", "IND vs RSA", "IND won by 8 wickets")
    ]
    print("\nMatch Details:")
    print(f"{'Match':<15} {'Stage':<15} {'Venue':<20} {'Teams':<15} {'Result':<20}")
    print("="*85)
    for match in matches:
        print(f"{match[0]:<15} {match[1]:<15} {match[2]:<20} {match[3]:<15} {match[4]:<20}")

def display_table_1():
    print("\nTable: T20 Blast 2024")

    # Super 8 Group 1
    print("\nSuper 8 Group 1")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'IND (Q)':<15} {3:<3} {3:<3} {0:<3} {0:<3} {6:<3} {+2.017:<5}")
    print(f"{'AFG (Q)':<15} {3:<3} {2:<3} {1:<3} {0:<3} {4:<3} {-0.305:<5}")
    print(f"{'AUS (E)':<15} {3:<3} {1:<3} {2:<3} {0:<3} {2:<3} {-0.331:<5}")
    print(f"{'BAN (E)':<15} {3:<3} {0:<3} {3:<3} {0:<3} {0:<3} {-1.709:<5}")

    # Super 8 Group 2
    print("\nSuper 8 Group 2")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'RSA (Q)':<15} {3:<3} {3:<3} {0:<3} {0:<3} {6:<3} {+0.780:<5}")
    print(f"{'ENG (Q)':<15} {3:<3} {2:<3} {1:<3} {0:<3} {4:<3} {+1.992:<5}")
    print(f"{'WI (E)':<15} {3:<3} {1:<3} {2:<3} {0:<3} {2:<3} {+0.686:<5}")
    print(f"{'USA (E)':<15} {3:<3} {0:<3} {3:<3} {0:<3} {0:<3} {-3.906:<5}")

    # Group D
    print("\nGroup D")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'RSA (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+0.470:<5}")
    print(f"{'BAN (Q)':<15} {4:<3} {3:<3} {1:<3} {0:<3} {6:<3} {+0.616:<5}")
    print(f"{'SL (E)':<15} {4:<3} {1:<3} {2:<3} {1:<3} {3:<3} {+0.863:<5}")
    print(f"{'NED (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-1.358:<5}")
    print(f"{'NEP (E)':<15} {4:<3} {0:<3} {4:<3} {1:<3} {1:<3} {-0.542:<5}")

    # Group C
    print("\nGroup C")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'WI (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+3.257:<5}")
    print(f"{'AFG (Q)':<15} {4:<3} {3:<3} {1:<3} {0:<3} {6:<3} {+1.835:<5}")
    print(f"{'NZ (E)':<15} {4:<3} {2:<3} {2:<3} {0:<3} {4:<3} {+0.415:<5}")
    print(f"{'UGA (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-4.510:<5}")
    print(f"{'PNG (E)':<15} {4:<3} {0:<3} {4:<3} {0:<3} {0:<3} {-2.107:<5}")

    # Group B
    print("\nGroup B")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'AUS (Q)':<15} {4:<3} {4:<3} {0:<3} {0:<3} {8:<3} {+2.791:<5}")
    print(f"{'ENG (Q)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+3.611:<5}")
    print(f"{'SCO (E)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+1.255:<5}")
    print(f"{'NAM (E)':<15} {4:<3} {1:<3} {3:<3} {0:<3} {2:<3} {-2.529:<5}")
    print(f"{'OMAN (E)':<15} {4:<3} {0:<3} {4:<3} {0:<3} {0:<3} {-3.062:<5}")

    # Group A
    print("\nGroup A")
    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'IND (Q)':<15} {4:<3} {3:<3} {0:<3} {1:<3} {7:<3} {+1.137:<5}")
    print(f"{'USA (Q)':<15} {4:<3} {2:<3} {1:<3} {1:<3} {5:<3} {+0.127:<5}")
    print(f"{'PAK (E)':<15} {4:<3} {2:<3} {2:<3} {0:<3} {4:<3} {+0.294:<5}")
    print(f"{'CAN (E)':<15} {4:<3} {1:<3} {2:<3} {1:<3} {3:<3} {-0.493:<5}")
    print(f"{'IRE (E)':<15} {4:<3} {0:<3} {3:<3} {1:<3} {1:<3} {-0.594:<5}")

def display_squads_1(series_name):
    if series_name == "T20 Blast 2024":
        display_t20_blast_squads()
    else:
        print("Squad details for this series are not available.")

def display_t20_blast_squads_1():
    print("\nIndian Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'rohit-sharma':<20} {'Rohit Sharma':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'yashasvi-jaiswal':<20} {'Yashasvi Jaiswal':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'virat-kohli':<20} {'Virat Kohli':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'suryakumar-yadav':<20} {'Suryakumar Yadav':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'hardik-pandya':<20} {'Hardik Pandya':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'shivam-dube':<20} {'Shivam Dube':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ravindra-jadeja':<20} {'Ravindra Jadeja':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'axar-patel':<20} {'Axar Patel':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'rishabh-pant':<20} {'Rishabh Pant':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'sanju-samson':<20} {'Sanju Samson':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'kuldeep-yadav':<20} {'Kuldeep Yadav':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'yuzvendra-chahal':<20} {'Yuzvendra Chahal':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'arshdeep-singh':<20} {'Arshdeep Singh':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'jasprit-bumrah':<20} {'Jasprit Bumrah':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-siraj':<20} {'Mohammed Siraj':<20} {'Bowler':<20}")

    print("\nEngland Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'harry-brook':<20} {'Harry Brook':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'ben-duckett':<20} {'Ben Duckett':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'moeen-ali':<20} {'Moeen Ali':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'will-jacks':<20} {'Will Jacks':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'liam-livingstone':<20} {'Liam Livingstone':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'sam-curran':<20} {'Sam Curran':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'jos-buttler':<20} {'Jos Buttler':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'jonny-bairstow':<20} {'Jonny Bairstow':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'philip-salt':<20} {'Philip Salt':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'jofra-archer':<20} {'Jofra Archer':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tom-hartley':<20} {'Tom Hartley':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'chris-jordan':<20} {'Chris Jordan':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'adil-rashid':<20} {'Adil Rashid':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'reece-topley':<20} {'Reece Topley':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mark-wood':<20} {'Mark Wood':<20} {'Bowler':<20}")

    print("\nSouth Africa Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'aiden-markram':<20} {'Aiden Markram (Captain)':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'reeza-hendricks':<20} {'Reeza Hendricks':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'david-miller':<20} {'David Miller':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'marco-jansen':<20} {'Marco Jansen':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'quinton-de-kock':<20} {'Quinton de Kock':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'heinrich-klaasen':<20} {'Heinrich Klaasen':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'ryan-rickelton':<20} {'Ryan Rickelton':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'tristan-stubbs':<20} {'Tristan Stubbs':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'ottneil-baartman':<20} {'Ottneil Baartman':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'gerald-coetzee':<20} {'Gerald Coetzee':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'bjorn-fortuin':<20} {'Bjorn Fortuin':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'keshav-maharaj':<20} {'Keshav Maharaj':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'anrich-nortje':<20} {'Anrich Nortje':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'kagiso-rabada':<20} {'Kagiso Rabada':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tabraiz-shamsi':<20} {'Tabraiz Shamsi':<20} {'Bowler':<20}")

    print("\nAustralia Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    print(f"{'BATTERS':<20} {'tim-david':<20} {'Tim David':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'travis-head':<20} {'Travis Head':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'david-warner':<20} {'David Warner':<20} {'Batter':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mitchell-marsh':<20} {'Mitchell Marsh (Captain)':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'cameron-green':<20} {'Cameron Green':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'glenn-maxwell':<20} {'Glenn Maxwell':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'marcus-stoinis':<20} {'Marcus Stoinis':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ashton-agar':<20} {'Ashton Agar':<20} {'Bowling Allrounder':<20}")
    print(f"{'WICKET KEEPERS':<20} {'josh-inglis':<20} {'Josh Inglis':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'matthew-wade':<20} {'Matthew Wade':<20} {'WK-Batter':<20}")
    print(f"{'BOWLERS':<20} {'pat-cummins':<20} {'Pat Cummins':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'nathan-ellis':<20} {'Nathan Ellis':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'josh-hazlewood':<20} {'Josh Hazlewood':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mitchell-starc':<20} {'Mitchell Starc':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'adam-zampa':<20} {'Adam Zampa':<20} {'Bowler':<20}")


def display_stats_1():
    print("\nT20 Blast 2024 Stats")

    # Most Runs
    print("\nMost Runs:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Gurbaz':<20} {8:<5} {8:<5} {281:<5} {35.12:<10}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {36.71:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {42.50:<10}")
    print(f"{'de Kock':<20} {9:<5} {9:<5} {243:<5} {27.00:<10}")
    print(f"{'Ibrahim Zadran':<20} {8:<5} {8:<5} {231:<5} {28.88:<10}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {38.00:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {43.80:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {42.80:<10}")
    print(f"{'Suryakumar Yadav':<20} {8:<5} {8:<5} {199:<5} {28.43:<10}")
    print(f"{'Klaasen':<20} {9:<5} {8:<5} {190:<5} {31.67:<10}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {37.60:<10}")
    print(f"{'Warner':<20} {7:<5} {7:<5} {178:<5} {29.67:<10}")
    print(f"{'Pant':<20} {8:<5} {8:<5} {171:<5} {24.43:<10}")
    print(f"{'David Miller':<20} {9:<5} {8:<5} {169:<5} {28.17:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {42.25:<10}")

    # Highest Scores
    print("\nHighest Scores:")
    print(f"{'Batter':<20} {'HS':<5} {'Balls':<6} {'SR':<6} {'Vs':<5}")
    print("="*40)
    print(f"{'Pooran':<20} {98:<5} {53:<6} {184.91:<6} {'AFG':<5}")
    print(f"{'Aaron Jones':<20} {94:<5} {40:<6} {235.00:<6} {'CAN':<5}")
    print(f"{'Rohit':<20} {92:<5} {41:<6} {224.39:<6} {'AUS':<5}")
    print(f"{'Salt':<20} {87:<5} {47:<6} {185.11:<6} {'WI':<5}")
    print(f"{'Jos Buttler':<20} {83:<5} {38:<6} {218.42:<6} {'USA':<5}")
    print(f"{'Shai Hope':<20} {82:<5} {39:<6} {210.26:<6} {'USA':<5}")
    print(f"{'Andries Gous':<20} {80:<5} {47:<6} {170.21:<6} {'RSA':<5}")
    print(f"{'Gurbaz':<20} {80:<5} {56:<6} {142.86:<6} {'NZ':<5}")
    print(f"{'Head':<20} {76:<5} {43:<6} {176.74:<6} {'IND':<5}")
    print(f"{'Gurbaz':<20} {76:<5} {45:<6} {168.89:<6} {'UGA':<5}")
    print(f"{'Kohli':<20} {76:<5} {59:<6} {128.81:<6} {'RSA':<5}")
    print(f"{'de Kock':<20} {74:<5} {40:<6} {185.00:<6} {'USA':<5}")
    print(f"{'Ibrahim Zadran':<20} {70:<5} {46:<6} {152.17:<6} {'UGA':<5}")
    print(f"{'Sherfane Rutherford':<20} {68:<5} {39:<6} {174.36:<6} {'NZ':<5}")
    print(f"{'Head':<20} {68:<5} {49:<6} {138.78:<6} {'SCO':<5}")

    # Best Batting Average
    print("\nBest Batting Average:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Berrington':<20} {4:<5} {3:<5} {102:<5} {102.00:<10}")
    print(f"{'Harry Brook':<20} {8:<5} {4:<5} {145:<5} {72.50:<10}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {70.00:<10}")
    print(f"{'Shai Hope':<20} {3:<5} {3:<5} {107:<5} {53.50:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {6:<5} {144:<5} {48.00:<10}")
    print(f"{'Roston Chase':<20} {6:<5} {3:<5} {94:<5} {47.00:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {43.80:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {42.80:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {42.50:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {42.25:<10}")
    print(f"{'Munsey':<20} {4:<5} {4:<5} {124:<5} {41.33:<10}")
    print(f"{'Babar Azam':<20} {4:<5} {4:<5} {122:<5} {40.67:<10}")
    print(f"{'Aaron Jones':<20} {6:<5} {6:<5} {162:<5} {40.50:<10}")
    print(f"{'Sherfane Rutherford':<20} {7:<5} {6:<5} {121:<5} {40.33:<10}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {38.00:<10}")

    # Best Batting Strike Rate
    print("\nBest Batting Strike Rate:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'SR':<10}")
    print("="*45)
    print(f"{'Shai Hope':<20} {3:<5} {3:<5} {107:<5} {187.72:<10}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {170.73:<10}")
    print(f"{'Russell':<20} {7:<5} {6:<5} {78:<5} {165.96:<10}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {164.08:<10}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {159.32:<10}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {158.52:<10}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {158.39:<10}")
    print(f"{'Harry Brook':<20} {8:<5} {4:<5} {145:<5} {157.61:<10}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {156.71:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {6:<5} {144:<5} {151.58:<10}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {151.03:<10}")
    print(f"{'Delany':<20} {3:<5} {3:<5} {60:<5} {150.00:<10}")
    print(f"{'Tim David':<20} {7:<5} {5:<5} {61:<5} {148.78:<10}")
    print(f"{'Sherfane Rutherford':<20} {7:<5} {6:<5} {121:<5} {147.56:<10}")
    print(f"{'Livingstone':<20} {8:<5} {4:<5} {72:<5} {146.94:<10}")

    # Most Wickets
    print("\nMost Wickets:")
    print(f"{'Bowler':<20} {'M':<5} {'O':<5} {'W':<5} {'Avg':<10}")
    print("="*45)
    print(f"{'Fazalhaq Farooqi':<20} {8:<5} {25.2:<5} {17:<5} {9.41:<10}")
    print(f"{'Arshdeep Singh':<20} {8:<5} {30.0:<5} {17:<5} {12.65:<10}")
    print(f"{'Bumrah':<20} {8:<5} {29.4:<5} {15:<5} {8.27:<10}")
    print(f"{'Nortje':<20} {9:<5} {35.0:<5} {15:<5} {13.40:<10}")
    print(f"{'Rashid Khan':<20} {8:<5} {29.0:<5} {14:<5} {12.79:<10}")
    print(f"{'Rishad Hossain':<20} {7:<5} {25.0:<5} {14:<5} {13.86:<10}")
    print(f"{'Naveen-ul-Haq':<20} {8:<5} {26.4:<5} {13:<5} {12.31:<10}")
    print(f"{'Rabada':<20} {9:<5} {31.0:<5} {13:<5} {15.00:<10}")
    print(f"{'Zampa':<20} {7:<5} {28.0:<5} {13:<5} {14.38:<10}")
    print(f"{'Alzarri Joseph':<20} {7:<5} {24.3:<5} {13:<5} {13.62:<10}")
    print(f"{'Tanzim Hasan Sakib':<20} {7:<5} {24.0:<5} {11:<5} {13.55:<10}")
    print(f"{'Maharaj':<20} {8:<5} {28.0:<5} {11:<5} {15.91:<10}")
    print(f"{'Russell':<20} {7:<5} {20.1:<5} {11:<5} {12.82:<10}")
    print(f"{'Shamsi':<20} {5:<5} {16.5:<5} {11:<5} {11.64:<10}")
    print(f"{'Hardik Pandya':<20} {8:<5} {25.0:<5} {11:<5} {17.36:<10}")

    # Most Fifties
    print("\nMost Fifties:")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'50s':<5}")
    print("="*30)
    print(f"{'Gurbaz':<20} {8:<5} {8:<5} {281:<5} {3:<5}")
    print(f"{'Rohit':<20} {8:<5} {8:<5} {257:<5} {3:<5}")
    print(f"{'Head':<20} {7:<5} {7:<5} {255:<5} {2:<5}")
    print(f"{'de Kock':<20} {9:<5} {9:<5} {243:<5} {2:<5}")
    print(f"{'Ibrahim Zadran':<20} {8:<5} {8:<5} {231:<5} {2:<5}")
    print(f"{'Andries Gous':<20} {6:<5} {6:<5} {219:<5} {2:<5}")
    print(f"{'Suryakumar Yadav':<20} {8:<5} {8:<5} {199:<5} {2:<5}")
    print(f"{'Warner':<20} {7:<5} {7:<5} {178:<5} {2:<5}")
    print(f"{'Stoinis':<20} {7:<5} {5:<5} {169:<5} {2:<5}")
    print(f"{'Brandon McMullen':<20} {4:<5} {3:<5} {140:<5} {2:<5}")
    print(f"{'Pooran':<20} {7:<5} {7:<5} {228:<5} {1:<5}")
    print(f"{'Jos Buttler':<20} {8:<5} {7:<5} {214:<5} {1:<5}")
    print(f"{'Klaasen':<20} {9:<5} {8:<5} {190:<5} {1:<5}")
    print(f"{'Salt':<20} {8:<5} {7:<5} {188:<5} {1:<5}")
    print(f"{'David Miller':<20} {9:<5} {8:<5} {169:<5} {1:<5}")

# Call the function to display stats

def display_ipl_squads():
    # Royal Challengers Bangalore Squad
    print("\nRoyal Challengers Bangalore Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    
    # BATTERS
    print(f"{'BATTERS':<20} {'suyash-prabhudessai':<20} {'Suyash Prabhudessai':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'rajat-patidar':<20} {'Rajat Patidar':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'virat-kohli':<20} {'Virat Kohli':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'faf-du-plessis':<20} {'Faf du Plessis (Captain)':<20} {'Batter':<20}")
    
    # ALL ROUNDERS
    print(f"{'ALL ROUNDERS':<20} {'glenn-maxwell':<20} {'Glenn Maxwell':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mahipal-lomror':<20} {'Mahipal Lomror':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'cameron-green':<20} {'Cameron Green':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'manoj-bhandage':<20} {'Manoj Bhandage':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'saurav-chauhan':<20} {'Saurav Chauhan':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'swapnil-singh':<20} {'Swapnil Singh':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'tom-curran':<20} {'Tom Curran':<20} {'Bowling Allrounder':<20}")
    
    # WICKET KEEPERS
    print(f"{'WICKET KEEPERS':<20} {'dinesh-karthik':<20} {'Dinesh Karthik':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'anuj-rawat':<20} {'Anuj Rawat':<20} {'WK-Batter':<20}")
    
    # BOWLERS
    print(f"{'BOWLERS':<20} {'karn-sharma':<20} {'Karn Sharma':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'vijaykumar-vyshak':<20} {'Vijaykumar Vyshak':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'alzarri-joseph':<20} {'Alzarri Joseph':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'yash-dayal':<20} {'Yash Dayal':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'rajan-kumar':<20} {'Rajan Kumar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mayank-dagar':<20} {'Mayank Dagar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'lockie-ferguson':<20} {'Lockie Ferguson':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-siraj':<20} {'Mohammed Siraj':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'himanshu-sharma':<20} {'Himanshu Sharma':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'akash-deep':<20} {'Akash Deep':<20} {'Bowler':<20}")

    # Chennai Super Kings Squad
    print("\nChennai Super Kings Squad:")
    print(f"{'Category':<20} {'Player ID':<20} {'Name':<20} {'Role':<20}")
    print("="*80)
    
    # BATTERS
    print(f"{'BATTERS':<20} {'ruturaj-gaikwad':<20} {'Ruturaj Gaikwad (Captain)':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'ajinkya-rahane':<20} {'Ajinkya Rahane':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'shaik-rasheed':<20} {'Shaik Rasheed':<20} {'Batter':<20}")
    print(f"{'BATTERS':<20} {'sameer-rizvi':<20} {'Sameer Rizvi':<20} {'Batter':<20}")
    
    # ALL ROUNDERS
    print(f"{'ALL ROUNDERS':<20} {'shivam-dube':<20} {'Shivam Dube':<20} {'Batting Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'ravindra-jadeja':<20} {'Ravindra Jadeja':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'mohammed-nabi':<20} {'Mohammed Nabi':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'michael-bracewell':<20} {'Michael Bracewell':<20} {'Bowling Allrounder':<20}")
    print(f"{'ALL ROUNDERS':<20} {'simarjeet-singh':<20} {'Simarjeet Singh':<20} {'Bowling Allrounder':<20}")
    
    # WICKET KEEPERS
    print(f"{'WICKET KEEPERS':<20} {'ms-dhoni':<20} {'MS Dhoni':<20} {'WK-Batter':<20}")
    print(f"{'WICKET KEEPERS':<20} {'devon-conway':<20} {'Devon Conway':<20} {'WK-Batter':<20}")
    
    # BOWLERS
    print(f"{'BOWLERS':<20} {'deepak-chahar':<20} {'Deepak Chahar':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'maheesh-theekshana':<20} {'Maheesh Theekshana':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'matheesha-pathirana':<20} {'Matheesha Pathirana':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mohammed-shami':<20} {'Mohammed Shami':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'tushar-deshpande':<20} {'Tushar Deshpande':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'mukesh-choudhary':<20} {'Mukesh Choudhary':<20} {'Bowler':<20}")
    print(f"{'BOWLERS':<20} {'prashant-solanki':<20} {'Prashant Solanki':<20} {'Bowler':<20}")

def display_matches_3():
    
    matches = [
        ("1st Match", "Chennai, MA Chidambaram Stadium", "RCB vs CSK", "RCB: 173-6 (20) | CSK: 176-4 (18.4)", "CSK won by 6 wkts"),
        ("2nd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "DC vs PBKS", "DC: 174-9 (20) | PBKS: 177-6 (19.2)", "PBKS won by 4 wkts"),
        ("3rd Match", "Kolkata, Eden Gardens", "KKR vs SRH", "KKR: 208-7 (20) | SRH: 204-7 (20)", "KKR won by 4 runs"),
        ("4th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs LSG", "RR: 193-4 (20) | LSG: 173-6 (20)", "RR won by 20 runs"),
        ("5th Match", "Ahmedabad, Narendra Modi Stadium", "GT vs MI", "GT: 168-6 (20) | MI: 162-9 (20)", "GT won by 6 runs"),
        ("6th Match", "Bengaluru, M.Chinnaswamy Stadium", "PBKS vs RCB", "PBKS: 176-6 (20) | RCB: 178-6 (19.2)", "RCB won by 4 wkts"),
        ("7th Match", "Chennai, MA Chidambaram Stadium", "CSK vs GT", "CSK: 206-6 (20) | GT: 143-8 (20)", "CSK won by 63 runs"),
        ("8th Match", "Hyderabad, Rajiv Gandhi International Stadium", "SRH vs MI", "SRH: 277-3 (20) | MI: 246-5 (20)", "SRH won by 31 runs"),
        ("9th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs DC", "RR: 185-5 (20) | DC: 173-5 (20)", "RR won by 12 runs"),
        ("10th Match", "Bengaluru, M.Chinnaswamy Stadium", "RCB vs KKR", "RCB: 182-6 (20) | KKR: 186-3 (16.5)", "KKR won by 7 wkts"),
        ("11th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs PBKS", "LSG: 199-8 (20) | PBKS: 178-5 (20)", "LSG won by 21 runs"),
        ("12th Match", "Ahmedabad, Narendra Modi Stadium", "SRH vs GT", "SRH: 162-8 (20) | GT: 168-3 (19.1)", "GT won by 7 wkts"),
        ("13th Match", "Visakhapatnam, Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "DC vs CSK", "DC: 191-5 (20) | CSK: 171-6 (20)", "DC won by 20 runs"),
        ("14th Match", "Mumbai, Wankhede Stadium", "MI vs RR", "MI: 125-9 (20) | RR: 127-4 (15.3)", "RR won by 6 wkts"),
        ("15th Match", "Bengaluru, M.Chinnaswamy Stadium", "LSG vs RCB", "LSG: 181-5 (20) | RCB: 153 (19.4)", "LSG won by 28 runs"),
        ("16th Match", "Visakhapatnam, Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "KKR vs DC", "KKR: 272-7 (20) | DC: 166 (17.2)", "KKR won by 106 runs"),
        ("17th Match", "Ahmedabad, Narendra Modi Stadium", "GT vs PBKS", "GT: 199-4 (20) | PBKS: 200-7 (19.5)", "PBKS won by 3 wkts"),
        ("18th Match", "Hyderabad, Rajiv Gandhi International Stadium", "CSK vs SRH", "CSK: 165-5 (20) | SRH: 166-4 (18.1)", "SRH won by 6 wkts"),
        ("19th Match", "Jaipur, Sawai Mansingh Stadium", "RCB vs RR", "RCB: 183-3 (20) | RR: 189-4 (19.1)", "RR won by 6 wkts"),
        ("20th Match", "Mumbai, Wankhede Stadium", "MI vs DC", "MI: 234-5 (20) | DC: 205-8 (20)", "MI won by 29 runs"),
        ("21st Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs GT", "LSG: 163-5 (20) | GT: 130 (18.5)", "LSG won by 33 runs"),
        ("22nd Match", "Chennai, MA Chidambaram Stadium", "KKR vs CSK", "KKR: 137-9 (20) | CSK: 141-3 (17.4)", "CSK won by 7 wkts"),
        ("23rd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "SRH vs PBKS", "SRH: 182-9 (20) | PBKS: 180-6 (20)", "SRH won by 2 runs"),
        ("24th Match", "Jaipur, Sawai Mansingh Stadium", "RR vs GT", "RR: 196-3 (20) | GT: 199-7 (20)", "GT won by 3 wkts"),
        ("25th Match", "Mumbai, Wankhede Stadium", "RCB vs MI", "RCB: 196-8 (20) | MI: 199-3 (15.3)", "MI won by 7 wkts"),
        ("26th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "LSG vs DC", "LSG: 167-7 (20) | DC: 170-4 (18.1)", "DC won by 6 wkts"),
        ("27th Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "PBKS vs RR", "PBKS: 147-8 (20) | RR: 152-7 (19.5)", "RR won by 3 wkts"),
        ("28th Match", "Kolkata, Eden Gardens", "LSG vs KKR", "LSG: 161-7 (20) | KKR: 162-2 (15.4)", "KKR won by 8 wkts"),
        ("29th Match", "Mumbai, Wankhede Stadium", "CSK vs MI", "CSK: 206-4 (20) | MI: 186-6 (20)", "CSK won by 20 runs"),
        ("30th Match", "Bengaluru, M.Chinnaswamy Stadium", "SRH vs RCB", "SRH: 287-3 (20) | RCB: 262-7 (20)", "SRH won by 25 runs"),
        ("31st Match", "Kolkata, Eden Gardens", "KKR vs RR", "KKR: 223-6 (20) | RR: 224-8 (20)", "RR won by 2 wkts"),
        ("32nd Match", "Ahmedabad, Narendra Modi Stadium", "GT vs DC", "GT: 89 (17.3) | DC: 92-4 (8.5)", "DC won by 6 wkts"),
        ("33rd Match", "Chandigarh, Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur", "MI vs PBKS", "MI: 192-7 (20) | PBKS: 183 (19.1)", "MI won by 9 runs"),
        ("34th Match", "Lucknow, Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "CSK vs LSG", "CSK: 176-6 (20) | LSG: 180-2 (19)", "LSG won by 8 wkts"),
        ("35th Match", "Delhi, Arun Jaitley Stadium", "SRH vs DC", "SRH: 266-7 (20) | DC: 199 (19.1)", "SRH won by 67 runs"),
        ("36th Match", "Kolkata, Eden Gardens", "KKR vs RCB", "KKR: 207-5 (20) | RCB: 200-7 (20)", "KKR won by 7 runs"),
        ("37th Match", "Chennai, MA Chidambaram Stadium", "CSK vs RR", "CSK: 184-8 (20) | RR: 186-7 (19.3)", "RR won by 3 wkts"),
        ("38th Match", "Mumbai, Wankhede Stadium", "MI vs SRH", "MI: 203-8 (20) | SRH: 206-4 (18.4)", "SRH won by 6 wkts"),
        ("39th Match", "Delhi, Arun Jaitley Stadium", "DC vs KKR", "DC: 182-7 (20) | KKR: 183-3 (17.5)", "KKR won by 7 wkts"),
        ("40th Match", "Hyderabad, Rajiv Gandhi International Stadium", "GT vs RR", "GT: 173-9 (20) | RR: 175-4 (19.4)", "RR won by 6 wkts"),
        ("41st Match", "Chennai, MA Chidambaram Stadium", "CSK vs RCB", "CSK: 177-6 (20) | RCB: 181-7 (19.5)", "RCB won by 3 wkts"),
        ("42nd Match", "Ahmedabad, Narendra Modi Stadium", "GT vs MI", "GT: 191-3 (20) | MI: 198-5 (20)", "MI won by 7 runs"),
        ("Final Match", "Mumbai, Wankhede Stadium", "MI vs RCB", "MI: 246-8 (20) | RCB: 251-5 (19.5)", "RCB won by 5 wkts")
    ]

    print("\nUpcoming Cricket Matches:")
    for match in matches:
        print(f"\nMatch: {match[0]}")
        print(f"Venue: {match[1]}")
        print(f"Teams: {match[2]}")
        print(f"Scores: {match[3]}")
        print(f"Result: {match[4]}")

def display_table_3():
    print("\nTable: IPL 2024")

    print(f"{'Team':<15} {'P':<3} {'W':<3} {'L':<3} {'NR':<3} {'Pts':<3} {'NRR':<5}")
    print("="*30)
    print(f"{'KKR (Q)':<15} {14:<3} {9:<3} {3:<3} {2:<3} {20:<3} {+1.428:<5}")
    print(f"{'SRH (Q)':<15} {14:<3} {8:<3} {5:<3} {1:<3} {17:<3} {+0.414:<5}")
    print(f"{'RR (Q)':<15} {14:<3} {8:<3} {5:<3} {1:<3} {17:<3} {+0.273:<5}")
    print(f"{'RCB (Q)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {+0.459:<5}")
    print(f"{'CSK (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {+0.392:<5}")
    print(f"{'DC (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {-0.377:<5}")
    print(f"{'LSG (E)':<15} {14:<3} {7:<3} {7:<3} {0:<3} {14:<3} {-0.667:<5}")
    print(f"{'GT (E)':<15} {14:<3} {5:<3} {7:<3} {2:<3} {12:<3} {-1.063:<5}")
    print(f"{'PBKS (E)':<15} {14:<3} {5:<3} {9:<3} {0:<3} {10:<3} {-0.353:<5}")
    print(f"{'MI (E)':<15} {14:<3} {4:<3} {10:<3} {0:<3} {8:<3} {-0.318:<5}")


def display_IPL_stats():
    print("\nMost Runs")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*50)
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {61.75:<10}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {53.00:<10}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {52.09:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {40.50:<10}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48.27:<10}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {47.91:<10}")
    print(f"{'Rahul':<20} {14:<5} {14:<5} {520:<5} {37.14:<10}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {62.38:<10}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {34.86:<10}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {32.27:<10}")
    print(f"{'Klaasen':<20} {16:<5} {15:<5} {479:<5} {39.92:<10}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {40.55:<10}")
    print(f"{'du Plessis':<20} {15:<5} {15:<5} {438:<5} {29.20:<10}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {39.55:<10}")
    print(f"{'Yashasvi Jaiswal':<20} {15:<5} {15:<5} {435:<5} {31.07:<10}")

    print("\nBest Batting Average")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'Avg':<10}")
    print("="*50)
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {62.38:<10}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {61.75:<10}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {54.00:<10}")
    print(f"{'Dhoni':<20} {14:<5} {11:<5} {161:<5} {53.67:<10}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {53.00:<10}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {52.09:<10}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48.27:<10}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {47.91:<10}")
    print(f"{'Venkatesh Iyer':<20} {14:<5} {13:<5} {370:<5} {46.25:<10}")
    print(f"{'Ravindra Jadeja':<20} {14:<5} {11:<5} {267:<5} {44.50:<10}")
    print(f"{'Shashank Singh':<20} {14:<5} {14:<5} {354:<5} {44.25:<10}")
    print(f"{'Tilak Varma':<20} {13:<5} {13:<5} {416:<5} {41.60:<10}")
    print(f"{'Arshad Khan':<20} {4:<5} {4:<5} {83:<5} {41.50:<10}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {40.55:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {40.50:<10}")

    print("\nBest Batting Strike Rate")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'SR':<10}")
    print("="*50)
    print(f"{'Romario Shepherd':<20} {6:<5} {5:<5} {57:<5} {271.43:<10}")
    print(f"{'Jake Fraser-McGurk':<20} {9:<5} {9:<5} {330:<5} {234.04:<10}")
    print(f"{'Dhoni':<20} {14:<5} {11:<5} {161:<5} {220.55:<10}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {204.22:<10}")
    print(f"{'Ramandeep Singh':<20} {14:<5} {9:<5} {125:<5} {201.61:<10}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {191.55:<10}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {190.91:<10}")
    print(f"{'Karthik':<20} {15:<5} {13:<5} {326:<5} {187.36:<10}")
    print(f"{'Russell':<20} {14:<5} {9:<5} {222:<5} {185.00:<10}")
    print(f"{'Lomror':<20} {10:<5} {10:<5} {125:<5} {183.82:<10}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {182.01:<10}")
    print(f"{'Rossouw':<20} {8:<5} {8:<5} {211:<5} {181.90:<10}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {180.74:<10}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {178.21:<10}")
    print(f"{'Naman Dhir':<20} {7:<5} {7:<5} {140:<5} {177.22:<10}")

    print("\nMost Sixes")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'6s':<5}")
    print("="*50)
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {42:<5}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {38:<5}")
    print(f"{'Klaasen':<20} {16:<5} {15:<5} {479:<5} {38:<5}")
    print(f"{'Pooran':<20} {14:<5} {14:<5} {499:<5} {36:<5}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {33:<5}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {33:<5}")
    print(f"{'Rajat Patidar':<20} {15:<5} {13:<5} {395:<5} {33:<5}")
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {32:<5}")
    print(f"{'Shivam Dube':<20} {14:<5} {14:<5} {396:<5} {28:<5}")
    print(f"{'Jake Fraser-McGurk':<20} {9:<5} {9:<5} {330:<5} {28:<5}")
    print(f"{'Tristan Stubbs':<20} {14:<5} {13:<5} {378:<5} {26:<5}")
    print(f"{'Pant':<20} {13:<5} {13:<5} {446:<5} {25:<5}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {24:<5}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {24:<5}")
    print(f"{'Rohit':<20} {14:<5} {14:<5} {417:<5} {23:<5}")

    print("\nMost Fours")
    print(f"{'Batter':<20} {'M':<5} {'I':<5} {'R':<5} {'4s':<5}")
    print("="*50)
    print(f"{'Head':<20} {15:<5} {15:<5} {567:<5} {64:<5}")
    print(f"{'Kohli':<20} {15:<5} {15:<5} {741:<5} {62:<5}")
    print(f"{'Ruturaj Gaikwad':<20} {14:<5} {14:<5} {583:<5} {58:<5}")
    print(f"{'Yashasvi Jaiswal':<20} {15:<5} {15:<5} {435:<5} {54:<5}")
    print(f"{'Narine':<20} {14:<5} {14:<5} {488:<5} {50:<5}")
    print(f"{'Salt':<20} {12:<5} {12:<5} {435:<5} {50:<5}")
    print(f"{'Samson':<20} {15:<5} {15:<5} {531:<5} {48:<5}")
    print(f"{'Sai Sudharsan':<20} {12:<5} {12:<5} {527:<5} {48:<5}")
    print(f"{'du Plessis':<20} {15:<5} {15:<5} {438:<5} {47:<5}")
    print(f"{'Rahul':<20} {14:<5} {14:<5} {520:<5} {45:<5}")
    print(f"{'Rohit':<20} {14:<5} {14:<5} {417:<5} {45:<5}")
    print(f"{'Riyan Parag':<20} {15:<5} {14:<5} {573:<5} {40:<5}")
    print(f"{'Stoinis':<20} {14:<5} {14:<5} {388:<5} {39:<5}")
    print(f"{'Shubman Gill':<20} {12:<5} {12:<5} {426:<5} {37:<5}")
    print(f"{'Abhishek Sharma':<20} {16:<5} {16:<5} {484:<5} {36:<5}")

# Call the function to display all stats
#display_cricket_stats()

# Example usage
#display_table_2()


# Sample Run
display_series_menu()
