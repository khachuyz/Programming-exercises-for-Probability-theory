from random import randint as rd


trials = 1000
keep = 0
change = 0
change_half = 0
for i in range(trials):
    choices = [1,2,3]
    car = rd.randint(1,3)
    player = rd.randint(1,3)
    swap  = rd.randint(0,1) 
    if car == player:
        keep += 1
        if swap == 0:
            change_half += 1
    else:
        change += 1
        if swap == 1:
            change_half += 1

def main():
    print(f"Keep the decision:   {str(keep/trials)}")
    print(f"Change the decision: {str(change/trials)}")
    print(f"All the same:        {str(change_half/trials)}")

if __name__ == "__main__":
    main()
    
