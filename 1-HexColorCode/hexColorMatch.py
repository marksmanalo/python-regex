import re

# Hex code for a color
txt = "#FF6600"

def checkForMatchAndPrint(regexResult):
  if (regexResult):
    print("We have a match")
    print(regexResult)
  else:
    print("No match")

# the square brackets are used to group a range of acceptable characters
# there are 3 basic quantifiers: 
# ? - match zero or one time
# * - match zero or more times
# + - match one or more times
x = re.match("#[ABCDEF0123456789]+", txt)
checkForMatchAndPrint(x)

# for sequential characters we can group them with the '-' character
x = re.match("#[A-F0-9]+", txt)
checkForMatchAndPrint(x)

# adding a question mark after the # makes it optional (match zero or one time)
# but this means it will match non hex codes like FF6
x = re.match("#?[A-F0-9]+", "FF6")
checkForMatchAndPrint(x)

# curly braces can add specificity, here we will match exactly 6 characters
x = re.match("#?[A-F0-9]{6}", "FF66")
checkForMatchAndPrint(x)
x = re.match("#?[A-F0-9]{6}", "FF6600")
checkForMatchAndPrint(x)

# but 3 characters is a valid hex code
# we can use the | character to indicate 'or' and group them with parenthesis
x = re.match("#?([A-F0-9]{6}|[A-F0-9]{3})", "#FF6")
checkForMatchAndPrint(x)

# for case incensitive stuff you can just add the lower case ones in
x = re.match("#?([A-Fa-f0-9]{6}|[A-Fa-f0-9])", "#aabb44")
checkForMatchAndPrint(x)

# you can also pass in the IGNORECASE flag
x = re.match("#?([A-F0-9]{6}|[A-F0-9])", "#aabb44", re.IGNORECASE)
checkForMatchAndPrint(x)