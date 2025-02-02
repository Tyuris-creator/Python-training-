from soil import sample

def main():
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisure is {moisture}")

    while moisture > 20:
        moisure = sample()
        days += 1
        print(f"Day {days}: Moisure is {moisture}")
    
    print("Time to water!")


main()