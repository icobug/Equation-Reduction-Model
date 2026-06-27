from sentinel_k import Sentinel3D

# Инициализираме системата веднъж
brain = Sentinel3D()

def loop():
    # 1. Четем данни от сензорите (напр. от I2C/SPI)
    sensor_data = get_sensors_from_hardware() 
    
    # 2. Обработваме през Sentinel-K
    clean_data = brain.process(sensor_data)
    
    # 3. Проверка за авария
    if any(brain.get_status()):
        # Системата се е защитила сама (код 19)
        trigger_emergency_protocol() 
        return

    # 4. Използваме clean_data за управление на моторите
    apply_controls(clean_data)

# Стартираме цикъла
while True:
    loop()