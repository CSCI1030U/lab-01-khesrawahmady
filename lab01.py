def main(): 
# YOUR CODE FOR PART 1 GOES HERE  
    cost_per_item = 19.99
    quantity = 5 
    subtotal_cost = quantity * cost_per_item
    tax= 13/100 * subtotal_cost
    total_cost= tax+subtotal_cost

# YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print(f'After 5 years, your investment will be worth {investment} dollars.')


if __name__ == "__main__":
    main()