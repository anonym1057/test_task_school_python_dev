"""
author: Nosova Olga
email: nosova-olenka@mail.ru

Calculate Student's grade given 4 scores.
For correct answers for tests 1a and 1b one could achieve 10 and 10 points respectively.
For 2-nd test - 30 points.
For 3rd test - 50 points.
If student passes first 3 tests then  his total_score will be 50 points? Which corresponds to letter grade B.
Following is a correspondence table:
[10, 10, 30, 50]  D D B B
"""

MAX_GRADES_NUM = [10, 10, 30, 50]


def get_grades():
    """
    Receives grades from user

    :return: grades - list[int]
    """
    print("Input 4 grades.\n"
          "For ending, enter 'n'")

    grades=[]
    for i,max_grade in enumerate(MAX_GRADES_NUM):
        print("\nTest ", i+1, '\nMax grade: ', max_grade)

        while (True):
            g = input(f"Enter grade: ")

            if g == 'n':
                return None

            try:
                grade = int(g)
            except Exception:
                print(f"Error: invalid format")
                continue

            if grade >= 0 and grade <= max_grade:
                grades.append(grade)
                break
            else:
                print(f"Error: grade should be 0 <= grade <= {max_grade}")

    return grades


def calculate_grade(grade:int,max_grade:int):
    """
    Calculate grade in the format of letters.
    Using Academic grading in the United States:
    Letter Grade	Percentage
        A	         90%-100%
        B	         80%-89%
        C	         70%-79%
        D	         60%-69%
        E	         50%-59%
        F	         0%-49%

    :param grade: int
    :param max_grade: int
    :return: grade in format letter
    """
    percent=grade/max_grade

    if percent <=1 and percent >=0.9:
        return 'A'
    elif percent <=0.89 and percent >=0.8:
        return 'B'
    elif percent <= 0.79 and percent >= 0.7:
        return 'C'
    elif percent <= 0.69 and percent >= 0.6:
        return 'D'
    elif percent <= 0.59 and percent >= 0.5:
        return 'E'
    elif percent <= 0.49 and percent >= 0.0:
        return 'F'
    else:
        print("Error invalid format grade or max_grade")
        return None


if __name__ == '__main__':
    grades_num=get_grades()
    grades_let=[]
    if grades_num:
        grades_let=[calculate_grade(grade,MAX_GRADES_NUM[i]) for i,grade in enumerate(grades_num)]

        print("\nResult:")
        print("Grade num: ", grades_num)
        print("Sum grade: ", sum(grades_num))
        print("Grade let: ",grades_let)
        print("Sum grade: ",calculate_grade(sum(grades_num),sum(MAX_GRADES_NUM)))