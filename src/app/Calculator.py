from os import system
from math import sqrt
from urllib import request

class Calculator:
    def __init__(self,first_operating,second_operating):
        self.first_operating = first_operating
        self.second_operating = second_operating

    def CalculatorClosing(self):
        system('cls')
        print(f'Done and closing, goodbye')

    
    def CalculateSum(self):
        result = self.first_operating + self.second_operating
        print(f'The operation -> ({self.first_operating:.0f} + {self.second_operating:.0f}) resulted in {result:.0f}.')
        
    def CalculateSubtract(self):
        result = self.first_operating - self.second_operating
        print(f'The operation -> ({self.first_operating:.0f} - {self.second_operating:.0f}) resulted in {result:.0f}.')
    
    def CalculateMultiply(self):
        result = self.first_operating * self.second_operating
        print(f'The options ->({self.first_operating:.0f} * {self.second_operating:.0f}) resulted in {result:.0f}.')

    def CalculateDivision(self):
        result = self.first_operating / self.second_operating
        print(f'The operation -> ({self.first_operating:.0f} / {self.second_operating:.0f}) resulted in {result:.0f}.')
        
    def CalculateExponentiation(self):
        result = self.first_operating ** self.second_operating
        print(f'The operation -> ({self.first_operating:.0f} ^ {self.second_operating:.0f}) resulted in {result:.0f}.')
    
    def CalculateRemainder(self):
        result = self.first_operating % self.second_operating
        print(f'The operation -> ({self.first_operating:.0f} % {self.second_operating:.0f}) will result in {result:.0f}.')
    
    def CalculateBhaskara(self,third_value):
        self.delta_value = (self.second_operating * self.second_operating) - 4 * self.first_operating * third_value
        print(f'▲ = {self.second_operating * self.second_operating} - 4 * {self.first_operating} * {third_value}')
        
        print(f'▲ = {self.delta_value:.0f}\n')
        
    def CalculateDelta(self):
        
        if self.delta_value < 0:
            print(f'Cannot calculate delta value, delta is less than 0.')
        else:
            positive_operator = ((self.second_operating * -1) + sqrt(self.delta_value)) / (2 * self.first_operating)
            negative_operator = ((self.second_operating * -1) - sqrt(self.delta_value)) / (2 * self.first_operating)
            
            print(f'First delta value = {positive_operator:.2f}')
            print(f'Second delta value = {negative_operator:.2f}')