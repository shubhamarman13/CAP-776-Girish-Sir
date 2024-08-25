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
    print("2. Recent Matches")
    print("3. Upcoming Matches")
    print("4. Back to Main Menu")

def display_schedule_menu():
    print("\nSchedule Menu:")
    print("1. Upcoming Matches")
    print("2. Team Schedules")
    print("3. Series Schedules")
    print("4. Back to Main Menu")

def display_news_menu():
    print("\nNews Menu:")
    print("1. Latest News")
    print("2. Top Stories")
    print("3. Back to Main Menu")

def display_series_menu():
    print("\nSeries Menu:")
    print("1. Current Series")
    print("2. Upcoming Series")
    print("3. Back to Main Menu")

def display_teams_menu():
    print("\nTeams Menu:")
    print("1. International Teams")
    print("2. Domestic Teams")
    print("3. Back to Main Menu")

def display_rankings_menu():
    print("\nRankings Menu:")
    print("1. Team Rankings")
    print("2. Player Rankings")
    print("3. Back to Main Menu")

def main():
    display_welcome_message()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            while True:
                display_live_scores_menu()
                sub_choice = input("Enter your choice (1-4): ")
                if sub_choice == '1':
                    print("Displaying Current Matches...")
                elif sub_choice == '2':
                    print("Displaying Recent Matches...")
                elif sub_choice == '3':
                    print("Displaying Upcoming Matches...")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        
        elif choice == '2':
            while True:
                display_schedule_menu()
                sub_choice = input("Enter your choice (1-4): ")
                if sub_choice == '1':
                    print("Displaying Upcoming Matches...")
                elif sub_choice == '2':
                    print("Displaying Team Schedules...")
                elif sub_choice == '3':
                    print("Displaying Series Schedules...")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        elif choice == '3':
            while True:
                display_news_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying Latest News...")
                elif sub_choice == '2':
                    print("Displaying Top Stories...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '4':
            while True:
                display_series_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying Current Series...")
                elif sub_choice == '2':
                    print("Displaying Upcoming Series...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '5':
            while True:
                display_teams_menu()
                sub_choice = input("Enter your choice (1-3): ")
                if sub_choice == '1':
                    print("Displaying International Teams...")
                elif sub_choice == '2':
                    print("Displaying Domestic Teams...")
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '6':
            while True:
                display_rankings_menu()
                sub_choice = input("\nEnter your choice: ")
                
                if sub_choice == '1':
                    print("\n**Displaying Team Rankings**")
                    print("\n1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    team_ranking_choice = input("\nEnter your choice: ")
                    print("\n1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    if team_ranking_choice == '1':   #1 = ODI, 2 = T20, 3 = TEST
                        print("\n\n                 * Displaying Top 10 ODI Teams *")
                        print("\nRank         Team             Matches           Rating          Points")
                        print("\n 1          India               45               118            5298\n 2          Australia           34               116            3936\n 3          South Africa        30               112            3357\n 4          Pakistan            26               106            2762\n 5          New Zealand         33               101            3349\n 6          Sri Lanka           50                97            4825\n 7          England             28                95            2672\n 8          Bangladesh          40                86            3453\n 9          Afghanistan         31                80            2477\n 10         West Indies         32                69            2205")
                        
                    elif team_ranking_choice == '2':
                        print("\n\n                 * Displaying Top 10 T20I Teams *")
                        print("\nRank         Team             Matches            Rating          Points")
                        print("\n 1          India               63                267           16835\n 2          Australia           40                256           10241\n 3          England             39                253            9876\n 4          West Indies         46                252           11604\n 5          South Africa        35                251           18777\n 6          New Zealand         49                247           12113\n 7          Pakistan            46                241           11097\n 8          Sri Lanka           40                229            9159\n 9          Bangladesh          50                225           11253\n 10         Afghanistan         39                223            8682")  
                        
                    elif team_ranking_choice == '3':
                        print("\n\n                 * Displaying Top 10 TEST Teams *")
                        print("\nRank         Team             Matches          Rating          Points")
                        print("\n 1          Australia           30              124            3715\n 2          India               26              120            3108\n 3          England             34              108            3679\n 4          South Africa        21              104            2179\n 5          New Zealand         22               96            2121\n 6          Pakistan            17               89            1519\n 7          Sri Lanka           18               83            1501\n 8          West Indies         26               77            1992\n 9          Bangladesh          17               53             906\n 10         Ireland              5               26             131")
                        
                elif sub_choice == '2':
                    print("\nDisplaying Player Rankings...")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    player_ranking_choice = input("\nEnter your choice: ")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")

                    if player_ranking_choice == '1':    #1 = ODI, 2 = T20, 3 = TEST
                        
                        print("\n   * Displaying Top 10 ODI Batters *  ")
                        print("\n  Rank              Player                     Points")
                        print("\n   1              Babar Azam                    824\n   2              Rohit Sharma                  765\n   3              Shubhman Gill                 763\n   4              Harry Tector                  746\n   5              Virat Kohli                   746\n   6              Daryl Mitchell                728\n   7              David Warner                  723\n   8              Pathum Nissanka               708\n   9              Dawid Malan                   707\n   10             Rassie van der Dussen         701                                                                      \n\n ") 
                        
                        print("    * Displaying Top 10 ODI Bowlers *")
                        print("\n  Rank         Player                   Points")
                        print("\n   1         Keshav Maharaj               716\n   2         Josh Hazlewood               688\n   3         Adam Zampa                   686\n   4         Kuldeep Yadav                665\n   5         Bernard Scholtz              657\n   6         Mohammad Nabi                656\n   7         Shaheen Afridi               650\n   8         Jasprit Bumrah               645\n   9         Mohammad Siraj               643\n   10        Trent Boult                  642\n\n")                           
                                                                      
                        print("* Displaying Top 10 ODI All Rounders *")
                        print("\n  Rank         Player                 Points")
                        print("\n   1          Mohammad Nabi             320\n   2          Shakib Al Hasan           292\n   3          Sikandar Raza             288\n   4          Assad Vala                248\n   5          Rashid Khan               239\n   6          Gerhard Erasmus           238\n   7          Glenn Maxwell             237\n   8          Mitchell Santner          233\n   9          Mehidy Hasan Miraz        230\n   10         Zeeshan Maqsood           229\n")
                        
                    elif player_ranking_choice == '2':    #1 = ODI, 2 = T20, 3 = TEST
                        
                        print("\n    * Displaying Top 10 T20I Batters *")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Travis Head              844\n   2           Surya K Yadav            805\n   3           Philip Salt              797\n   4           Yashasvi Jaiswal         757\n   5           Babar Azam               755\n   6           Mohammad Rizwan          746\n   7           Jos Butler               716\n   8           Ruturaj Gaikwad          664\n   9           Brandon King             656\n   10          Johnson Charles          655")
                        
                        print("\n\n    * Displaying Top 10 T20I Bowlers *")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Adil Rashid              718\n   2           Anrich Nortje            675\n   3           Rashid Khan              668\n   4           Wanindu Hasaranga        663\n   5           Josh Hazlewood           662\n   6           Akeal Hosein             659\n   7           Adam Zampa               654\n   8           Fazalhaq Farooqi         645\n   9           Maheesh Teekshana        645\n   10          Ravi Bishnoi             640")
                        
                        print("\n\n    * Displaying Top 10 T20I All Rounders *")
                        print("\n  Rank           Player                Points")
                        print("\n   1          Marcus Stoinis            211\n   2          Sikandar Raza             208\n   3          Shakib Al Hasan           206\n   4          Wanindu Hasaranga         205\n   5          Mohammad Nabi             204\n   6          Deependra S. Airee        199\n   7          Hardik Pandya             187\n   8          Liam Livingstone          186\n   9          Aiden Markram             174\n   10         Moeen Ali                 174")
                        
                    elif player_ranking_choice == '3':    #1 = ODI, 2 = T20, 3 = TEST
                        print("\n   * Displaying Top 10 TEST Batters *")
                        print("\n  Rank           Player                Points")
                        print("\n   1           Joe Root                 872\n   2           Kane Williamson          859\n   3           Babar Azam               768\n   4           Daryl Mitchell           767\n   5           Steven Smith             757\n   6           Rohit Sharma             751\n   7           Harry Brook              749\n   8           Yashasvi Jaiswal         740\n   9           Dimuth Karunaratne       739\n   10          Virat Kohli              737")
                        
                        print("\n\n    **Displaying Top 10 TEST Bowlers **")
                        print("\n  Rank           Player                Points")
                        print("\n   1           R. Ashwin                870\n   2           Josh Hazlewood           847\n   3           Jasprit Bumrah           847\n   4           Kagiso Rabada            820\n   5           Pat Cummins              820\n   6           Nathan Lyon              801\n   7           Ravindra Jadeja          788\n   8           Shaheen Afridi           733\n   9           Kyle Jamieson            729\n   10          Prabath Jayasuriya       724")
                        
                        print("\n\n  * Displaying Top 10 TEST All Rounders *")
                        print("\n  Rank           Player                Points")
                        print("\n   1         Ravindra Jadeja            444\n   2         R. Ashwin                  322\n   3         Shakib Al Hasan            310\n   4         Joe Root                   284\n   5         Axar Patel                 270\n   6         Ben Stokes                 266\n   7         Jason Holder               265\n   8         Pat Cummins                245\n   9         Chris Woakes               237\n   10        Marco Jansen               225")

                        
                    elif sub_choice == '3':
                        break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if _name_ == "_main_":
    main()
