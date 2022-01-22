import requests


def get_inputs():
    link = input("Enter your profile views link\n:- ")
    number = int(input("Enter how many views you need\n:- "))  # You can change to None for unlimited views
    return link, number


def hack(link):
    return requests.get(link)


def main(total=0):
    link, number = get_inputs()
    print("Hacking Started")
    while True:
        hack(link)
        total += 1
        print(total, "views successfully")
        if number and total >= number:
            print("\nHacked successfully\n")
            again = input("\nIf you need hack again?\ny for yes and n for no\n:- ")
            if again == 'y':
                return main()
            else:
                print('\nThanks for using.\n')
                break


main()