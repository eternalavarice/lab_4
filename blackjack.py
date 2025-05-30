import random

def draw_card():
    return random.randint(2, 11)

def hand_sum(hand):
    return sum(hand)

def show_hand(name, hand, hide_second=False):
    if hide_second:
        print(f"{name}'s hand: [{hand[0]}, ?]")
    else:
        print(f"{name}'s hand: {hand} (Total: {sum(hand)})")

def play_game():
    print("Добро пожаловать в игру!")

    # Начальные карты
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    show_hand("Игрок", player_hand)
    show_hand("Дилер", dealer_hand, hide_second=True)

    # Ход игрока
    while True:
        choice = input("Взять карту (1) или остановиться (2)? ").lower()
        if choice == '1':
            player_hand.append(draw_card())
            show_hand("Игрок", player_hand)
            if hand_sum(player_hand) > 21:
                print("Перебор. Вы проиграли.")
                return
        elif choice == '2':
            break
        else:
            print("Введите '1' (взять) или '2' (остановиться).")

    # Ход дилера
    print("\nКарты дилера открыты:")
    show_hand("Дилер", dealer_hand)
    while hand_sum(dealer_hand) < 17:
        print("Дилер берёт карту...")
        dealer_hand.append(draw_card())
        show_hand("Дилер", dealer_hand)

    player_total = hand_sum(player_hand)
    dealer_total = hand_sum(dealer_hand)

    print("\nИтог:")
    print(f"Сумма игрока: {player_total}")
    print(f"Сумма дилера: {dealer_total}")

    # Определение победителя
    if dealer_total > 21:
        print("Дилер перебрал! Вы выиграли!")
    elif player_total > dealer_total:
        print("Вы ближе к 21! Победа!")
    elif player_total < dealer_total:
        print("Вы проиграли.")
    else:
        print("Ничья.")

# Запуск
play_game()
