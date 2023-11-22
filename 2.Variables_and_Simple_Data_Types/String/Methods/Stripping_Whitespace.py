# - whitespace can be: empty space, tab, newline...

print("\n############### Stripping Whitespace ###############")

favorite_language_1 = 'python '
favorite_language_2 = ' cpp'
favorite_language_3 = '\tcsharp\t'

# Remove whitespaces from the right side
print(f"no strip: \t'{favorite_language_1}'")
print(f"rstrip(): \t'{favorite_language_1.rstrip()}'")

# Remove whitespaces from the left side
print(f"no strip: \t'{favorite_language_2}'")
print(f"lstrip(): \t'{favorite_language_2.lstrip()}'")

# Remove whitespaces from both sides
print(f"no strip: \t'{favorite_language_3}'")
print(f"strip(): \t'{favorite_language_3.strip()}'")