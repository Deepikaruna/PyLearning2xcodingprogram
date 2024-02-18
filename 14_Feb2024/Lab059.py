def make_pizza(*toppings, base):
    print(toppings, base)
    for topping in toppings:
        print(topping)


make_pizza("onion", "tomato", "sweetcorn", base="thin crust")
