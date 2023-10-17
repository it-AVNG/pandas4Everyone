import numpy as np


def list_return(data,data_flat):    
    max_list = [
        # axis1,
        list(np.max(data,axis=0)),
        # axis2,
        list(np.max(data,axis=1)),
        # flatten
        float(np.max(data_flat))]
    min_list = [
        # axis1,
        list(np.min(data,axis=0)),
        # axis2,
        list(np.min(data,axis=1)),
        # flatten
        float(np.min(data_flat))]
    
    sum_list = [
        # axis1,
        list(np.sum(data,axis=0)),
        # axis2,
        list(np.sum(data,axis=1)),
        # flatten
        float(np.sum(data_flat))]    
    
    mean = [
        # axis1,
        list(np.mean(data,axis=0)),
        # axis2,
        list(np.mean(data,axis=1)),
        # flatten
        float(np.mean(data_flat))]
    
    variance = [
        # axis1,
        list(np.var(data,axis=0)),
        # axis2,
        list(np.var(data,axis=1)),
        # flatten
        float(np.var(data_flat))]
    
    stand_dist = [
        # axis1,
        list(np.std(data,axis=0)),
        # axis2,
        list(np.std(data,axis=1)),
        # flatten
        float(np.std(data_flat))]    
        
    list_type ={
        'mean': mean,
        'variance':variance,
        'stand_dist': stand_dist,
        'min':min_list,
        'max':max_list,
        'sum':sum_list
    }
    return list_type

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    num_list = np.array(list)
    shaped_list = num_list.reshape((3,3))
    list_typ = list_return(shaped_list,num_list)

    calculations = {
        'mean': list_typ['mean'],
        'variance': list_typ['variance'],
        'standard deviation': list_typ['stand_dist'],
        'max': list_typ['max'],
        'min': list_typ['min'],
        'sum': list_typ['sum']
    }

    return calculations

actual = calculate([9,1,5,3,3,3,2,9,0])
print(actual)