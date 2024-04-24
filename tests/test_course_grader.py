import pytest
from course_grader import convert_to_letter_grade

class TestConvertToLetterGrade:
    
    # TODO-1: Add test_exact_grade_boundaries() function
    def test_exact_boundaries(self):
        assert convert_to_letter_grade(0) == 'F'
        assert convert_to_letter_grade(59) == 'F'
        assert convert_to_letter_grade(60) == 'D'
        assert convert_to_letter_grade(69) == 'D'
        assert convert_to_letter_grade(70) == 'C'
        assert convert_to_letter_grade(79) == 'C'
        assert convert_to_letter_grade(80) == 'B'
        assert convert_to_letter_grade(89) == 'B'
        assert convert_to_letter_grade(90) == 'A'
        assert convert_to_letter_grade(100) == 'A'
    
    # TODO-2: Add test_invalid_numerical_score() function
    def test_invalid_numerical_score(self):
        # Test below 0
        with pytest.raises(ValueError) as e:
            convert_to_letter_grade(-1)
        assert str(e.value) == "Score must be between 0 and 100."
        
        # Test above 100
        with pytest.raises(ValueError) as e:
            convert_to_letter_grade(101)
        assert str(e.value) == "Score must be between 0 and 100."
    
    # TODO-3: Add test_non_numeric_input() function
    def test_non_numeric_type(self):
        # Test string input
        with pytest.raises(TypeError) as e:
            convert_to_letter_grade("abc")
        assert str(e.value) == "Score must be a numeric value."
        
        # Test list input
        with pytest.raises(TypeError) as e:
            convert_to_letter_grade([1, 2, 3])
        assert str(e.value) == "Score must be a numeric value."
        
        # Test None input
        with pytest.raises(TypeError) as e:
            convert_to_letter_grade(None)
        assert str(e.value) == "Score must be a numeric value."
