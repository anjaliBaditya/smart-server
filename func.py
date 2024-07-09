import argparse
import json
import os

TODO_FILE = "todo_list.json"
CONTACT_FILE = "contacts.json"

def main():
    parser = argparse.ArgumentParser(description="A multi-purpose CLI tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for arithmetic operations
    arithmetic_parser = subparsers.add_parser("arithmetic", help="Perform arithmetic operations")
    arithmetic_parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="The operation to perform")
    arithmetic_parser.add_argument("a", type=float, help="The first number")
    arithmetic_parser.add_argument("b", type=float, help="The second number")

    # Subparser for to-do list management
    todo_parser = subparsers.add_parser("todo", help="Manage your to-do list")
    todo_parser.add_argument("action", choices=["add", "list", "remove"], help="The action to perform on the to-do list")
    todo_parser.add_argument("item", nargs="?", help="The to-do item (required for add and remove actions)")

    # Subparser for weather information
    weather_parser = subparsers.add_parser("weather", help="Get the current weather information")
    weather_parser.add_argument("city", help="The city to get the weather for")

    # Subparser for contact management
    contact_parser = subparsers.add_parser("contact", help="Manage your contacts")
    contact_parser.add_argument("action", choices=["add", "list", "remove"], help="The action to perform on the contacts")
    contact_parser.add_argument("--name", help="The contact's name")
    contact_parser.add_argument("--phone", help="The contact's phone number")
    contact_parser.add_argument("--email", help="The contact's email address")

    # Subparser for unit conversion
    convert_parser = subparsers.add_parser("convert", help="Convert between units")
    convert_parser.add_argument("type", choices=["length", "weight"], help="The type of unit conversion")
    convert_parser.add_argument("value", type=float, help="The value to convert")
    convert_parser.add_argument("from_unit", help="The unit to convert from")
    convert_parser.add_argument("to_unit", help="The unit to convert to")

    args = parser.parse_args()

    if args.command == "arithmetic":
        handle_arithmetic(args)
    elif args.command == "todo":
        handle_todo(args)
    elif args.command == "weather":
        handle_weather(args)
    elif args.command == "contact":
        handle_contact(args)
    elif args.command == "convert":
        handle_conversion(args)
    else:
        parser.print_help()

def handle_arithmetic(args):
    if args.operation == "add":
        result = args.a + args.b
    elif args.operation == "subtract":
        result = args.a - args.b
    elif args.operation == "multiply":
        result = args.a * args.b
    elif args.operation == "divide":
        if args.b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = args.a / args.b
    print(f"Result: {result}")

def handle_todo(args):
    todo_list = load_data(TODO_FILE)
    if args.action == "add":
        todo_list.append(args.item)
        save_data(TODO_FILE, todo_list)
        print(f"Added: {args.item}")
    elif args.action == "list":
        print("To-Do List:")
        for item in todo_list:
            print(f"- {item}")
    elif args.action == "remove":
        try:
            todo_list.remove(args.item)
            save_data(TODO_FILE, todo_list)
            print(f"Removed: {args.item}")
        except ValueError:
            print(f"Item not found: {args.item}")

def handle_weather(args):
    # Mock function to simulate fetching weather information
    def get_weather(city):
        return f"The current weather in {city} is sunny with a temperature of 25°C."

    weather_info = get_weather(args.city)
    print(weather_info)

def handle_contact(args):
    contacts = load_data(CONTACT_FILE)
    if args.action == "add":
        contact = {
            "name": args.name,
            "phone": args.phone,
            "email": args.email
        }
        contacts.append(contact)
        save_data(CONTACT_FILE, contacts)
        print(f"Added contact: {args.name}")
    elif args.action == "list":
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    elif args.action == "remove":
        contacts = [contact for contact in contacts if contact["name"] != args.name]
        save_data(CONTACT_FILE, contacts)
        print(f"Removed contact: {args.name}")

def handle_conversion(args):
    conversion_factors = {
        "length": {
            "m": 1.0,
            "km": 1000.0,
            "cm": 0.01,
            "mm": 0.001,
            "mile": 1609.34,
            "yard": 0.9144,
            "foot": 0.3048,
            "inch": 0.0254
        },
        "weight": {
            "kg": 1.0,
            "g": 0.001,
            "mg": 0.000001,
            "lb": 0.453592,
            "oz": 0.0283495
        }
    }

    if args.type in conversion_factors:
        factors = conversion_factors[args.type]
        if args.from_unit in factors and args.to_unit in factors:
            result = args.value * factors[args.to_unit] / factors[args.from_unit]
            print(f"Result: {result} {args.to_unit}")
        else:
            print(f"Unsupported units for {args.type} conversion")
    else:
        print(f"Unsupported conversion type: {args.type}")

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

if __name__ == "__main__":
    main()
