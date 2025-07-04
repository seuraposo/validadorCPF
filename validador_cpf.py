
class validade_cpf():

    def __init__(self, cpf: str):
        self.cpf = cpf \
            .replace('.','') \
            .replace('-','') \
            .replace(' ','')
        self.rest_one = False


    def validate_first_digit(self):
        if len(self.cpf) == 11:

            self.my_list_one = []
            self.counter_one = 0

            for self.number_first in range(10,1,-1):
            
                self.first_calculation = int(self.cpf [self.counter_one])* self.number_first
                self.counter_one += 1
                self.my_list_one.append(self.first_calculation)

            self.rest_one = sum(self.my_list_one)% 11
            if self.rest_one < 2:
                self.rest_one = 0
                

            else:
                self.rest_one = 11 - self.rest_one
                

            if str(self.rest_one) == self.cpf[9]:               
                self.rest_one = True
                return self.rest_one

            else:
                print ('Primeiro digito não foi validado')

                return None

        else:
            print ('CPF invalido')

            return None
        

    
        
        

            

    def validate_second_digit(self):
        self.my_list_two = []
        self.counter_two = 0
        self.rest_two = False
        if self.rest_one is True:
        
            for self.number_second in range(11,1,-1):
                self.second_calculation = int(self.cpf [self.counter_two])* self.number_second
                self.counter_two += 1
                

                self.my_list_two.append (self.second_calculation)

    

            self.rest_two =  sum(self.my_list_two)%11

        
            
            

            if self.rest_two < 2:
                self.rest_two = 0
                

            else:
                self.rest_two = 11 - self.rest_two

            

            if str(self.rest_two) == self.cpf[10]:    
                self.rest_two = True          
                return self.rest_two

            else:
                print ('Segundo digito não foi validado')  

            
        
        else:
            return print("Primeiro digito não foi validado")
        
    def cpf_validate(self):
        if self.validate_first_digit() == True and self.validate_second_digit() == True:
            print("CPF validado com sucesso")
    




cpf = validade_cpf(input('Digite um cpf para validar: '))
cpf.cpf_validate()


