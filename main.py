from player import Player
from computer import Computer


def main():
    player = Player()
    computer = Computer()

    print("Welcome to Simple Turn Based Game")
    print("Featuring a simple A.I.\n")

    while 1:
        while 1:
            print("Press q to quit at any time\n")
            # Give player choices
            print("1. Weak Attack")
            print("2. Strong Attack")
            print("3. Heal")
            print("4. Improve Attack")
            print("5. Improve Defense")
            print("6. Show Health\n")
            choice = input(": ")
            print()

            if choice == 'q':
                print("Exiting...")
                return
            elif choice == '1':
                computer.atked_weak()
                break
            elif choice == '2':
                computer.atked_strong()
                break
            elif choice == '3':
                player.heal()
                break
            elif choice == '4':
                computer.imp_player_atk()
                break
            elif choice == '5':
                player.imp_def()
                break
            elif choice == '6':
                win_cond(player, computer)
            else:
                print("That is not an option.\n")

        print()
        if win_cond(player, computer):
            return

        print()

        # AI's turn
        computer.move(player.hp)

        if win_cond(player, computer):
            return
        print("\n")
        

def win_cond(player, computer):
    if player.hp <= 0:
        print("Player HP: 0")
        print("Computer HP:", computer.hp)
        print("\nComputer Wins!\n")
        return 1
    elif computer.hp <= 0:
        print("Player HP:", player.hp)
        print("Computer HP: 0\n")
        print("You Win!\n")
        return 1
    else:
        print("Player HP:", player.hp)
        print("Computer HP:", computer.hp)
        return 0

if __name__ == '__main__':
    main()
