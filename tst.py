def display_welcome_message():
    print("+" + "-"*38 + "+")
    print("|" + " " * 11 + "Welcome to Cricbuzz" + " " * 11 + "|")
    print("|" + " " * 38 + "|")
    print("|" + "Your one-stop destination for all cricket related things...!" + "|")
    print("+" + "-"*38 + "+")
    print()
#hii
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
                        print("\nDisplaying Top 10 ODI Batsmen...\n1    Babar Azam\n2    Rohit Sharma\n3    Shubhman Gill\n4    Harry Tector\n5    Virat Kohli\n6    Daryl Mitchell\n7    David Warner\n8    Pathum Nissanka\n9    Dawid Malan\n10   Rassie van der Dussen")
                    elif player_ranking_choice == '2':    #1 = ODI, 2 = T20, 3 = TEST
                        print("\nDisplaying Top 10 T20 Batsmen...\n1    Travis Head\n2    Surya Kumar Yadav\n3    Philip Salt\n4   Yashasvi Jaiswal\n5    Babar Azam\n6    Mohammad Rizwan \n7    Jos Butler\n8    Ruturaj Gaikwad\n9    Brandon King\n10   Johnson Charles")
                    elif player_ranking_choice == '3':    #1 = ODI, 2 = T20, 3 = TEST
                        print("\nDisplaying Top 10 TEST Batsmen...\n1    Joe Root\n2    Kane Williamson\n3    Babar Azam\n4    Daryl Mitchell\n5    Steven Smith\n6    Rohit Sharma\n7    Harry Brook\n8    Yashasvi Jaiswal\n9    Dimuth Karunaratne\n10   Virat Kohli")

                        
                    elif sub_choice == '3':
                        break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
    
1
