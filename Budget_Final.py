

class Category:

    def __init__(self, name):
        self.ledger = list()
        self.name = name


    def __str__(self):
        title = f"{self.name:*^30}\n" # ':*^30' allows for center align
        items = '' 
        total = 0 

        for item in self.ledger: 
            items += f"{item['description'][0:23]:23}" + f"{item['amount']: > 7.2f}" + '\n'

            total += item['amount']
        
        output = title + items + 'Total: ' + str(total)
        return str(output)     
    # Deposit money into account 
    def deposit ( self, amount , description = ''):
        self.ledger.append ({'amount': amount , 'description': description})
    
    # Withdraw money from an account
    # If amount withdrawn is larger than account value transaction does not go through
    def withdraw ( self, amount , description = ''):
        if amount > self.get_balance():
            return False
        else:
            self.ledger.append ({'amount': -amount , 'description': description})
            return True 

    # Returns account balance 
    def get_balance(self):
        total = 0
        for trans in self.ledger:
            total += trans.get('amount')
        return total
    
    # Checks if there is enough money in an account 
    def check_funds(self, needed_amount):
        if needed_amount > self.get_balance():
            return False
        else:
            return True 
    # Transfer money betweek different accounts 
    def transfer (self , trans_amount , category):
        if (self.check_funds(trans_amount)):
           self.withdraw (trans_amount, 'Transfer to ' + category.name )
           category.deposit( trans_amount, ('Transfer from ' + self.name))
           return True
        else:
            return False
    
    def withdraw_amount (self):
        total = 0 
        for item in self.ledger:
            items = item['amount']
            if items < 0: 
                total += items
        return(total)



def create_spend_chart (categories):

    spent_amount = [c.withdraw_amount() for c in categories] # forms a list containing withdrawn amount
    total = sum(spent_amount)
    percentage = [s*100 / total for s in spent_amount] # list containing percentages

    ss = ['Percentage spent by category']

    for i in range(0, 11):
        level = 10 * (10 - i)
        s = '{:>3}| '.format(level) # right aligned with 3 spaces
        for p in percentage:
            if p >= level:
                s += 'o  '
            else: 
                s += '   '
        ss.append(s)
    padding = ' ' * 4
    ss.append(padding + '-' * 3 *len(spent_amount) + '-')
    
    names = [c.name for c in categories]
    n = max(map(len, names))
    for i in range(0, n):
        s = padding
        for name in names:
            s += " "
            s += name[i] if len(name) > i else " "
            s += " "

        ss.append(s + " ")

    return "\n".join(ss)

    
        


    
    

    




food = Category('food')
clothing = Category('clothes')
food.deposit(1000, 'Initial Deposit')
food.deposit(500, 'cat food')
food.deposit( 600 , 'ice cream')
food.withdraw(400,'cat')
clothing.deposit(1000)
clothing.withdraw(100)
food.withdraw(300)
auto = Category('auto')



print(create_spend_chart([food, clothing, auto]))
