#!/usr/bin/env python3
"""
Main entry point for the calculator application
"""

from calculator import add, subtract, multiply, divide

def main():
    """Main function to demonstrate calculator functionality"""
    print("=" * 50)
    print("🧮 Calculator Application Demo")
    print("=" * 50)
    
    # Demo calculations
    operations = [
        ("Addition", add, 10, 5),
        ("Subtraction", subtract, 10, 5),
        ("Multiplication", multiply, 10, 5),
        ("Division", divide, 10, 5),
    ]
    
    for name, func, a, b in operations:
        try:
            result = func(a, b)
            print(f"✅ {name}: {a} {get_symbol(func)} {b} = {result}")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    
    print("=" * 50)
    print("🎉 Demo completed successfully!")
    print("Run 'pytest test_calculator.py' to execute tests")

def get_symbol(func):
    """Get mathematical symbol for function"""
    symbols = {
        add: "+",
        subtract: "-", 
        multiply: "×",
        divide: "÷"
    }
    return symbols.get(func, "?")

if __name__ == "__main__":
    main()