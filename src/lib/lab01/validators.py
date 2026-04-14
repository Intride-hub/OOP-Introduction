def _validate_brand(brand):
    if not isinstance(brand, str) or brand.strip() == '':
        raise ValueError("должно быть строкой, не должно быть пустым")
    return brand 
    
def _validate_speed(speed):
    if not isinstance(speed, int) or speed<=0:
        raise ValueError('скорость не может быть меньше или равно 0')       
    return speed 
    
def _validate_capacity(capacity):
    if not isinstance(capacity, int) or capacity<=0:
        raise ValueError('вместимость > 0')
    return capacity
    
def _validate_fuel(fuel):
    if not isinstance(fuel, int) or fuel <= 0:
        raise ValueError('топливо>0')   
    return fuel

def _validate_id(car_id):
    if not isinstance(car_id, int) or car_id<0:
        raise ValueError('id должен быть >0, числом')