def Anagram(string1, string2):
    string1 = string1.replace(" ","").lower()
    string2 = string2.replace(" ","").lower()

    if len(string1) != len(string2):
        return False
    
    count = [0] * 26

    for char in string1:
        count[ord(char) - ord('a')] += 1

    for char in string2:
        count[ord(char) - ord('a')] -= 1

    for i in count:
        if i != 0:
            return False
    return True

n = input()
string1 = n.split()[0]
string2 = n.split()[1]
ans = Anagram(string1, string2)
print(ans)