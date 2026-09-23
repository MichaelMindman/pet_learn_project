# Muodule for lear build function sys

import sys

print("Module sys.script_1 is run")
# print(help(sys))

# print(dir(sys))
# print(dir(sys.modules))
# print()
# print(dir(sys.modules.__doc__))
# print(help(dir))

public = [s for s in dir(sys) if not s.startswith("_")]
private = [s for s in dir(sys) if s.startswith("_") and not s.startswith("__")]
dunder = [s for s in dir(sys) if s.startswith("__") and s.endswith("__")]
print(public, len(public))
print()
print(private, len(private))
print()
print(dunder, len(dunder))
