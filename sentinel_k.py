import numpy as np
from collections import deque
import json
import os

class SentinelK:
    """
    Sentinel-K: Индустриален хибриден филтър за критични системи.
    Основни функции: Kalman Predictor, ERM Defense, Black Box Telemetry.
    """
    EMERGENCY_CODE = 0b10011  # 19
    
    def __init__(self, buffer_size=20):
        # 1. Параметри на филтъра (Настройвай Q и R според сензора)
        self.Q, self.R = 0.005, 0.15
        self.P, self.x = 1.0, 0.0
        self.f_val = 0.0
        
        # 2. Състояние на системата
        self.emergency = False
        self.initialized = False
        self.smart_zero = 1e-17
        
        # 3. Черна кутия (Кръгов буфер за телеметрия)
        self.history = deque(maxlen=buffer_size)

    def _log(self, data):
        """Записва последните стойности преди евентуален срив."""
        self.history.append(data)

    def export_telemetry(self, filename="emergency_crash_report.json"):
        """Автоматичен експорт при авария."""
        try:
            with open(filename, 'w') as f:
                json.dump(list(self.history), f, indent=4)
        except Exception as e:
            print(f"Критична грешка при запис на телеметрията: {e}")

    def update(self, raw_val):
        """Основен метод за обработка на сигнал."""
        # Проверка за авариен режим (Fail-Safe)
        if self.emergency:
            return self.EMERGENCY_CODE
            
        # Логване в Черната кутия
        self._log(raw_val)
        
        # Cold Start - инициализация при първо пускане
        if not self.initialized:
            self.f_val = raw_val
            self.x = raw_val
            self.initialized = True
            return raw_val
            
        # Kalman Gain & State Update
        self.P += self.Q
        K = self.P / (self.P + self.R)
        self.x += K * (raw_val - self.x)
        self.P *= (1 - K)
        
        # ERM Защита (Shock Detection)
        err = self.x - self.f_val
        shock = abs(err) / (abs(self.f_val) + self.smart_zero)
        
        # Реакция при Black Swan събитие
        if shock > 10.0:
            self.emergency = True
            self.export_telemetry() # Записваме доказателствата
            return self.EMERGENCY_CODE
        
        # Демпване на сигнала (Адаптивен филтър)
        damp = 0.15 / (1.0 + 2.5 * shock**2)
        self.f_val += damp * err
        
        return self.f_val

class Sentinel3D:
    """
    3D обвивка: Изолира всяка ос (X, Y, Z), за да не срине цялата система.
    """
    def __init__(self):
        self.axes = [SentinelK(), SentinelK(), SentinelK()]
        
    def process(self, vec_3d):
        """Вход: [x, y, z]. Изход: [x_filtered, y_filtered, z_filtered]."""
        return [self.axes[i].update(vec_3d[i]) for i in range(3)]
        
    def get_status(self):
        """Връща списък със статуса на всяка ос [bool, bool, bool]."""
        return [sk.emergency for sk in self.axes]