#C:\Users\Rmond\Downloads\Project_1_CSC471_S22\Project_1_CSC471_S22\Test_1.txt
def find_subset(sets):
    """
    :desc:
    finds the subset of set by using bit manipulation

    :param: sets
    :return: Prints the subset
    """
    x = len(sets)
    lists = ['empty']
    for i in range(0, (1 << x)):
        m = 1
        l = []
        for j in range(0, x):
            if ((i & m) > 0):
                l.append(sets[j])
                lists.append(l)
            m = m << 1
    print(f"State set of the equivalent DFA = \n{lists}")


def find_eq_V2(lists, state, result):

    cur_state = lists[state]

    cur_set = cur_state[0]
    result.append(state + 1)

    if cur_state[0] == 'empty':
        return

    elif len(cur_set) > 1:
        for j in range(0, len(cur_set)):
            state = cur_set[j] - 1
            return find_eq_V2(lists, state, result)

    else:
        state = cur_set[0] - 1
        return find_eq_V2(lists , state, result)

    return


def find_eq(lists):
    for x in range(0, len(lists)):
        r = []
        find_eq_V2(lists, x, r)
        print(f"E{x + 1} = {r}")


def rearrange(lists):
    """
    :desc :
     Gets rid of the first value because that a reference to the state.
     Ex:
     -> (1), {2,3}
     -> (2), empty

    Turns:
    (2,3)  --- index 0 in the list or state 1
    empty  --- index 1 in the list or sate 2

    :param: lists
    :return:lists
    """
    result = []
    for x in range(0, len(lists)):
        cur_state = lists[x]
        result.append(cur_state[0])
        del cur_state[0]
    return result


def open_file(file, lists):

    """
    :descip
    open file and reads
     As well as converts the output from string to int
    to better implement the E(q) function

    :param: file
    :param: lists
    """
    l = []

    with open(file, "r") as f:

        while True:
            char = f.read(1)

            if not char:
                break
            elif char == '\n':
                l = []
            elif char == '{':
                l2 = []

                while char != '}':
                    char = f.read(1)
                    if char.isdigit():
                        l2.append(int(char))
                        if l2 not in l:
                            l.append(l2)

            elif char == 'e':
                empty = char + f.read(4)
                l.append(empty)
                if l not in lists:
                    lists.append(l)

            elif char.isdigit():
                l.append(int(char))
                if l not in lists:
                    lists.append(l)

        f.close()


if __name__ == "__main__":
    print("Enter text file path")
    file = input()
    lists = []
    open_file(file, lists)
    r = rearrange(lists)
    print()
    find_subset(r)
    print()
    find_eq(lists)



