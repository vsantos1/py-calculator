from os import system
from time import sleep
from app.Calculator import Calculator

options_list = ['[1]-Simple operations','[2]-Others','[3]-Geometric operations']
simple_operations =['[1]-Sum','[2]-Subtract','[3]-Multiply','[4]-Divide','[5]-Exponentiation','[6]-Remainder','[7]-Bhaskara and delta','[8]-Exit ']


def main():
    
    while True:
       
        print(f'Welcome to pyconsolator.')
        sleep(1)
        system('cls')
        print(f'Choose an option below.')
    
        for options in options_list:
            print(options)
            
        
        user_input = float(input('Enter your option: '))
        if user_input != 1:
            print(f'This option is currently unavailable. Please try again.')
            sleep(2)
            system('cls')
            continue
        
        if user_input == 1: 
            system('cls')
            for options in simple_operations:
                print(options) 
                
                
            user_option = float(input('Enter your option: '))
            
            if user_option != 0 and user_option < 7:
                system('cls')
                first_number = float(input('First operating: '))
                second_number = float(input('Second operating: '))
                calculator = Calculator(first_number,second_number)
    
            if user_option == 1:
                calculator.CalculateSum()
                sleep(2)
                break
            
            elif user_option == 2:
                calculator.CalculateSubtract()
                sleep(2)
                break
            
            elif user_option == 3:
                calculator.CalculateMultiply()
                sleep(2)
                break
            
            elif user_option == 4:
                calculator.CalculateDivision()
                sleep(2)
                break
            
            elif user_option == 5:
                calculator.CalculateExponentiation()
                sleep(2)
                break
            
            elif user_option == 6:
                calculator.CalculateRemainder()
                sleep(2)
                break        
            
            elif user_option == 7:
                first_number = float(input('[A] Value: '))
                second_number = float(input('[B] Value: '))
                third_number = float(input('[C] Value: '))
                calculator = Calculator(first_number, second_number)
                calculator.CalculateBhaskara(third_number)
                calculator.CalculateDelta()
                
                sleep(2)
                
                break
            
                                    
            else:
                system('cls')
                print(f'OOOH OHH, it wasnt expected lets try again, ok? ')
                sleep(1)
                system('cls')
                
                continue
    

if __name__ == '__main__':  
    main()