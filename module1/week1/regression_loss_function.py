import math
import random


def MAE(n):
    final_mae = 0
    for i in range(0,n):
        target_i = random.uniform(0,10)
        predict_i = random.uniform(0,10)

        loss = abs(target_i - predict_i)
        final_mae += loss
        print(f"loss name: MAE, sample: {i},pred: {predict_i}, target: {target_i}, loss: {loss}")
    final_mae = final_mae/n
    print(f"final MAE: {final_mae}")

def MSE(n):
    final_mse = 0
    for i in range(0,n):
        target_i = random.uniform(0,10)
        predict_i = random.uniform(0,10)

        loss = (target_i - predict_i)**2
        final_mse += loss
        print(f"loss name: MSE, sample: {i},pred: {predict_i}, target: {target_i}, loss: {loss}")
    final_mse = final_mse/n
    print(f"final MSE: {final_mse}")
    

def RMSE(n):
    final_rmse = 0
    for i in range(0,n):
        target_i = random.uniform(0,10)
        predict_i = random.uniform(0,10)

        loss = (target_i - predict_i)**2
        final_rmse += loss
        print(f"loss name: MSE, sample: {i},pred: {predict_i}, target: {target_i}, loss: {loss}")    
    final_rmse = math.sqrt(final_rmse/n)
    print(f"final MSE: {final_rmse}")


def exercise3():
    n = input("Input number of samples (integer number) which are generated : ")
    if n.isnumeric() == False:
        print('number of samples must be an integer number')
        return
    
    lost_name = input("Input loss name : ")
    n = int(n)
    print(f"Input x = {n}")
    print(f'Input loss name : {lost_name}')
    if lost_name == 'MAE':
        MAE(n)
    elif lost_name == 'MSE':
        MSE(n)  
    elif lost_name == 'RMSE':
        RMSE(n)
    else:
        print(f"{lost_name} is not supportted")
    
exercise3()
exercise3()