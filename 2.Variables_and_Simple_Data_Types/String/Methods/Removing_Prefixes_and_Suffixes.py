print("\n############### Removing Prefixes and Suffixes ###############")

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(f"removeprefix(): \t{nostarch_url.removeprefix('https://')}\n")

file = 'python_notes.txt'
print(file)
print(f"removesuffix(): \t{file.removesuffix('.txt')}")
