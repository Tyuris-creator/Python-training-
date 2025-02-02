def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (2 <= len(s) <= 6) and (s[:2].isalpha()) and s.isalnum():
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i] == "0" and s[i-1].isalpha():
                    return False
                if i < (len(s) - 1) and s[i+1].isalpha():
                    return False
        return True

main()

#“All vanity plates must start with at least two letters.”  СДЕЛАЛ
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” СДЕЛАЛ
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
# vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.” СДЕЛАЛ
