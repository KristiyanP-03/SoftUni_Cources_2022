import os

def save_extensions(dir, first_level = False):
    for file_name in os.listdir(dir):
        file = os.path.join(dir, file_name)

        if os.path.isfile(file):
            extension = file_name.split('.')[1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)

        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level = True)

directory = input()
extensions = {}
result = []

save_extensions(directory)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append('.' + extension)

    for file in sorted(files):
        result.append(f"- - - {file}")

with open("1/report.txt", 'w') as f:
    f.write('\n'.join(result))