while(True):
    try:
        num = int(input("Enter a integer: "))
        print(f"Hey you entered {num}, is it your lucky number XD")
        break
    except KeyboardInterrupt:
        print("No input taken")
        break
    except (ValueError, NameError):
        print("Not a valid number")
    finally:
        print('Attempted to Input')
