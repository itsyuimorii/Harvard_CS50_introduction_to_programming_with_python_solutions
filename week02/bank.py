user_input = input ("Greeting: ").strip().lower()

if ("hello" in user_input):
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")