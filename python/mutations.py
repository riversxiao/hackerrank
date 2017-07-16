def mutate_string(string, position, character):
    k =list(string)
    k[position]=character
    return "".join(k)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
