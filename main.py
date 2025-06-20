#class to store and manage a food item
class FoodItem:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


#class to handle the calorie counter logic
class CalorieCounter:
    def __init__(self):
        self.items = []
    
    #Add a food item
    def add_item(self, name, calories):
        self.items.append(FoodItem(name, calories))
    
    #view all added food items
    def view_items(self):
        if not self.items:
            print('No items added')
        
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - {item.calories} cal")
    
    #Get total calories
    def total_calories(self):
        total = sum(item.calories for item in self.items)
        print(f"Total alories: {total} cal")


#main function for menu interaction
def main():
    counter = CalorieCounter()

    while True:
        print("\n-------Calorie Counter-------")
        print('1. Add Food Item')
        print('2. View Items')
        print('3. Show Total Calories')
        print('4. Exit')

        choice = input('Choose: ')
        if choice == '1':
            name = input('Enter food name: ')
            try:
                calories = int(input('Enter calories: '))
                counter.add_item(name, calories)
            except ValueError:
                print('Please enter a valid number')

        elif choice == '2':
            counter.view_items()
        
        elif choice == '3':
            counter.total_calories()
        
        elif choice == '4':
            print('Goodbye!')
            break

        else:
            print('Invalid choice')


# Start the program
main()



