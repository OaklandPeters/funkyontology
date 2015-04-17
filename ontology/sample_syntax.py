

# type "superposition"
cls = str | int
#
# ...
#
# type "collapse"
result = cls.append(...)
# we now know that cls has to be a str, and not an int
#
# --> Run-time type inference

