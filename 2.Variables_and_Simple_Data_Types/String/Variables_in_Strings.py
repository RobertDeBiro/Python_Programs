# - variables are used inside strings by using so called f-strings
# - 'f' means "format"

print("\n############### Variables in Strings ###############")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")

message = f"Hello, {full_name.title()}"
print(message)
