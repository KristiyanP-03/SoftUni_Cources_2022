file_directory = input().split("\\")
file_details_found = False
for file_path_part in file_directory:
    if "." in file_path_part:
        file_name, file_extention = file_path_part.split(".")
        file_details_found = True
if file_details_found:
    print(f"File name: {file_name}")
    print(f"File extension: {file_extention}")