
if __name__ == "__main__":
    prev_guess = 50
    guess = 50
    lb = 1
    ub = 100
    while True:
        hi_low = input("Current guess is:"+str(guess)+"\n (h)igher, (l)ower, (y)es, or (q)uit?: ")
        if hi_low == "h":
            lb = guess
            if guess == 99:
                guess = 100
                print("Your number is "+str(guess))
                exit()
        elif hi_low == "l":
            ub = guess
        elif hi_low == "y":
            print("Your number is "+str(guess))
            exit()
        elif hi_low == "q":
            print("you exited lel")
            exit()
        else:
            print("valid input lel")
            guess = prev_guess
        prev_guess = guess
        guess = int((ub + lb) / 2)