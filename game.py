def quiz():
    print("\n-----Welcome To Brainiac Masters-----\n")
    print("\n-----Round 1 Starts-----\n")

    # Round 1 questions, options, answers, and prize money
    round1Questions = [
        "Which planet is known as the Red Planet?",
        "What is the capital city of France?",
        "Which animal is known as man's best friend?",
        "What is the largest mammal in the world?",
        "What do you call a baby lion?"
    ]
    round1Options = [
        ["A. Jupiter", "B. Earth", "C. Mercury", "D. Mars"],
        ["A. Berlin", "B. Madrid", "C. Paris", "D. Italy"],
        ["A. Parrot", "B. Horse", "C. Dog", "D. Cat"],
        ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        ["A. Cub", "B. Calf", "C. Foal", "D. Kid"]
        
    ]
    round1Answers = ["D","C","C","B","A"]  # Add Round 1 answers
    round1PrizeMoney = [10000, 20000, 30000, 40000, 50000]  # Add Round 1 prize money
    amount = 0
    score = 0
    Round = 1

    for q, ans, prize in zip(round1Questions, round1Answers, round1PrizeMoney):
        print(q)
        for option in round1Options[round1Questions.index(q)]:
            print(option)
        User = input("Enter Your Answer : ").upper()

        if User == ans:
            print(f"Congratulations! Your answer is correct. You've won Rs. {prize}")
            amount += 10000
        else:
            print("Sorry, Your answer is wrong. Better Luck Next Time :)")
            print(f"You've Won A Total Of Rs. {amount}")
            return amount

        score += 1
        if score % 5 == 0 and Round == 1:
            print(f"---->Congratulations! you have passed to Round {Round+1}<----")
            Round += 1

    print(f"You've completed Round 1 and won a total of Rs. {amount}")
    print("\n-----Round 2 Starts-----\n")

    # Round 2 questions, options, answers, and prize money
    round2Questions = [
        "In which year did World War II end?",
        "Who painted the famous artwork 'Mona Lisa'?",
        "Which country is the largest by land area?",
        "What is the chemical symbol for gold?",
        "Who is the author of the Harry Potter book series?"
    ]
    round2Options = [
        ["A. 1943", "B. 1945", "C. 1947", "D. 1950"],
        ["A.  Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D.  Michelangelo"],
        ["A. Russia", "B. Canada", "C. China", "D. United States"],
        ["A. Au", "B. Ag", "C. Pt", "D. Gl"],
        ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. C.S. Lewis", "D. Stephenie Meyer"]
    ]
    round2Answers = ["B", "C", "A", "A", "B"]  # Add Round 2 answers
    round2PrizeMoney = [60000,70000,80000,90000,100000]  # Add Round 2 prize money
    score = 0

    for q, ans, prize in zip(round2Questions, round2Answers, round2PrizeMoney):
        print(q)
        for option in round2Options[round2Questions.index(q)]:
            print(option)
        User = input("Enter Your Answer : ").upper()

        if User == ans:
            print(f"Congratulations! Your answer is correct. You've won Rs. {prize}")
            amount += 10000
        else:
            print("Sorry, Your answer is wrong. Better Luck Next Time :)")
            print(f"You've Won A Total Of Rs. {amount}")
            return amount

        score += 1
        if score % 5 == 0 and Round == 2:
            print(f"---->Congratulations! you have passed to Round {Round+1}<----")
            Round += 1

    print(f"You've completed Round 2 and won a total of Rs. {amount}")
    print("\n-----Round 3 Starts-----\n")

    # Round 3 questions, options, answers, and prize money
    round3Questions = [
        "Which scientist formulated the theory of general relativity?",
        "What is the chemical formula for ozone?",
        "Which artist painted the famous work 'The Starry Night'?",
        "What is the smallest bone in the human body?",
        "Which country is the largest producer of coffee in the world?"
    ]
    round3Options = [
        ["A. Issac Newton", "B. Albert Einstein", "C. Stephen Hawking", "D. Niels Bohr"],
        ["A. O1", "B. O6", "C. O3", "D. O9"],
        ["A. Michelangelo", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Vincent van Gogh"],
        ["A. Stapes", "B. Femur", "C. Radius", "D. Tibia"],
        ["A. Saudi Arabia", "B. Brazil", "C. Colombia", "D. Ethiopia"]
        
    ]
    round3Answers = ["B", "C", "D", "A", "B"]  # Add Round 3 answers
    round3PrizeMoney = [110000,120000,130000,140000,150000]  # Add Round 3 prize money
    score = 0

    for q, ans, prize in zip(round3Questions, round3Answers, round3PrizeMoney):
        print(q)
        for option in round3Options[round3Questions.index(q)]:
            print(option)
        User = input("Enter Your Answer : ").upper()

        if User == ans:
            print(f"Congratulations! Your answer is correct. You've won Rs. {prize}")
            amount += 10000
        else:
            print("Sorry, Your answer is wrong. Better Luck Next Time :)")
            print(f"You've Won A Total Of Rs. {amount}")
            return amount

        score += 1
        if score % 5 == 0 and Round == 3:
            print(f"---->Congratulations! you have completed the game yah!<----")
            

    print(f"You've won a total of Rs. {amount}")
    return amount

# Call the function to start the game
quiz()
