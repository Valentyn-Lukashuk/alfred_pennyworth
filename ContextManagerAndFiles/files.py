import os

if __name__ == "__main__":
    file = open(file='write_lines.txt', mode='w')
    print (file)
    file.close()
    print(file)

    with open("write_lines.txt", "w") as f:
        f.writelines(["Hello, it`s me\n", "I was wondering if after all these years\n", ])
<<<<<<< HEAD
    #
    with open("write.txt", 'w') as f:
=======

    with open("write.txt", "w") as f:
>>>>>>> 666a225f749302b09f082a416095047520757c36
        f.write("Some very wise text")
    #
    with open("write_lines.txt", 'r') as f:
        result = f.read()
        print(f"What we have in write_lines.txt {result}")

    with open("write_lines.txt", 'r') as f:
        result = f.readlines()
        print(f"What we have in write_lines.txt {type(result)}: {result}")
    #
    main_path = "dir_with_files"
    path = os.path.join(main_path, "write_lines.txt")
<<<<<<< HEAD
    with open(path, 'w') as f:
        f.writelines(["Hello, it`s me\n", "I was wondering if after all these years\n", ])
=======

    with open(path, "w") as f:
        f.writelines(["Hello, it`s me\n", "I was wondering if after all these years\n", ])



>>>>>>> 666a225f749302b09f082a416095047520757c36
