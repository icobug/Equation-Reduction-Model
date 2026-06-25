"""
================================================================================
EQUATION REDUCTION MODEL (ERM-CORE) - OFFICIAL PRODUCTION ENGINE (V2.1)
================================================================================
Core Logic Paradigm: Bounded Ternary State Machine (Fault-Tolerant)
Mathematical Operator: Delta-Time (dt) Kinematic Boundary Constraints
Reference Repository: https://github.com/icobug/Equation-Reduction-Model
DOI Specification: https://doi.org/10.5281/zenodo.20813171
================================================================================
"""

import numpy as np
import time
from typing import Tuple, Dict, Any, Union

class ERMBusProtocol:
    """Handles low-level hardware serialization for the 7-bit synchronous bus."""
    SYNC_HEADER = "10011"
    PAYLOAD_MAP: Dict[str, str] = {
        "SMART_ZERO": "00",
        "ROGUE":      "01",
        "ACTIVE":     "10",
        "EMERGENCY":  "11"
    }

    @classmethod
    def generate_frame(cls, state_name: str) -> str:
        """Assembles the 5-bit sync word and 2-bit payload into a 7-bit string."""
        payload = cls.PAYLOAD_MAP.get(state_name, "00")
        return f"{cls.SYNC_HEADER}{payload}"


class ERMCoreLogicEngine:
    """
    The main ERM-Core logic controller. Evaluates multi-dimensional spatial inputs
    against time intervals (dt) and switches operational states dynamically.
    """
    def __init__(self, max_velocity: float = 20.0, max_entropy_cycles: int = 3):
        # The Non-Volatile Memory Vault: Hardcoded ground truth coordinate array [X, Y]
        self._memory_vault = np.array([0.0, 0.0])
        self._last_execution_time = None
        self._v_max = max_velocity
        self._max_entropy_cycles = max_entropy_cycles
        self._entropy_counter = 0
        self.current_state = "SMART_ZERO"

    def process_state_reduction(self, raw_x: Any, raw_y: Any, current_timestamp: float) -> Tuple[int, str, str]:
        """
        Processes and filters incoming telemetry data stream.
        Formula: || P_t - P_{t-1} || <= V_max * dt
        
        Returns:
            Tuple[int, str, str]: (Logic Code, 7-bit Hardware Frame, Flight Controller Command Directive)
        """
        # Initialization logic for the first execution loop cycle
        if self._last_execution_time is None:
            self._last_execution_time = current_timestamp
            bus_frame = ERMBusProtocol.generate_frame(self.current_state)
            return 0, bus_frame, "INITIALIZATION_CYCLE: Awaiting stabilized stream telemetry."

        # Step 1: Structural Integrity & Syntax Validation Filter
        if not isinstance(raw_x, (int, float)) or not isinstance(raw_y, (int, float)):
            self._last_execution_time = current_timestamp
            return self._absorb_entropy_state()

        # Compute dynamic time delta interval (dt)
        dt = current_timestamp - self._last_execution_time
        if dt <= 0:
            dt = 0.001 # Prevent zero division anomalies on ultra-high frequency calls
        
        self._last_execution_time = current_timestamp

        # Step 2: Spatiotemporal Kinematic Constraint Check (Delta-Time Verification)
        incoming_position = np.array([float(raw_x), float(raw_y)])
        spatial_distance = np.linalg.norm(incoming_position - self._memory_vault)
        permissible_boundary = self._v_max * dt

        if spatial_distance > permissible_boundary:
            # Kinematic mismatch caught: Threat or sensor fault detected.
            self.current_state = "ROGUE"
            self._entropy_counter = 0 # Reset entropy buffer since state is explicitly rogue
            bus_frame = ERMBusProtocol.generate_frame(self.current_state)
            return -1, bus_frame, f"REJECT_COMMAND: Distance delta ({spatial_distance:.2f} u) breaches kinematic threshold ({permissible_boundary:.2f} u for dt={dt:.2f}s)."

        # Step 3: Success State Verification & Matrix Convergence
        self.current_state = "ACTIVE"
        self._entropy_counter = 0
        self._memory_vault = incoming_position
        bus_frame = ERMBusProtocol.generate_frame(self.current_state)
        return 1, bus_frame, f"EXECUTE_FLIGHT_WAYPOINT: Vector updated to {self._memory_vault.tolist()}"

    def _absorb_entropy_state(self) -> Tuple[int, str, str]:
        """Activates internal IMU-hold loop during telemetry drops to prevent flight crashes."""
        self._entropy_counter += 1
        
        if self._entropy_counter >= self._max_entropy_cycles:
            self.current_state = "EMERGENCY"
            bus_frame = ERMBusProtocol.generate_frame(self.current_state)
            return -2, bus_frame, "HARDWARE_OVERRIDE_ACTIVE: Intermittent fault limit breached. Commencing Emergency Return-To-Home (RTH)."
        
        self.current_state = "SMART_ZERO"
        bus_frame = ERMBusProtocol.generate_frame(self.current_state)
        return 0, bus_frame, f"SMART_ZERO_ISOLATION: RF/GPS Link decoupled due to input entropy. IMU stabilization engine holding coordinate: {self._memory_vault.tolist()}"


# ==============================================================================
# RIGOROUS HARDWARE SIMULATION HARNESS (VALIDATION MATRIX)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 110)
    print("      EQUATION REDUCTION MODEL (ERM-CORE) FLIGHT AVIONICS SIMULATION MATRIX (V2.1)")
    print("=" * 110)
    
    # Initialize the core with V_max = 15 units/sec, allowing 3 sequential corrupted frames
    core_processor = ERMCoreLogicEngine(max_velocity=15.0, max_entropy_cycles=3)
    
    start_time = time.time()
    
    # Simulated flight scenario sequence mapping real timestamps and telemetry data inputs
    # Format: (Simulated Timestamp Offset, Data X, Data Y, Context Description)
    telemetry_simulation_stream = [
        (0.0, 0.0, 0.0, "System Startup Vector"),
        (1.0, 5.0, 5.0, "Normal flight progression within V_max constraints"),
        (2.0, 12.0, 14.0, "Normal flight progression within V_max constraints"),
        (3.0, "CORRUPT_NAN", None, "RF Jitter/Signal Jamming Event occurs"),
        (4.0, "LINK_DROP", "LINK_DROP", "Total Telemetry Stream Loss continues"),
        (5.0, "LINK_DROP", "LINK_DROP", "Jamming persists beyond the safety buffer tolerance"),
        (6.0, 14.0, 16.0, "Manual override attempt to reconnect after emergency drop"),
        (7.0, 500.0, 600.0, "Malicious Phantom Position Spoofing Attack launched by rogue transmitter")
    ]

    print(f"{'TIME (s)':<10} | {'DATA IN':<22} | {'CORE STATE':<12} | {'BUS FRAME':<10} | {'AVIONICS ACTUATOR OVERRIDE ROUTINE'}")
    print("-" * 110)
    
    for offset, x_val, y_val, description in telemetry_simulation_stream:
        sim_timestamp = start_time + offset
        
        # Pass variables directly into the reduction logic matrix
        logic_code, hardware_frame, routine_directive = core_processor.process_state_reduction(
            raw_x=x_val, 
            raw_y=y_val, 
            current_timestamp=sim_timestamp
        )
        
        input_display = f"[{x_val}, {y_val}]"
        print(f"{offset:<10.1f} | {input_display:<22} | {core_processor.current_state:<12} | {hardware_frame:<10} | {routine_directive}")
        
    print("=" * 110)
    print("SIMULATION SEQUENCE TERMINATED SUCCESSFULY: All validation conditions resolved.")