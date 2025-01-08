# Define the file path
file_path = "build/index.html"

# Open the file, read its content, and replace href="/"
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace href="/" with href="/tailwindvitereactone/"
content = content.replace('href="/', 'href="/tailwindvitereactone/')
content = content.replace('src="/', 'src="/tailwindvitereactone/')

print(content)

# Write the modified content back to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(content)

print(f"Updated {file_path}")