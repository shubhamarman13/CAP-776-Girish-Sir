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

def display_live_scores_menu():
    print("\nLive Scores Menu:")
    print("1. Current Matches")
    print("2. Back to Main Menu")

def display_current_matches():
    print("\nCurrent Matches:")
    print("+" + "-"*75 + "+")
    print("| SRI LANKA TOUR OF ENGLAND, 2024" + " " * 30 + "|")
    print("| Sri Lanka vs England, 1st Test" + " " * 29 + "|")
    print("| Aug 21 - Today  •  3:30 PM at Manchester, Emirates Old Trafford" + " " * 5 + "|")
    print("| SL236 & 326" + " " * 50 + "|")
    print("| ENG358 & 205-5" + " " * 45 + "|")
    print("| England won by 5 wkts" + " " * 47 + "|")
    print("+" + "-"*75 + "+")
    print("| NETHERLANDS T20I TRI-SERIES, 2024" + " " * 27 + "|")
    print("| Canada vs United States, 2nd T20I Match" + " " * 24 + "|")
    print("| Aug 24  •  7:30 PM at Utrecht, Sportpark Maarschalkerweerd" + " " * 4 + "|")
    print("| CAN169-5 (20 Ovs)" + " " * 53 + "|")
    print("| USA" + " " * 69 + "|")
    print("| No result - due to rain" + " " * 50 + "|")
    print("+" + "-"*75 + "+")
    print("| BANGLADESH TOUR OF PAKISTAN, 2024" + " " * 27 + "|")
    print("| Pakistan vs Bangladesh, 1st Test" + " " * 28 + "|")
    print("| Aug 21 - Today  •  10:30 AM at Rawalpindi, Rawalpindi Cricket Stadium" + " " * 2 + "|")
    print("| PAK448-6 d & 23-1" + " " * 51 + "|")
    print("| BAN565" + " " * 62 + "|")
    print("| Day 4: Stumps - Pakistan trail by 94 runs" + " " * 34 + "|")
    print("+" + "-"*75 + "+")
    print("| ICC MENS T20 WORLD CUP SUB REGIONAL EUROPE QUALIFIER C, 2024" + " " * 7 + "|")
    print("| Greece vs Cyprus, 11th Match, Group A" + " " * 31 + "|")
    print("| Aug 24  •  8:00 PM at Castel, King George V Sports Ground" + " " * 11 + "|")
    print("| GRC100 (19.4 Ovs)" + " " * 56 + "|")
    print("| CYP102-2 (12.2 Ovs)" + " " * 52 + "|")
    print("| Cyprus won by 8 wkts" + " " * 52 + "|")
    print("+" + "-"*75 + "+")
    print("| Bulgaria vs Estonia, 12th Match, Group B" + " " * 33 + "|")
    print("| Aug 24  •  8:00 PM at Port Soif, Guernsey Rovers Athletic Club Ground" + "|")
    print("| BGR129-8 (20 Ovs)" + " " * 55 + "|")
    print("| EST131-3 (17 Ovs)" + " " * 56 + "|")
    print("| Estonia won by 7 wkts" + " " * 53 + "|")
    print("+" + "-"*75 + "+")
    #print("\n2. Back to Main Menu")

def display_schedule_menu():
    print("\nSchedule Menu:")
    print("1. Upcoming Matches")
    print("2. Back to Main Menu")

def display_upcoming_matches():
    upcoming_matches = {
        "SAT, AUG 24 2024": [
            ("Bangladesh tour of Pakistan, 2024", "Pakistan vs Bangladesh, 1st Test, Day 4", "Rawalpindi Cricket Stadium, Rawalpindi", "10:30 AM", "05:00 AM GMT / 10:00 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Denmark vs Spain, 9th Match, Group A", "King George V Sports Ground, Castel", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL")
        ],
        "SUN, AUG 25 2024": [
            ("Bangladesh tour of Pakistan, 2024", "Pakistan vs Bangladesh, 1st Test, Day 5", "Rawalpindi Cricket Stadium, Rawalpindi", "10:30 AM", "05:00 AM GMT / 10:00 AM LOCAL"),
            ("Netherlands T20I Tri-Series, 2024", "Netherlands vs United States, 3rd T20I Match", "Sportpark Maarschalkerweerd, Utrecht", "7:30 PM", "02:00 PM GMT / 04:00 PM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Bulgaria vs Malta, 13th Match, Group B", "King George V Sports Ground, Castel", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Cyprus vs Czech Republic, 14th Match, Group A", "Guernsey Rovers Athletic Club Ground, Port Soif", "3:00 PM", "09:30 AM GMT / 10:30 AM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Greece vs Spain, 16th Match, Group A", "Guernsey Rovers Athletic Club Ground, Port Soif", "8:00 PM", "02:30 PM GMT / 03:30 PM LOCAL"),
            ("ICC Mens T20 World Cup Sub Regional Europe Qualifier C, 2024", "Guernsey vs Estonia, 15th Match, Group B", "King George V Sports Ground, Castel", "8:00 PM", "02:30 PM GMT / 03:30 PM LOCAL"),
            ("Malaysia T20I Tri Nations Cup, 2024", "Kuwait vs Malaysia, 5th Match", "Selangor Turf Club, Kuala Lumpur", "8:00 AM", "02:30 AM GMT / 10:30 AM LOCAL")
        ],
        "MON, AUG 26 2024": [
            ("Netherlands T20I Tri-Series, 2024", "Netherlands vs United States, 4th T20I Match", "Sportpark Maarschalkerweerd, Utrecht", "5:30 PM", "12:00 PM GMT / 02:00 PM LOCAL"),
            ("South Africa tour of West Indies, 2024", "West Indies vs South Africa, 2nd T20I", "Brian Lara Stadium, Tarouba, Trinidad", "12:30 AM (Aug 26)", "07:00 PM GMT / 03:00 PM LOCAL"),
            ("Malaysia T20I Tri Nations Cup, 2024", "Hong Kong vs Malaysia, 6th Match", "Selangor Turf Club, Kuala Lumpur", "8:00 AM", "02:30 AM GMT / 10:30 AM LOCAL")
        ]
    }

    print("\nUpcoming Matches:")
    print("+" + "-"*75 + "+")
    for date, matches in upcoming_matches.items():
        print("| " + date + " " * (75 - len(date)) + "|")
        print("+" + "-"*75 + "+")
        for match in matches:
            print(f"| {match[0]:<40} | {match[1]:<40} | {match[2]:<25} | {match[3]:<8} | {match[4]:<28} |")
            print("+" + "-"*75 + "+")
    #print("\n2. Back to Main Menu")

def display_news_menu():
    print("\nNews Menu:")
    print("1. Latest News")
    print("2. Back to Main Menu")

def display_latest_news():
    news_items = [
        ("REPORTS • ENG V SL, 1ST TEST", "Root stars in England's jittery win in Manchester", "1h ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND, 2024", "England lose top-order in pursuit of 205", "4h ago"),
        ("NEWS • PAK V BAN, 1ST TEST", "Early strikes on Day 5 could seal historic win for Bangladesh, says Mehidy", "4h ago"),
        ("NEWS • BANGLADESH CRICKET", "BCB to take a call on Shakib's future after ongoing Rawalpindi Test", "5h ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Mushfiqur puts Bangladesh in driver's seat in Rawalpindi", "6h ago"),
        ("REPORTS • ENG V SL, 1ST TEST", "Kamindu Mendis, Dinesh Chandimal lift Sri Lanka's hopes", "7h ago"),
        ("NEWS • WOMEN'S LEAGUE 2", "Associates call for Women's League 2 after Championship snub", "7h ago"),
        ("NEWS • AUSTRALIAN CRICKET", "Josh Hazlewood ruled out of Scotland T20Is", "8h ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Rahim-Mehidy record stand propels Bangladesh into lead", "10h ago"),
        ("NEWS • PAK V BAN, 1ST TEST", "Rahim's ton helps Bangladesh reduce deficit", "13h ago"),
        ("REPORTS • SOUTH AFRICA TOUR OF WEST INDIES, 2024", "Pooran blitz powers West Indies to thumping win", "15h ago"),
        ("NEWS • FAREWELL", "Shikhar Dhawan announces retirement from all cricket", "17h ago"),
        ("NEWS • SRI LANKA'S TOUR OF ENGLAND, 2024", "Jamie Smith 'grateful' for mentor Ian Bell", "18h ago"),
        ("NEWS • WOMEN'S T20 WORLD CUP, 2024", "Nigar Sultana disappointed to not be playing a 'home World Cup'", "19h ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND 2024", "Bowlers deliver again to put England in command", "1d ago"),
        ("REPORTS • SRI LANKA TOUR OF ENGLAND, 2024", "Mathews resists but England chip away", "1d ago"),
        ("NEWS • BANGLADESH TOUR OF PAKISTAN, 2024", "Crime to get out for just 50 - Mominul on his batting", "1d ago"),
        ("REPORTS • BANGLADESH TOUR OF PAKISTAN, 2024", "Dogged Bangladesh batters fight to cut deficit", "1d ago"),
        ("NEWS • SRI LANKA TOUR OF ENGLAND, 1ST TEST", "Jamie Smith's maiden ton puts England in command", "1d ago")
    ]

    print("\nLatest News:")
    print("+" + "-"*80 + "+")
    print("| Category                                | Headline                                               | Time     |")
    print("+" + "-"*80 + "+")
    for item in news_items:
        print(f"| {item[0]:<40} | {item[1]:<50} | {item[2]:<8} |")
        print("+" + "-"*80 + "+")
    #print("\n2. Back to Main Menu")

def main():
    display_welcome_message()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            while True:
                display_live_scores_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_current_matches()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")
        
        elif choice == '2':
            while True:
                display_schedule_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_upcoming_matches()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")
        
        elif choice == '3':
            while True:
                display_news_menu()
                sub_choice = input("Enter your choice (1-2): ")
                if sub_choice == '1':
                    display_latest_news()
                elif sub_choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")
        
        elif choice == '4':
            print("Displaying Series...")
        
        elif choice == '5':
            print("Displaying Teams...")
        
        elif choice == '6':
            print("Displaying Rankings...")
        
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if _name_ == "_main_":
    main()
