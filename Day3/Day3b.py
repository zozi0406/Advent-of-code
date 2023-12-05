import numpy as np
import numpy.ma as ma

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
                if schem[row_index, col_index] == "*":
                    subschem_adjacent = schem[
                        max(row_index - 1, 0) : min(row_index + 2, schem.shape[0]),
                        max(col_index - 1, 0) : min(col_index + 2, schem.shape[1]),
                    ]
                    subschem_large = schem[
                        max(row_index - 1, 0) : min(row_index + 2, schem.shape[0]),
                        max(col_index - 3, 0) : min(col_index + 4, schem.shape[1]),
                    ]
                    boolarray = np.isin(subschem_adjacent, digits)
                    row_sums = boolarray.sum(axis=1)
                    nonzero_rows = np.count_nonzero(row_sums)
                    large_boolarray = np.isin(subschem_large, digits)
                    if nonzero_rows == 2 or (
                        nonzero_rows == 1 and np.all(boolarray.sum(axis=0) == [1, 0, 1])
                    ):
                        mask = np.ones([3, 7], dtype=bool)
                        mask[1, 3] = False
                        if not boolarray[0, 0]:
                            mask[0, 0:3] = False
                        if not boolarray[0, 1]:
                            mask[0, 3] = False
                        if not boolarray[0, 2]:
                            mask[0, 4:7] = False
                        if not boolarray[1, 0]:
                            mask[1, 0:3] = False
                        if not boolarray[1, 2]:
                            mask[1, 4:7] = False
                        if not boolarray[2, 0]:
                            mask[2, 0:3] = False
                        if not boolarray[2, 1]:
                            mask[2, 3] = False
                        if not boolarray[2, 2]:
                            mask[2, 4:7] = False
                        # if boolarray[0, :].all():
                        #     mask[0, 0:2] = False
                        #     mask[0, 5:7] = False
                        # if boolarray[2, :].all():
                        #     mask[2, 0:2] = False
                        #     mask[2, 5:7] = False

                        extra_mask = np.ones([3, 7], dtype=bool)
                        for rownum in range(3):
                            for colnum in range(7):
                                if (
                                    colnum in [0, 1]
                                    and subschem_large[rownum, colnum] == "."
                                ):
                                    extra_mask[rownum, 0 : colnum + 1] = False
                                elif (
                                    colnum in [5, 6]
                                    and subschem_large[rownum, colnum] == "."
                                ):
                                    extra_mask[rownum, colnum:] = False

                        combined_mask = np.logical_and(mask, large_boolarray)
                        combined_mask = np.logical_and(combined_mask, extra_mask)

                        print(subschem_large)
                        factors = []
                        for rownum in range(3):
                            if (
                                np.count_nonzero(combined_mask.sum(axis=1)) == 2
                                and combined_mask.sum(axis=1)[rownum] > 0
                            ):
                                factors.append(
                                    int(
                                        "".join(
                                            list(
                                                subschem_large[
                                                    rownum, combined_mask[rownum, :]
                                                ]
                                            )
                                        )
                                    )
                                )
                            elif (
                                np.count_nonzero(combined_mask.sum(axis=1)) == 1
                                and combined_mask.sum(axis=1)[rownum] > 0
                            ):
                                factors.append(
                                    int(
                                        "".join(
                                            list(
                                                subschem_large[rownum, 0:3][
                                                    combined_mask[rownum, 0:3]
                                                ]
                                            )
                                        )
                                    )
                                )
                                factors.append(
                                    int(
                                        "".join(
                                            list(
                                                subschem_large[rownum, 4:7][
                                                    combined_mask[rownum, 4:7]
                                                ]
                                            )
                                        )
                                    )
                                )
                        if (
                            np.count_nonzero(combined_mask.sum(axis=1)) == 3
                            or len(factors) in [0, 1, 3]
                            or factors[0] > 999
                            or factors[1] > 999
                        ):
                            print(subschem_large)
                            print(subschem_adjacent)
                            print(boolarray)
                            print(large_boolarray)
                            print(mask)
                            print(combined_mask)
                            print(factors)
                            raise NotImplementedError
                        product = factors[0] * factors[1]
                        print(factors)
                        result += product
                        print(product)

        print(result)
