# grade = float(input())

# if 2 <= grade < 3:
#     result = "Fail"
# elif grade < 3.5:
#     result = "Poor"
# elif grade < 4.5:
#     result = "Good"
# elif grade < 5.5:
#     result = "Very Good"
# elif grade >= 5.5:
# #     result = "Excellent"
# # print(result)
def grade_type(grade):
    if 2 <= grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.5:
        return "Good"
    elif grade < 5.5:
        return "Very Good"
    elif grade >= 5.5:
        return "Excellent"


grade = float(input())
print(grade_type(grade))
#

# def type_of_grade(score):
#     if 2.00 <= score <= 2.99:
#         return 'Fail'
#     elif 3.00 <= score <= 3.49:
#         return "Poor"
#     elif 3.50 <= score <= 4.49:
#         return "Good"
#     elif 4.50 <= score <= 5.49:
#         return "Very Good"
#     elif 5.50 <= score <= 6.00:
#         return "Excellent"
#
#
# score = float(input())
# print(type_of_grade(score))
