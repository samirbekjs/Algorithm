a = input().split()
s = ""
for i in a:
    if i == ".-":
        s+="A"
    elif i == "-...":
        s+="B"
    elif i == "-.-.":
        s+="C"
    elif i == "-..":
        s+="D"
    elif i == ".":
        s+="E"
    elif i == "..-.":
        s+="F"
    elif i == "--.":
        s+="G"
    elif i == "....":
        s+="H"
    elif i == "..":
        s+="I"
    elif i == ".---":
        s+="J"
    elif i == "-.-":
        s+="K"
    elif i == ".-..":
        s+="L"
    elif i == "--":
        s+="M"
    elif i == "-.":
        s+="N"
    elif i == "---":
         s+="O"
    elif i == ".--.":
         s+="P"
    elif i == "--.-":
         s+="Q"
    elif i == ".-.":
         s+="R"
    elif i == "...":
         s+="S"
    elif i == "-":
         s+="T"
    elif i == "..-":
         s+="U"
    elif i == "...-":
         s+="V"
    elif i == ".--":
         s+="W"
    elif i == "-..-":
         s+="X"
    elif i == "-.--":
         s+="Y"
    elif i == "--..":
         s+="Z"
    #sonlar
    elif i == "-----":
        s+="0"
    elif i == ".----":
         s+="1"
    elif i == "..---":
         s+="2"
    elif i == "...--":
         s+="3"
    elif i == "....-":
         s+="4"
    elif i == ".....":
         s+="5"
    elif i == "-....":
         s+="6"
    elif i == "--...":
         s+="7"
    elif i == "---..":
         s+="8"
    elif i == "----.":
         s+="9"
    elif i == ".-.-.":
         s+="."
    elif i == "--..-":
         s+=","
    elif i == "..--.":
         s+="?"
print(s)
