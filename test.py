string_1=""
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        string_line=line.strip("\n")
        string_line+=" "
        string_1+=string_line
print(string_1)
