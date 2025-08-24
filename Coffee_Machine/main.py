print('''                                                                                                              
 ===-==-+==--------=++***+==---===---::-:--::=*#@@%%%####%%###*=-::-+:.:.  .:.::::.:----:     :::. ..--=---= 
 +==+=-:-==-:::-=====++=======-:-==+=-:-#@@@@%=                -=+*#*--:... .:::.:.::.::.:-::::...::..:----= 
 =++++**+-==+*+=-++++=====-=====+===+@@@@      .-+###%%%%%%%#+:      ++#*---:.-:.:::.:...:::..:::..::::----- 
 +==+++==---======-==--==++===++++%@@+    :=++=++---====+++**%@@@@%#-   :##*-::---:-:--=-. :=-----===---==== 
 +====++=*+++==+++++=++++==+==++@@@    -==--::                :-+**#@@@*   +@*-..:::::----=--:-----:-=--==== 
 ***++++*+++++++++++++++++=+++#@@    -::.        =*+%%%%%%%#*:      =+*#@%-  *@#------:--:--==--::-=----==== 
 +*++++=*=++**+*+++**++++++*+#@@   :..     :%@@@@@@@@@@@@@@@@@@@@@#.   :++#%:  @%=-=---=---:----:-=--==---== 
 +**+**#***#*+++****+++***++#@.  .      %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=   :+%=  %@*===-=--+-=--==---======-= 
 *****+*+**+**++**+++*++++%@@@   .    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   -**  =@===-==---===--==:---===== 
 *********++*+***+******%@@+    .   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-  -#-  @@#====-=---===-=====--=-= 
 ******+**#*******+****@@%  *      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   =    @@*====-============+==+ 
 ****#***#***********%@@   .+.    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% :%   + :@@*==++=====+========+ 
 *****##**#******#**#@@      %   +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .*       @@@@#====+++++++=++== 
 #####**##**#***#*#%@@  ..   @=  :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=           -@@*++==++=+=++=++ 
 ##########*###*#*#@@  ..     @*  :+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    =:-::-:   #@++++++=+++++++ 
 ########*########@@  :        @%    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   -@@@@@@@@+   @++===+++++++++ 
.##%##%#%#@@%%####@# .          @@*   -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   -=@        @@= @*+++++++++++*+ 
:#%#####@@@@@@@@@%@    #-        #@@#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @=          .%=+%++*+++++*+**+* 
.#######@      @@@@     :         :%@@@.    -@@@@@@@@@@@@@@@@@@@@@@@@     :#@          :-%* @#+++++++****+++ 
:%%%%%%%@@@         * +   ..::      =%@@@@#         .*@@@@@%=         :#@#+=::+%%#*=::-*%+  @*****+*++++++*+ 
=%#%%%%%%@@@@@@@:       .+#+:. ..    %+*##@@@@@@#-              -#@@@@*=--=*%#+===*@@@@@@@  @*************** 
=%%%%%%%%%%##%@@@@@@@@@-              %#=*#***#%@@@@@@@@@@@@@@###++=-::::       .+@@@%=.    @++**+*+*+****** 
+@@%%%%%%%%%%%%###%+.@@:%@@@@@+*@+     .%=-+***++++=---------:-----:.... .:=+#%@%@@#-      @@*******+******+ 
*%%@%%@@@@%@@%%%@%@@  #@%     .+#@@@@@@   =--=+++++*****+++++==-:.   -==++*#%%%%#+.   -    @%*##**#*##***##* 
*@@%%%%%%###%%%@@%%@@   #@#.         -@@@@+ :..--=+===+==----:.   =##*+***##*++-.    ..   @@****#******#**** 
*@%@@@@@@@@@@@%%%%@@@@    *@%#-:.:-::    *@@@%##+-        .--+#%%%#********+-:.   ..:==  @@#**#*#*#**#***#*# 
#@@@@@@@@@@@@@@@%@@%@@@:   . =.%=. ::-++-. +@@@@@@@@@@@@@@+   :=+=++++++=-::.:::. :--:  @@%#%%####**##*##### 
%@@@%%%@@@%@@@@@@@@@@@@@@   . . *@#=. .-+++--@@%@@@@@@@@%%@@@@.  .====--::::-.   -=-   @@%#####*#*%#*###*##* 
%@@@@@@@@@@@@@@@@@@@@@@@@@-      .=%@#+::===-:@@@@@@@@@@@@@#%@@@@:.----::::   .-+-   %@@%################*##.
#@@@@@@@@@@@@@@@@@@@@@@@@@@@.       .-+*#*#%#+..@@@@@@@%%%#%@@@@@@=---:..  :.:=:    @@@###%%%###%#*#%%%#####.
%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+     .:--====+#%#*+*=%@@@@@@@@#  ::..   .-: ..    @@@@%%#%###%%%%####*#######:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=       .:----=+*@@@@@@@@@@@@*:.  .:-:        @@@@@@@%#%%#######*#%%######%:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                           .         +@@@@@@@@%%%%%%%%#%#%%##%%##%%##%:''')
MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
    "cost":1.5,
    },
    "lattle":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources={
    "water":1000,
    "milk":1000,
    "coffee":1000,
}

#Creating a dunvtion to check the resources
def is_resourse_sufficient(order_ingridients):
    for i in order_ingridients:
        #Any ingredients is not sufficient
        if order_ingridients[i]>=resources[i]:
            print(f"Sorry There is not enough {i}")    
            return False
    return True

#Check if transaction is successful
def is_transaction_success(money_received,drink_cost):
    if money_received>=drink_cost:
        #Round the number to 2 decimal places
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global money
        money+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
        
def make_coffee(drink_name,order_ingridients):
    #Deduct the required ingredients from the resources
    for i in order_ingridients:
        resources[i]-=order_ingridients[i]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


money=0
is_on=True
#Asking user 
while is_on:
    user_choice = input("What would you like: ").lower().strip()
    if user_choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if user_choice not in MENU:
            print("Invalid choice. Please select a valid drink.")
            continue
        user_quantity = int(input("How many cups would you like?: "))
        coffee = MENU[user_choice]
        # Multiply ingredients by quantity
        required_ingredients = {k: v * user_quantity for k, v in coffee["ingredients"].items()}
        # Check resources
        if is_resourse_sufficient(required_ingredients):
            print("Insert Coins")
            total_cost = coffee["cost"] * user_quantity
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01
            money_received = quarters + dimes + nickles + pennies
            if is_transaction_success(money_received, total_cost):
                make_coffee(user_choice, required_ingredients)






