def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:])+s[0]


def palindrome(s):
    if s != rev(s):
        return False
    return True


if __name__ == "__main__":
    s = "RaceCar".lower()
    print(rev(s))
    if palindrome(s):
        print(" >> Palindrome <<")
    else:
        print(" >> Not a Palindrome <<")
