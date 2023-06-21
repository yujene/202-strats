import numpy as np
import os

directions = ["", "L", "R", "U", "D", "LU", "RU", "LD", "RD"]
dashes = {x: 0 for x in directions}
demos = {x: 0 for x in directions}

dash_started = False
dashed = False
demo_started = False
demoed = False
frames = 0

def get_dir(chars):
    dir = ""
    if "L" in chars:
        dir += "L"
    if "R" in chars:
        dir += "R"
    if "U" in chars:
        dir += "U"
    if "D" in chars:
        dir += "D"
    return dir

for file in os.listdir("."):
    if file.endswith(".tas") and file != "202.tas" and "g" not in file:
        print(file)
        with open(file, "r") as f:
            line = f.readline().strip()

            while "FileTime" not in line:
                # if tas input
                if line and line[0].isnumeric():
                    chars = line.split(",")
                    # if not dashing rn and find a dash line
                    if not dash_started:
                        if "C" in chars or "X" in chars:
                            dash_started = True
                            frames += int(chars[0])
                            # set dir when gain dash dir
                            if frames >= 5:
                                dashes[get_dir(chars)] += 1
                                dashed = True
                    else:
                        # continuing dash lines
                        if "C" in chars or "X" in chars:
                            frames += int(chars[0])
                            # set dir when gain dash dir
                            if frames >= 5:
                                dashes[get_dir(chars)] += 1
                                dashed = True
                        else:
                            # reset when no more consecutive dash lines
                            dash_started = False
                            dashed = False
                            frames = 0

                    if not demo_started:
                        if "Z" in chars:
                            demo_started = True
                            frames += int(chars[0])
                            # set dir when gain dash dir
                            if frames >= 5:
                                demos[get_dir(chars)] += 1
                                demoed = True
                    else:
                        # continuing dash lines
                        if "Z" in chars:
                            frames += int(chars[0])
                            # set dir when gain dash dir
                            if frames >= 5:
                                demos[get_dir(chars)] += 1
                                demoed = True
                        else:
                            # reset when no more consecutive dash lines
                            demo_started = False
                            demoed = False
                            frames = 0

                line = f.readline().strip()

    print(dashes)
    print(demos)
