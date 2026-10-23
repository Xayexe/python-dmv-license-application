# DMV License Application System
import random  # lets us roll random numbers, like dice in a game

# Function to hide most of the SSN (keep only last 4 digits visible)
def hide_ssn(ssn): 
    return "***-**-" + ssn[-4:] # keep only last 4 digits visible

# Function to ask the user for their details
def collect_applicant_details():
    # Ask for name
    while True:
        name = input("Full Name: ").strip()
        if name:  # make sure it's not empty
            break
        print("Name cannot be empty. Please try again.")

    # Ask for date of birth
    while True:
        dob_string = input("Date of Birth (YYYY-MM-DD): ").strip() #
        # Check if format looks like YYYY-MM-DD
        if len(dob_string) == 10 and dob_string[4] == '-' and dob_string[7] == '-':
            year, month, day = dob_string.split('-') # split into parts
            if year.isdigit() and month.isdigit() and day.isdigit():
                year, month, day = int(year), int(month), int(day)
                # Check if numbers make sense
                if 1900 <= year <= 2025 and 1 <= month <= 12 and 1 <= day <= 31: # format for years so they are realistic 
                    break
        print("Invalid date format. Please use YYYY-MM-DD (example: 2000-05-15).")

    # Ask for address
    address = input("Address: ").strip()

    # Ask for SSN
    while True:
        ssn = input("Social Security Number (XXX-XX-XXXX): ").strip()
        if len(ssn) == 11 and ssn.replace("-", "").isdigit(): # checks if the SSN is in the correct format replaces the dashes with nothing and checks if the rest are digits
            break
        print("Invalid SSN format. Please try again.")

    return {
        "name": name, 
        "dob": dob_string,
        "address": address,
        "ssn": ssn
    } #assigns these strings to these variables and returns them as a dictionary

# Function to calculate age
def calculate_age(dob_string):
    year, month, day = map(int, dob_string.split('-')) # split the date of birth into parts
    # the map function applies the int function to each part of the split result
    # For simplicity, we use a fixed "today" date
    today_year, today_month, today_day = 2025, 10, 2 # multiple strings assigned to multiple variables
    age = today_year - year
    # If birthday hasn't happened yet this year, subtract 1
    if (today_month, today_day) < (month, day):
        age -= 1
    return age

# Function to check if someone is old enough
def check_eligibility(dob_string):
    age = calculate_age(dob_string) # calculate the age from the date of birth
    return age >= 16, age  # returns two things: (eligible or not, and age)

# Function to let user pick license type
def select_license_type():
    print("\nSelect License Type:")
    print("1. Learner’s Permit")
    print("2. Standard Driver’s License")
    print("3. Commercial License")

    while True:
        choice = input("Enter option number (1-3): ").strip() # no extr spaces 
        if choice == "1":
            return "Learner’s Permit" # prints the type of license
        elif choice == "2":
            return "Standard Driver’s License"
        elif choice == "3":
            return "Commercial License"
        else:
            print("Invalid option. Please type 1, 2, or 3.")

# Function to make a random application ID
def generate_application_id():
    return "DMV" + str(random.randint(100000, 999999))# random number between 100000 and 999999 and turns the randomized number into a string

# Function to show the application summary
def display_summary(applicant, license_type, eligible, age, app_id): # all the stuff we want to show in the summary

    print("\n--- Application Summary ---")
    print(f"Application ID: {app_id}")
    print(f"Name: {applicant['name']}") 
    print(f"Date of Birth: {applicant['dob']} (Age: {age})") 
    print(f"Address: {applicant['address']}")
    print(f"SSN: {hide_ssn(applicant['ssn'])}")  # hide most of the SSN
    print(f"License Type: {license_type}")
    print(f"Eligibility Status: {'Approved' if eligible else 'Not Eligible'}")
    print("----------------------------\n")

# Function to save applications to a text file
def save_to_file(applications):

    with open("dmv_applications.txt", "w") as f: # opens the file in write mode
        for app in applications:
            f.write(str(app) + "\n")  # write each application on a new line
            

# Main function (the main game loop)
def main():
    applications = []  # empty list to store applications
    while True:
        print("=== DMV New License Application ===")
        applicant = collect_applicant_details() #sets the applicant variable to the function that collects details
        eligible, age = check_eligibility(applicant["dob"]) #sets the eligible and age variables to the function that checks eligibility
        license_type = select_license_type() #sets the license type variable to the function that selects license type
        app_id = generate_application_id() #sets the application id variable to the function that generates application id
        display_summary(applicant, license_type, eligible, age, app_id)

        # Save this application into the list
        applications.append({
            "Application ID": app_id,
            "Name": applicant["name"],
            "DOB": applicant["dob"],
            "Age": age,
            "Address": applicant["address"],
            "SSN": hide_ssn(applicant["ssn"]),
            "License Type": license_type,
            "Eligibility": "Approved" if eligible else "Not Eligible"
        })

        # Ask if the user wants to do another one
        again = input("Process another application? (Y/N): ").strip().lower()
        if again != "y":
            break

    # Save everything to a file at the end
    save_to_file(applications)
    print("All applications saved to dmv_applications.txt.")

# Start the program
if __name__ == "__main__":
    main()
