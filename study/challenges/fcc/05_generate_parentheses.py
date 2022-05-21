"""
BACKTRACKING type of algo

"""


def generate(n):
    def rec(n, diff, comb, combs):
        """
        n = number of remaining parenthesis to add
        diff = the difference between opening and closing brackets
        comb = current combination being built
        combs = array of combinations
        """
        if diff < 0 or diff > n:
            return

        elif diff == 0 and n == 0:
            combs.append(''.join(comb))                 # O(n)

        else:
            # branch 1 - add a new open parenthesis
            comb.append('(')                            # O(1)
            rec(n-1, diff+1, comb, combs)               # T(n-1)
            comb.pop()                                  # O(1)

            # branch 2 - add a new close parenthesis
            comb.append(')')                            # O(1)
            rec(n-1, diff-1, comb, combs)               # T(n-1)
            comb.pop()                                  # O(1)

    combs = []
    rec(2*n, 0, [], combs)  # n = number of pairs, not parenthesis
    return combs


if __name__ == "__main__":
    gen_3 = generate(3)
    print("gen_3: ", "\n", len(gen_3), "\n", gen_3)

    gen_4 = generate(4)
    print("gen_4: ", "\n", len(gen_4), "\n", gen_4)
