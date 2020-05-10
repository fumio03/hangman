import Comp
import Stages

wrong = 0

print("Welcome Hangman Game!")
Answer = Comp.start()
Answer_list = list(Answer)
#print(Answer)
Secret_answer = Comp.secret_ans(Answer)
print("Now I set the Secret_word: '{}'".format(Secret_answer))

while wrong < len(Stages.stage):
    input_char = input("Guess one character in Secret_word:")
    index_num = Comp.comparison(input_char,Answer_list)
    judge = Comp.rename_secret_ans(index_num,Secret_answer,input_char)
    Comp.rename_ans(index_num,Answer_list,y="$")
    if judge is None:
        wrong +=1
        Stages.drow_stage(wrong)
    elif "_" not in Secret_answer:
        print("Great You win! Just {} times wrong.".format(wrong))
        break

if wrong == len(Stages.stage):
    print("You loose..Collect Answer is {}.".format(Answer))



