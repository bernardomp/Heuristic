from functools import reduce
import random

class VNS():

    def __init__(self,problem,seed=0):

        random.seed(seed)

        self.problem = problem
        self.evaluation_function = self.problem.evaluation_function
        self.N = self.problem.neighbour_structure
        self.k_max = len(self.N)
        self.k =0 # Reset neighbour structure to the first structure
    
    def gen_initial_solution(self):
        '''
        Generates a random initial solution
        '''

        return [0 for i in range(self.problem.num_objects)]

    def shake(self,x_cur):
        '''
        Generates randomly a neighbour solution of another solution x_cur given a neighbour structure n
            Args:
                x_cur (str): A problem solution
        '''
        neighbourhood_structure = self.N[self.k]
        neighbours = list(neighbourhood_structure(x=x_cur))

        return random.choice(neighbours)

    
    def neighbourhood_change_sequential(self,x_cur,x_new,l=None):

        x_aux = None

        if l == None:
            k = self.k
        else:
            k = l

        if self.evaluation_function(x_cur)<self.evaluation_function(x_new):
            x_aux = x_new
            k=0
            #print("     New solution: " + str(x_aux) + " ------> Value: " + str(self.evaluation_function(x_aux)))
        else:
            k+=1
            x_aux = x_cur


        if l == None:
            self.k = k
            return x_aux
        else:
            return x_aux,k
        
    
    def improvement_function(self,x_cur):
        pass

    def solve(self):
       pass


   
        