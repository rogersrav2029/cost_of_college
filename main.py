"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost
    


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthly_cost = annual_cost / MONTHS_PER_YEAR
    return monthly_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    daily_cost = annual_cost / CLASS_DAYS_PER_SEMESTER / 2
    return daily_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost / credits / 2
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = annual_cost / CS1430_MEETINGS_PER_SEMESTER * CS1430_CREDITS / credits / 2
    return class_cost

def cost_of_skipped_classes(annual_cost, credits, skipped_classes):
    """Give back what the cost of skipped classes is. skipped_classes is the number of classes skipped this semester."""
    skipped_cost = annual_cost / credits / 2 * skipped_classes
    return skipped_cost


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the annual cost of college: $"))
    credits = float(input("Enter the number of credits for this semester: "))
    skipped_classes = float(input("Enter the number of classes skipped this semester: "))

    while True:
        semester_cost = cost_per_semester(annual_cost)
        monthly_cost = cost_per_month(annual_cost)
        daily_cost =  cost_per_day(annual_cost)
        credit_cost = cost_per_credit(annual_cost, credits)
        class_cost = cost_per_class(annual_cost, credits)
        skipped_cost = cost_of_skipped_classes(annual_cost, credits, skipped_classes) 

        choice = input("Choose an option: ")
        if choice == "1":
            print(f"Cost per semester: ${semester_cost:.2f}")
        elif choice == "2":
            print(f"Cost per month: ${monthly_cost:.2f}")
        elif choice == "3":
            print(f"Cost per day: ${daily_cost:.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${credit_cost:.2f}")
        elif choice == "5":
            print(f"Cost per class: ${class_cost:.2f}")
        elif choice == "6":
            print(f"Cost of skipped classes: ${skipped_cost:.2f}")
        elif choice == "Q":
            break



# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
