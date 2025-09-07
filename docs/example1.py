from AccelStepper import AccelStepper, DRIVER
import time

def setup_stepper():
    """Initialize and configure the stepper motor"""
    # Define pins for STEP, DIR, and ENABLE
    STEP_PIN = 14
    DIR_PIN = 11
    ENABLE_PIN = 10

    # Create stepper instance
    stepper = AccelStepper(DRIVER, STEP_PIN, DIR_PIN, 0, 0, True)
    
    # Configure enable pin and pin inversions
    stepper.set_enable_pin(ENABLE_PIN)
    stepper.set_2_pins(direction_invert=False, 
                       step_invert=False,
                       enable_invert=True)
    
    # Set motor parameters
    stepper.set_max_speed(1000)      # Steps per second
    stepper.set_acceleration(5000)    # Steps per second^2
    stepper.set_current_position(0)   # Reset position to 0
    
    return stepper

def move_to_position(stepper, target_position):
    """Move stepper to a specific position"""
    try:
        stepper.enable_outputs()
        stepper.move_to(target_position)
        
        # Run until target is reached
        while stepper.is_running():
            stepper.run()
            
    except Exception as e:
        print(f"Error during movement: {e}")
    finally:
        stepper.disable_outputs()

def main():
    # Initialize stepper
    stepper = setup_stepper()
    
    # Example movement sequence
    print("Starting motor movement...")
    move_to_position(stepper, 2000)  # Move 2000 steps clockwise
    time.sleep(1)  # Wait 1 second
    move_to_position(stepper, 0)     # Return to home position
    print("Movement complete!")

if __name__ == "__main__":
    main()
