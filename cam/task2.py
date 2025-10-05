import random

def play_dice_game():
    roll = random.randint(1, 6)
    print(f"Cube value: {roll}")
    if roll in [5, 6]:
        print("You win!")
        return
    elif roll in [3, 4]:
        print("Rerolling...")
        play_dice_game()
    elif roll in [1, 2]:
        print("You lose!")
        return

if __name__ == '__main__':
    print("--- Recursive Dice Game ---")
    play_dice_game()