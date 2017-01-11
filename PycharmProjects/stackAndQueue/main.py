from queue import Daily_Tasks


def main():

    d_o_t_o = Daily_Tasks()

    while True:
        d_o_t_o.print_menu()

        menu_choice = int(input("Enter your menu choice > "))

        if menu_choice == 1:
            d_o_t_o.view()
        elif menu_choice == 2:
            d_o_t_o.push()
        elif menu_choice == 3:
            d_o_t_o.pop()

main()