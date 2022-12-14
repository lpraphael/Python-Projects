def tic_tac_toe():
    s = input()

    print(
        f"""
        ---------
        | {s[0]} {s[1]} {s[2]} |
        | {s[3]} {s[4]} {s[5]} |
        | {s[6]} {s[7]} {s[8]} |
        ---------
        """
    )

    combinations = [
        [s[0], s[3], s[6]],
        [s[1], s[4], s[7]],
        [s[2], s[5], s[8]],
        [s[0], s[4], s[8]],
        [s[2], s[4], s[6]],
        [s[0], s[1], s[2]],
        [s[3], s[4], s[5]],
        [s[6], s[7], s[8]],
    ]

    counter_x = 0

    counter_o = 0

    for sequence in combinations:
        if sequence[0] == "X" and sequence[1] == "X" and sequence[2] == "X":
            counter_x += 1
            continue
        if sequence[0] == "O" and sequence[1] == "O" and sequence[2] == "O":
            counter_o += 1
            continue

    if counter_x > counter_o:
        return print("X wins")
    if counter_x < counter_o:
        return print("O wins")
    if (
        counter_x != 0
        and counter_o != 0
        or s.count("X") - s.count("O") >= 2
        or s.count("O") - s.count("X") >= 2
    ):
        return print("Impossible")
    if counter_x == 0 and counter_o == 0:
        if "_" not in s:
            return print("Draw")
        elif "_" in s:
            return print("Game not finished")


tic_tac_toe()
