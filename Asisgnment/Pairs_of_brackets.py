start_brackets = "{([])}"
# close_brackets = "])}"

if start_brackets.startswith("{") and start_brackets.endswith("}"):
    print("Bracket { } matches")
else:
    print("No match for { }")

if start_brackets.startswith("(") and start_brackets.endswith(")"):
    print("Bracket ( ) matches")
else:
    print("No match for ( )")
