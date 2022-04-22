from name_function import get_formatted_name

print(f"Enter 'q' at any time to quit.")
while True:
    first = input("\nplease give me a firstname: ")
    if first == 'q':
        break

    last = input("\nplease give me a lastname: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")