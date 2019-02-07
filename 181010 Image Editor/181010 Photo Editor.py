from Image_Library import *


menu_list = {
        1: "Rotate 90 clockwise.",
        2: "Rotate 90 anti-clockwise.",
        3: "Custom rotation.",
        4: "Print a histogram.",
        5: "Quit"
    }



def menu(options):
    print("--== Welcome to the Image Manipulator 3000! ==--")
        
    #prints the menu_list dictionary
    for x in options:
        print(str(x) + ":", str(options[x]))

    #tests to check the choice is a valid int.
    correct = False
    while not correct:
        try:
            choice = int(input("\nPlease enter your choice: "))
            
            #checks if the int is in the menu_list dictionary.
            if choice in options:
                correct = True
                return choice
            else:
                print("***Enter a correct choice!***")

        except ValueError:
            print("***Enter a valid number!***")
        except:
            print("***Unexpected Error!!***")



def selected(choice):
    print("\n*Selected: {}*".format(menu_list[choice]))



def filename():
    #check the filename is correct, turns the validated filename.
    filename = ""
    while filename == "":
        filename = input("Please enter a filename: ")
        return filename
        

            


def main():
    while True:

        #parameter menu_list. So it can use the dictionary inside the def. 
        choice = menu(menu_list)
        
        if choice == 1:
            selected(choice)
            file = filename()
        
            try:
                rotate_90_clockwise(file)
            except FileNotFoundError:
                print("\n\n***** File specified not found! *****")
                print("Returning to main menu\n\n")
            except OSError:
                print("\n\n***** File error! *****")
                print("Returning to main menu\n\n")
                
            except:
                print("\n\n***** Unknown Error *****")
                print("Returning to main menu\n\n")
                


        
        elif choice == 2:
            selected(choice)
            file = filename()

            try:
                rotate_90_anticlockwise(file)
            except FileNotFoundError:
                print("\n\n***** File specified not found! *****")
                print("Returning to main menu\n\n")
            except OSError:
                print("\n\n***** File error! *****")
                print("Returning to main menu\n\n")
                
            except:
                print("\n\n***** Unknown Error *****")
                print("Returning to main menu\n\n")
                
                
            


        elif choice == 3:
            selected(choice)
            file = filename()
            
            try:
                custom_rotation(file)
            except FileNotFoundError:
                print("\n\n***** File specified not found! *****")
                print("Returning to main menu\n\n")
            except OSError:
                print("\n\n***** File error! *****")
                print("Returning to main menu\n\n")
                main()
            except:
                print("\n\n***** Unknown Error *****")
                print("Returning to main menu\n\n")
                



        elif choice == 4:
            selected(choice)
            file = filename()
            
            try:
                histogram(file)
            except FileNotFoundError:
                print("\n\n***** File specified not found! *****")
                print("Returning to main menu\n\n")
            except OSError:
                print("\n\n***** File error! *****")
                print("Returning to main menu\n\n")
                
            except:
                print("\n\n***** Unknown Error *****")
                print("Returning to main menu\n\n")
                


            
        elif choice == 5:
            return False
            exit

        print()
        print()




###MAIN PROGRAM STARTS HERE###
main()

