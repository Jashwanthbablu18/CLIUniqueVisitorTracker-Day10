# Day 10 - Unique Visitor Tracker
# Topic: Sets and Frozensets

#This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🌐 Welcome to Day 10 of Python 30-Day Challenge!")
    print("🔹 Topic: Sets & Frozensets")
    print("🧾 Tracking unique web visitors in a simulation\n")

# This function takes user ID's as input and stores them, takes day_num as a parameter of this function.
def simulate_day_visits(day_num):

    # Creates unique visitors set using set constructor.
    unique_visitors = set()
    
    # This loop runs until user enters the text 'done' and takes visitors ID as an input.
    while True:

        # Asks user for input and removes all extra spaces.
        user_id = input(f"👤 Enter visitor ID for Day {day_num} (or type 'done' to stop): ").strip()
        
        # if user enters the id as 'Done' or 'DONE' converts it into "done" and breaks the loop here.
        if user_id.lower() == 'done':
            break

        # Even if they enter the same ID twice, set keeps it clean
        unique_visitors.add(user_id)
        print(f"✅ Visitor '{user_id}' recorded. So far: {len(unique_visitors)} unique")

    # Displays the vistiors ID's of day-01 which consists of only unique visitors ID's.
    print(f"\n📊 Summary for Day {day_num}:")
    print("👥 Visitors Set:", unique_visitors)

    # Locking the set as a snapshot and cannot be edited.
    frozen_snapshot = frozenset(unique_visitors)
    print("❄️ Frozen Snapshot:", frozen_snapshot)

    # returns the unique set 
    return frozen_snapshot

# This function compares the visitors of Day-01 and Day-02, takes Day-01 and Day-02 as parameters into function.
def compare_visits(day1_set, day2_set):

    # Displays visitors comparision msg.
    print("\n📈 Visitor Comparison Between Days")

    # This finds people who came on Day-02 but not on Day-01 (New visitors). This is set difference.
    new_people = day2_set - day1_set

    # This finds people who came on Day-01 and Day-02 (Returning visitors). This is set intersectio.
    returning_people = day1_set & day2_set

    # This combines both days and removes duplicates. This is set union.
    all_visitors = day1_set | day2_set

    # Displays the output if it isn't empty else displays None.
    print("➕ New on Day 2:", new_people if new_people else "None")
    print("🔁 Returning Visitors:", returning_people if returning_people else "None")
    print("🧾 Total Unique Across Both:", all_visitors)

# main
def main():

    # Calls show_intro() to display the introduction of this assignment / project.
    show_intro()
    
    # This displays tracking for day-1. And passes '1' as a parameter into simulate_day_visits() to track day-1's visitors by calling simulate_day_visits() and passing '1' as a parameter.
    print("\n📅 Tracking for Day 1")
    day1_data = simulate_day_visits(1)

    # This displays tracking for day-2. And passes '2' as a parameter into simulate_day_visits() to track day-2's visitors by calling simulate_day_visitors() and passing '2' as a parameter.
    print("\n📅 Tracking for Day 2")
    day2_data = simulate_day_visits(2)

    # This compares the day-01 and day-02 visitors data and displays new visitors data, returning visitors data and combined day1 and 2 visitors data.
    compare_visits(day1_data, day2_data)

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
