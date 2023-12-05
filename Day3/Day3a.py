import numpy as np

with open("./Day3/input.txt", encoding="utf-8") as f:
    digits = [str(x) for x in range(10)]
    notsymbols = digits + ["."]
    numbers = []
    first = True
    schem = None
    result = 0
    for line in f.readlines():
        if first:
            schem = np.array(list(line.strip()))
            first = False
        else:
            if schem is not None:
                schem = np.vstack([schem, np.array(list(line.strip()))])
    if schem is not None:
        for row_index in range(schem.shape[0]):
            for col_index in range(schem.shape[1]):
                if col_index > 0:
                    if (
                        schem[row_index, col_index] in digits
                        and schem[row_index, col_index - 1] not in digits
                    ):
                        numstring = schem[row_index, col_index]
                        ndigits = 1
                        for col_offset in range(1, 4):
                            if col_index + col_offset < schem.shape[1]:
                                if schem[row_index, col_index + col_offset] in digits:
                                    numstring += schem[
                                        row_index, col_index + col_offset
                                    ]
                                    ndigits += 1
                                else:
                                    break

                        subschem = schem[
                            max(row_index - 1, 0) : min(row_index + 2, schem.shape[0]),
                            max(col_index - 1, 0) : min(
                                col_index + ndigits + 1, schem.shape[1]
                            ),
                        ]
                        if np.logical_not(np.isin(subschem, notsymbols)).any():
                            result += int(numstring)
                            print(numstring)

                elif schem[row_index, col_index] in digits:
                    numstring = schem[row_index, col_index]
                    ndigits = 1
                    for col_offset in range(1, 4):
                        if schem[row_index, col_index + col_offset] in digits:
                            numstring += schem[row_index, col_index + col_offset]
                            ndigits += 1
                        else:
                            break
                    subschem = schem[
                        max(row_index - 1, 0) : min(row_index + 2, schem.shape[0]),
                        max(col_index - 1, 0) : min(
                            col_index + ndigits + 1, schem.shape[1]
                        ),
                    ]
                    if np.logical_not(np.isin(subschem, notsymbols)).any():
                        result += int(numstring)
                        print(numstring)
            print("New row")
        print(result)
