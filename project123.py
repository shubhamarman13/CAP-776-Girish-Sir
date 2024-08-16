def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all cricket-related things...!" + "|")
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
    print("1. T20-2024")
    print("2. IPL")
    print("3. Bangladesh tour of India, 2024")
    print("4. Back to Main Menu")

def display_series_sub_menu(series_name):
    print(f"\n{series_name} Menu:")
    print("1. Schedule & Results")
    print("2. News")
    print("3. Squads")
    print("4. Stats")
    print("5. Back to Series Menu")

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

        elif choice == '4':  # Series option
            while True:
                display_series_menu()
                series_choice = input("Enter your choice (1-4): ")
                
                if series_choice == '1':
                    while True:
                        display_series_sub_menu("T20-2024")
                        sub_choice = input("Enter your choice (1-5): ")
                        if sub_choice == '1':
                            print("Displaying T20-2024 Schedule & Results...")
                        elif sub_choice == '2':
                            print("Displaying T20-2024 News...")
                        elif sub_choice == '3':
                            print("Displaying T20-2024 Squads...")
                        elif sub_choice == '4':
                            print("Displaying T20-2024 Stats...")
                        elif sub_choice == '5':
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 5.")

                elif series_choice == '2':
                    while True:
                        display_series_sub_menu("IPL")
                        sub_choice = input("Enter your choice (1-5): ")
                        if sub_choice == '1':
                            print("Displaying IPL Schedule & Results...")
                        elif sub_choice == '2':
                            print("Displaying IPL News...")
                        elif sub_choice == '3':
                            print("Displaying IPL Squads...")
                        elif sub_choice == '4':
                            print("Displaying IPL Stats...")
                        elif sub_choice == '5':
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 5.")

                elif series_choice == '3':
                    while True:
                        display_series_sub_menu("Bangladesh tour of India, 2024")
                        sub_choice = input("Enter your choice (1-5): ")
                        if sub_choice == '1':
                            print("Displaying Bangladesh tour of India, 2024 Schedule & Results...")
                        elif sub_choice == '2':
                            print("Displaying Bangladesh tour of India, 2024 News...")
                        elif sub_choice == '3':
                            print("Displaying Bangladesh tour of India, 2024 Squads...")
                        elif sub_choice == '4':
                            print("Displaying Bangladesh tour of India, 2024 Stats...")
                        elif sub_choice == '5':
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 5.")
                        
                elif series_choice == '4':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

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
                    print("\nDisplaying Team Rankings...")
                    print("\n1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    team_ranking_choice = input("\nEnter your choice: ")
                    print("\n1. ODI Rankings")
                    print("\n2. T20I Rankings")
                    print("\n3. TEST Rankings")
                    
                    if team_ranking_choice == '1':   #1 = ODI, 2 = T20, 3 = TEST
                        print("\nDisplaying Top 10 ODI Teams...\n1    India\n2    Australia\n3    South Africa\n4    Pakistan\n5    New Zealand\n6    Sri Lanka\n7    England\n8    Bangladesh\n9    Afghanistan\n10   West Indies")
                    elif team_ranking_choice == '2':
                        print("\nDisplaying Top 10 T20 Teams...\n1    India\n2    Australia\n3    England\n4    West Indies\n5    South Africa\n6    New Zealand\n7    Pakistan\n8    Sri Lanka\n9    Bangladesh\n10   Afghanistan")  
                    elif team_ranking_choice == '3':
                        print("\nDisplaying Top 10 TEST Teams...\n1    Australia\n2    India\n3    England\n4    South Africa\n5    New Zealand\n6    Pakistan\n7    Sri Lanka\n8    West Indies\n9    Bangladesh\n10   Ireland")
                        
                        
                elif sub_choice == '2':
                    print("Displaying Player Rankings...")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")
                    
                    player_ranking_choice = input("\nEnter your choice: ")
                    print("1. ODI Rankings")
                    print("2. T20I Rankings")
                    print("3. TEST Rankings")

                    if player_ranking_choice == '1':    #1 = ODI, 2 = T20, 3 = TEST
                        print("\nDisplaying Top 10 ODI Batsmen...\n1    Babar Azam\n2    Rohit Sharma\n3    Shubhman Gill\n4    Harry Brook\n5    Fakhar Zaman\n6    Imam-ul-Haq\n7    David Warner\n8    Virat Kohli\n9    Rassie van der Dussen\n10   Aiden Markram")
                        print("\nDisplaying Top 10 ODI Bowlers...\n1    Shaheen Afridi\n2    Jasprit Bumrah\n3    Mitchell Starc\n4    Mohammed Siraj\n5    Josh Hazlewood\n6    Mujeeb Ur Rahman\n7    Rashid Khan\n8    Trent Boult\n9    Kuldeep Yadav\n10   Kagiso Rabada")       
                        print("\nDisplaying Top 10 ODI Allrounders...\n1    Shakib Al Hasan\n2    Ravindra Jadeja\n3    Mitchell Santner\n4    Ben Stokes\n5    Mohammad Nabi\n6    Glenn Maxwell\n7    Sean Williams\n8    Hardik Pandya\n9    Wanindu Hasaranga\n10   Marcus Stoinis") 
                    
                    elif player_ranking_choice == '2':   
                        print("\nDisplaying Top 10 T20 Batsmen...\n1    Suryakumar Yadav\n2    Mohammad Rizwan\n3    Babar Azam\n4    Aiden Markram\n5    Devon Conway\n6    Jos Buttler\n7    Rilee Rossouw\n8    Alex Hales\n9    David Miller\n10   Glenn Phillips")
                        print("\nDisplaying Top 10 T20 Bowlers...\n1    Rashid Khan\n2    Maheesh Theekshana\n3    Mujeeb Ur Rahman\n4    Adam Zampa\n5    Wanindu Hasaranga\n6    Anrich Nortje\n7    Shaheen Afridi\n8    Mohammad Wasim\n9    Tabraiz Shamsi\n10   Joshua Little")       
                        print("\nDisplaying Top 10 T20 Allrounders...\n1    Shakib Al Hasan\n2    Mitchell Marsh\n3    Hardik Pandya\n4    Moeen Ali\n5    David Wiese\n6    Glenn Maxwell\n7    Liam Livingstone\n8    Wanindu Hasaranga\n9    Ben Stokes\n10   Jimmy Neesham")
                    
                    elif player_ranking_choice == '3':    
                        print("\nDisplaying Top 10 TEST Batsmen...\n1    Kane Williamson\n2    Steve Smith\n3    Joe Root\n4    Marnus Labuschagne\n5    Babar Azam\n6    Travis Head\n7    Daryl Mitchell\n8    Dimuth Karunaratne\n9    Rohit Sharma\n10   Usman Khawaja")
                        print("\nDisplaying Top 10 TEST Bowlers...\n1    Ravichandran Ashwin\n2    James Anderson\n3    Pat Cummins\n4    Kagiso Rabada\n5    Ollie Robinson\n6    Nathan Lyon\n7    Ravindra Jadeja\n8    Shaheen Afridi\n9    Neil Wagner\n10   Tim Southee")       
                        print("\nDisplaying Top 10 TEST Allrounders...\n1    Ravindra Jadeja\n2    Ben Stokes\n3    Ravichandran Ashwin\n4    Shakib Al Hasan\n5    Jason Holder\n6    Mitchell Starc\n7    Pat Cummins\n8    Marco Jansen\n9    Axar Patel\n10   Dhananjaya de Silva")

                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
                    
        elif choice == '7':
            print("Exiting Cricbuzz. Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
