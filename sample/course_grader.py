# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """
    Converts a numerical score into a letter grade.

    Args:
        score (int or float): The numerical score to be converted into a letter grade.

    Returns:
        str: The letter grade corresponding to the input score.

    Raises:
        ValueError: If the input score is outside the range of 0 to 100.
        TypeError: If the input score is not of type int or float.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
