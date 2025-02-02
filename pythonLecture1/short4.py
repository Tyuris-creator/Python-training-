emoticon = "v.v" #global variable

def main():
    global emoticon #after defining global inside function we can chnage it inside locally
    say("Is anyone there?")
    #emoticon = ":D" we can't change global variable
    say("hmm...")
    emoticon = ":D"
    say("Oh, hi!")
    say("Hi")

def say(phrase):
    print(phrase + " " + emoticon)


main()
______________________________________________________
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    print(" ".join(cleaned_shows))
______________________________________________________