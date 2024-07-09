import argparse

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

    args = parser.parse_args()

    if args.command == "arithmetic":
        handle_arithmetic(args)
    elif args.command == "todo":
        handle_todo(args)
    elif args.command == "weather":
        handle_weather(args)
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
    # For simplicity, we'll use an in-memory list. This could be extended to use a file or database.
    todo_list = []
    if args.action == "add":
        todo_list.append(args.item)
        print(f"Added: {args.item}")
    elif args.action == "list":
        print("To-Do List:")
        for item in todo_list:
            print(f"- {item}")
    elif args.action == "remove":
        try:
            todo_list.remove(args.item)
            print(f"Removed: {args.item}")
        except ValueError:
            print(f"Item not found: {args.item}")

def handle_weather(args):
    # Mock function to simulate fetching weather information
    def get_weather(city):
        return f"The current weather in {city} is sunny with a temperature of 25°C."

    weather_info = get_weather(args.city)
    print(weather_info)

if __name__ == "__main__":
    main()
