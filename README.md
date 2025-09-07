# AccelStepper 

## A stepper motor control library for MicroPython.

This class provides an interface for controlling stepper motors with acceleration and speed control.
It supports multiple stepper driver types and stepping modes including full-step and half-step.

### Key Features:

- Acceleration and deceleration support
- Multiple stepping modes (Driver, 2 wire, 3 wire, 4 wire)
- Position tracking and control
- Speed control

### Arguments:

- **6 arguments**: (`interface`, `pin1`, `pin2`, `pin3` `pin4`, `enable`)
  - `interface` (int): The stepping interface type
    - `DRIVER`: Stepper Driver (e.g. A4988), 2 driver pins required (STEP, DIR)
    - `FULL2WIRE`: 2 wire stepper, 2 motor pins required
    - `FULL3WIRE`: 3 wire stepper, such as HDD spindle, 3 motor pins required
    - `FULL4WIRE`: 4 wire full stepper, 4 motor pins required
    - `HALF3WIRE`: 3 wire half stepper, such as HDD spindle, 3 motor pins required
    - `HALF4WIRE`: 4 wire half stepper, 4 motor pins required
  - `pinX` (int): Motor control pins
    - DRIVER: `STEP_PIN, DIR_PIN, 0, 0`
    - 2WIRE: `M1A, M1B, 0, 0`
    - 3WIRE: `U_Pin, V_Pin, W_Pin,0`
    - 4WIRE: `M1A, M1B, M2A, M2B`
  - `enable` (bool): Whether to enable outputs immediately
    - Doesn't work for seperate enable pin (e.g. `interface = DRIVER`)
- *Internal Use Only:* **2 arguments**: (`forward_func`, `backward_func`)
  - `forward_func` (callable): Function to call for forward stepping
  - `backward_func` (callable): Function to call for backward stepping

### Properties:

- `_currentPos` (int): Current position of the stepper
- `_targetPos` (int): Target position to move to
- `_speed` (float): Current speed in steps per second
- `_maxSpeed` (float): Maximum speed in steps per second
- `_acceleration` (float): Acceleration in steps per second per second
- `_interface` (int): Type of stepper driver interface
- `_direction` (int): Current direction of movement

### Methods:

- `move_to(absolute: int) -> None`:
  - Move to absolute position
- `move(relative: int) -> None`:
  - Move relative to current position
- `run_speed() -> bool`:
  - Run motor at constant speed
- `run() -> bool`:
  - Keep stepping the motor to target position with acceleration
- `set_max_speed(speed: float) -> None`:
  - Set maximum speed
- `set_acceleration(acceleration: float) -> None`:
  - Set acceleration rate
- `set_speed(speed: float) -> None`:
  - Set constant speed mode
- `distance_to_go() -> int`:
  - Get remaining distance to target position
- `target_position() -> int`:
  - Get target position
- `current_position() -> int`:
  - Get current position
- `set_current_position(position: int) -> None`:
  - Reset current position
- `run_to_position() -> None`:
  - Blocking call to run to target position
- `run_to_new_position(position: int) -> None`:
  - Blocking call to run to new target position
- `stop() -> None`:
  - Stop motor with deceleration
- `is_running() -> bool`:
  - Check if motor is still running to target
