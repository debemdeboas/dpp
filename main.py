from solutions.leftie import solution___at_least_one_leftie
from solutions.tanenbaum import solution__tanenbaum


MENU = \
'''***  DPP SOLUTIONS  ***
To stop execution, press any key\n
--- Choose your desired solution approach ---
\t1: Leftie solution
\t2: Tanenbaum solution'''

print(MENU)
if (choice := input('> ')).isdigit():
    if choice == '1':
        solution___at_least_one_leftie()
    elif choice == '2':
        solution__tanenbaum()
    else:
        print('Invalid choice :(')
        exit(1)
else:
    print('Please only input numbers')
    exit(2)
