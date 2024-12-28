def add(salary, bonus):
    return salary + bonus

def get_salaries():
    while True:
        try:
            salaries = input("enter salaries separated by space (ex: 2000 1500) : ")
            return [int(salary) for salary in salaries.split()]
        except ValueError:
            print("invalid entry. Please enter an integer")

def get_bonus():
    while True:
        try:
            bonus = int(input("enter the bonus to add (integer number) : "))
            return bonus
        except ValueError:
            print("invalid entry. Please enter an integer")



def save_to_file(salaries, filename = ""): # filename = "put your file name here"
    if not filename:
        print("Error: filename is not define")
        print("Please modify the code to include a valid filename")
        return
    if "." not in filename:
        filename += ".txt"

    try:
        with open(filename, "w") as file:
                file.write("salaries updated after bonus added :\n")
                file.write("=" * 40 + "\n")
                for salary in salaries:
                    file.write(f"{salary}\n")
        print(f"the updated salaries have been saved to the file '{filename}'")
    except Exception as e:
        print(f"Error while saving : {e}")

def main():
    print("Welcome to the salaryBoost app!")
    print("=" * 40)

    salaries = get_salaries()
    print("initial salaries", salaries)

    bonus = get_bonus()
    print(f"\nadded a bonus of {bonus} to each salary...")

    updated_salaries = [add(salary, bonus) for salary in salaries]
    print("salaries after adding bonus : ", updated_salaries)

    save_to_file(updated_salaries)

if __name__== "__main__":
    main()
