def main():
    amount_due = 50
    coin = 0
    print(f"Amount Due: {amount_due}")
    while coin != 5 and coin != 10 and coin != 25 and coin != 50:
        while amount_due >= 0:
            coin = int(input("Insert coin: "))
            match coin:
                case 5:
                    amount_due = amount_due - 5
                    if amount_due > 0:
                        print(f"Amount Due: {amount_due}")
                case 10:
                    amount_due -= 10
                    if amount_due > 0:
                        print(f"Amount Due: {amount_due}")
                case 25:
                    amount_due -= 25
                    if amount_due > 0:
                        print(f"Amount Due: {amount_due}")
                case 50:
                    amount_due -= 50
                    if amount_due > 0:
                        print(f"Amount Due: {amount_due}")
                case _:
                    print(f"Amount Due: {amount_due}")

            if amount_due <= 0:
                if amount_due == 0:
                    print("Change Owed:", amount_due)
                elif amount_due < 0:
                    amount_due = amount_due * -1
                    print("Change Owed:", amount_due)
                break
# abs(amount_dew)
main()