import rclpy
import land_rover
from land_rover.fuel_injector import diagnose

def main():
    b1 = 3
    b2 = 3
    result = diagnose(b1,b2)
    print(f'{},{}:{}')
if __name__ == '__main__':
main()

