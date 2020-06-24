water_ = { 'espresso' : 250, 'latte' : 350 , 'cappuccino' : 200 }
milk_ = {'espresso' : 0, 'latte' : 75 , 'cappuccino' : 100 }
coffee_ = {'espresso' : 16, 'latte' : 20 , 'cappuccino' : 12 }
price_ = {'espresso' : 4, 'latte' : 7 , 'cappuccino' : 6}



class CoffeeMachine():
      
    def __init__(self, water,milk,coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
          
    def __repr__(self):
        return  f"The coffee machine has: \n {self.water} of water\n {self.milk} of milk\n {self.coffee} of coffee beans\n {self.cups} of disposable cups\n {self.money} of money"
                
    def make(self,order):
        
        if (self.water >= water_[order]) and (self.milk >= milk_[order]) and (self.coffee >= coffee_[order]) and self.cups > 0:
            print('I have enough resources, making you a coffee!')
            self.water -= water_[order]
            self.milk  -= milk_[order]
            self.coffee-= coffee_[order]
            self.cups -= 1
            
            self.money += price_[order]
        else:
            if self.water < water_[order]:
                print('Sorry, not enough water')
            elif self.milk < milk_[order]:
                print('Sorry, not enough milk')
            elif self.coffee < coffee_[order]:
                print('Sorry, not enough coffee')
            else:
                print('Sorry chap, ran out of cups')
                
        return True
                
    def buy(self):
        order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        
        if order == '1':
            self.make('espresso')
        elif order == '2':
            self.make('latte')
        elif order == '3':
            self.make('cappuccino')
        else:
            pass
        
        return True
        
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk  += int(input("Write how many ml of milk do you want to add:"))
        self.coffee+= int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups  += int(input("Write how many disposable cups of coffee do you want to add:"))
        
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
           
                    
    def run(self):
        
        running = True
        
        while running:
            print("Write action (buy, fill, take, remaining, exit):")
            option = input()
        
            if option == 'buy':
                self.buy()
            elif option == 'fill':
                self.fill()
            elif option == 'take':
                self.take()
            elif option == 'remaining':
                print(self)
            else:
                running = False
                
        
          
if __name__ = "__main__":
  machine = CoffeeMachine(400,540,120,9,550)
  machine.run()    
    
