import re

with open("./Day1/input.txt", encoding="utf-8") as f:
    runningsum = 0
    digits = [str(x) for x in range(10)]
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    combined = digits + words
    for line in f.readlines():
        print(line)
        val_dict = dict()
        for substr in combined:
            m = re.finditer(substr, line)
            match_starts = [match.start(0) for match in m]
            for start in match_starts:
                val_dict[start] = substr

        linevals = [val_dict[ind] for ind in sorted(val_dict)]
        for ind, word in enumerate(words):
            linevals = [val.replace(word, str(ind + 1)) for val in linevals]
        # line = [line[ind:].startswith() for ind in range(len(line)) if ]
        # for index, word in enumerate(words):
        #     line = line.replace(word, str(index + 1))
        # print(line)
        # linevals = [val for val in line if val in digits]
        # print(linevals)
        # lineval = (
        #     int(linevals[0] + linevals[-1]) if len(linevals) > 1 else int(linevals[0])
        # )
        print(linevals)
        lineval = int(linevals[0] + linevals[-1])
        print(lineval)
        runningsum += lineval

        print(runningsum)
