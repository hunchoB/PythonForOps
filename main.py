#TODO: Q

if __name__ == '__main__':
    language = "Python"
    position = "Ops"
    print(f"Изучить {language} " , end="")
    if "o" in language.lower() and not "g" in language:
        print("намного проще", end="")
    else:
        print("проще", end=" ")
    print(", чем сопромат")