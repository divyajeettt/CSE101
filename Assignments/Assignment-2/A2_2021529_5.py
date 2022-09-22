NOTES: list[str] = [
    "C", "C#", "D", "D#", "E", "F", "F#" ,"G", "G#", "A", "A#", "B"
] * 2

MAJOR: str = ".\\Data\\Q5\\scalemajor.txt"
MINOR: str = ".\\Data\\Q5\\scaleminor.txt"


def noteCreate() -> None:
    """creates separate text-files scalemajor.txt and scaleminor.txt"""
    
    major_indices = [0, 2, 4, 5, 7, 9, 11, 12]
    minor_indices = [0, 2, 3, 5, 7, 8, 10, 12]
             
    with open(MAJOR, "w") as f1, open(MINOR, "w") as f2:
        # run the loop 12 times as there are 12 unique notes
        for i in range(12):
            # adding i to j -> first note starts at the i-th index from the NOTES list
            major_scale = [NOTES[i+j] for j in major_indices]
            minor_scale = [NOTES[i+j] for j in minor_indices]
            major_scale[-1] += "'"    # to denote an "octave"
            minor_scale[-1] += "'"    # to denote an "octave"
            f1.write(str(major_scale) + "\n")
            f2.write(str(minor_scale) + "\n")


def majorNotes(root: str) -> str:
    """retrives the major scale of the given root from scalemajor.txt"""
    
    with open(MAJOR) as file:
        for scale in file.readlines():
            scale = eval(scale)
            if scale[0] == root:
                # it is advised not to return from the with block
                # so break the loop, and return outside the with block
                break
    return " ".join(scale)


def minorNotes(root: str) -> str:
    """retrives the minor scale of the given root from scalemajor.txt"""
    
    with open(MINOR) as file:
        for scale in file.readlines():
            scale = eval(scale)
            if scale[0] == root:
                # it is advised not to return from the with block
                # so break the loop, and return outside the with block
                break
    return " ".join(scale)


def main() -> None:
    """__main__ function"""
    
    noteCreate()
    note = input("Enter a musical note: ").capitalize()
    kind = input("Enter type of scale (Major / Minor): ").capitalize()
    
    while (note not in NOTES) or (kind not in ["Major", "Minor"]):
        print("Please enter a valid musical note and kind of scale \n")
        note = input("Enter a musical note: ").capitalize()
        kind = input("Enter type of scale (Major / Minor): ").capitalize()
        print()
    
    print(f"{note} {kind} Scale:", majorNotes(note) if kind == "Major" else minorNotes(note))


if __name__ == "__main__":
    main()