def get_grade(marks):
    if marks >= '85':
        return 'A'
    elif marks >= '75' :
        return 'B'
    elif marks >= '55':
        return 'C'
    else:
        return 'D'
    
def is_pass(marks):
    return marks >= '25'