print("Welcome To our HangMan Game : ")
password = "AmoAboKhozayem"
password_letters = list(password)
user_list = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_",]
current_index = 0
lives = 5
failed = 0
trails = len(password_letters) + 5
def game(password_letters,failed,current_index,lives,user_list,trails):
    if trails > 0 :
        user_input = input("Enter the letter : ")
        trails-=1
        if user_input in password_letters:
            if user_input not in user_list:
                print(f"Correct, The word has : {user_input}")
                check(user_input,password_letters,current_index,user_list)
                if user_list == password_letters:
                    print(user_list)
                    print(f"Congratulations, You Got it the passwors was : {password}")
                    quit()
                else:
                    failed = 0
                    print(user_list)
                    print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
                    game(password_letters,failed,current_index,lives,user_list,trails)
            else:
                print(f"the letter '{user_input}' is already added.")
                game(password_letters,failed,current_index,lives,user_list,trails)
        else:
            failed+=1
            print("TRYAGAIN~~~")
            if failed == 2:
                lives-=1
                print("You entered two incorrect following so, your lives decreased")
                print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
                failed = 0
                game(password_letters,failed,current_index,lives,user_list,trails)
                if lives == 0:
                    print("Your lives reached to '0', You Lose~~~")
                    quit()
            else:
                print(f"Your Score is => Trails : {trails} , Lives : {lives} , Failed : {failed}")
                game(password_letters,failed,current_index,lives,user_list,trails)
    else:
        print("Your trails reached to '0', You Lose~~~")
        quit()

def check(user_input,password_letters,current_index,user_list):
    if user_input == password_letters[current_index]:
        user_list[current_index] = user_input
        if current_index < len(password_letters)-1:
            current_index+=1
            check(user_input,password_letters,current_index,user_list)
        else:
            current_index = 0
    else:
        if current_index < len(password_letters)-1:
            current_index+=1
            check(user_input,password_letters,current_index,user_list)
        else:
            current_index = 0



game(password_letters,failed,current_index,lives,user_list,trails)