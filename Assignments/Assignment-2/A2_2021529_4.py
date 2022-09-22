import os


STUDENT_FOLDER: str = ".\\Data\\Q4\\Student"
# it makes more sense for the final report to be in the Admin Folder
FINAL_REPORT: str = ".\\Data\\Q4\\Admin\\FinalReport.txt"
ANSWERS: str = ".\\Data\\Q4\\Admin\\AnswerKey.txt"


def qa_mapping(filename: str) -> dict[str, str]:
    """returns the question: answer map from a file"""
    
    qa = {}
    with open(filename) as file:
        for line in file:
            question, answer = line.split()
            qa[question] = answer
    return qa
    
    
def score(responses: dict[str, str], key: dict[str, str]) -> int:
    """returns the score of a student in the JEE Exam
    key is the answer-key according to which evaluation is to be done"""
    
    questions = [str(i) for i in range(1, 21)]
    total = 0
    
    for q in questions:
        if responses[q] == "-":
            total += 0
        elif responses[q] == key[q]:
            total += 4
        else:
            total -= 1
    
    return total


def write_file(data: list[list[str]]) -> None:
    """writes student data into the file"""
    
    with open(FINAL_REPORT, "w") as file:
        for line in data:
            line = str(line).lstrip("[").rstrip("]").replace(",", "")
            file.write(line.replace("'", "") + "\n")


def main() -> None:
    """__main__ function"""
    
    key = qa_mapping(ANSWERS)
    data = []
   
   # traverse through the folder and find every student file 
    for student in os.listdir(STUDENT_FOLDER):
        filename = f".\\Data\\Q4\\Student\\{student}"
        name, roll = student.strip(".txt").split("_")
        points = score(qa_mapping(filename), key)
        data.append([name, roll, points])
    
    write_file(data)
    
    print("Students evaluated successfully")
    print("File FinalReport.txt has been created")
    

if __name__ == "__main__":
    main()