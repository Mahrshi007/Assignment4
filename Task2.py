try:
    user_input=input("Enter text to write to a file: ")
    with open('output.txt','w') as file1:
        file1.write(user_input+'\n')

    more_input = input("Enter additional text to append to the file: ")
    with open('output.txt','a') as file1:
        file1.write(more_input+'\n')

    print("\nFinal content of the file:")
    with open('output.txt', 'r') as file1:
        for idx, line in enumerate(file1, start=1):
            print(f"Line{idx}:{line.strip()}")
except FileNotFoundError:
    print(f"Error: The file output.txt was not found.")