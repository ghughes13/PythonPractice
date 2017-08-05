people = {"Monty Python": "01/05/1984"}


def main():
    do_this = int(input("What would you like to do? \n"
                    "1) Add a birthday \n"
                    "2) Search for a birthday \n"
                    "3) Quit \n"))

    if do_this == 1:
        add()
    elif do_this == 2:
        show()
    elif do_this == 3:
        print("Thank's for playing!")
        exit()
    else:
        print("That wasn't a choice. Please use 1,2, or 3. ")
        main()


def show():
    print("We have birthday's stored for: ")
    for key in people.keys():
        print('- ' + key)
    print("Who's do you want to display?")
    display = input(">> ")
    try:
        print("\n" + display + "'s birthday is " + people[display])
    except KeyError:
        print("Whoops looks like that wasn't a valid choice. Remember your input is case sensitive, currently.")
        show()
    print('\n')
    main()


def add():
    name = input("What's the name of the person you want to add?")
    date = input("When is their birthday? MM/DD/YYYY format: ")
    people.update({name:date})
    print("It has been added.")
    main()

main()