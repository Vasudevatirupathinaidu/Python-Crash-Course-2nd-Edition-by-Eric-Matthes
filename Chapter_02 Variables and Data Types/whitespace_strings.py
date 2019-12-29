# Adding whitespace to strings with tabs or newlines

# Tab
print("Python")
print("\tPython")

# Newline
print("Languages:\nPython\nC++\nJavascript")

# Combine tabs and newlines
print("Languages:\n\tPython\n\tC++\n\tJavascript")


# Stripping whitespace - To ensure that no whitespace exists at the right end and left end of a string

# Strip whitespace from the right side of a string - rstrip()

favorite_language = ' python '
print(favorite_language, f"length: {len(favorite_language)}")

favorite_language_right = favorite_language.rstrip()
print(f"{favorite_language_right}", f"length: {len(favorite_language_right)}")


# Strip whitespace from the left side of a string - lstrip()

favorite_language_left = favorite_language.lstrip()
print(f"{favorite_language_left}", f"length: {len(favorite_language_left)}")


# Strip whitespace from the both side of a string - strip()

favorite_language_both = favorite_language.strip()
print(f"{favorite_language_both}", f"length: {len(favorite_language_both)}")
