import os
import re
import shutil

dir_202 = "202"
dir_sauce = "202_sauce"

if not os.path.isdir(dir_sauce):
    os.mkdir(dir_sauce)

# removes all non-sauce comments for all non-fullgame files
for file in os.listdir(dir_202):
    if file.endswith(".tas") and file != "202.tas":
        src = os.path.join(dir_202, file)
        dst = os.path.join(dir_sauce, file)

        src_str = ""

        with open(src, 'r') as f:
            src_str = f.read()

        # remove checkpoints then rooms
        with open(dst, 'w') as f:
            new_str = re.sub("\n{3}# .*\n# .*", "", src_str, 0, re.MULTILINE)
            f.write(re.sub("\n{2}# .*", "", new_str, 0, re.MULTILINE))
