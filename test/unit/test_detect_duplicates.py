import pytest
from unittest.mock import patch
from src.util.detector import detect_duplicates

# develop your test cases here


@pytest.mark.unit
def test_missing_data_raises_valueerror():
    # Arrange
    data = """"@article{test1,
        title={Test 1},
        author={Test Author 1},
        journal={Test Journal},
        pages={1--2},
        year={2025},
        publisher={Testing Team}
    }
    """
    parse_return_data = ["test1"]

    # Act & Assert
    with patch('src.util.detector.parse', return_value=parse_return_data, autospec=True):
        with pytest.raises(ValueError):
            detect_duplicates(data)

# @pytest.mark.unit
# def test_same_keys_returns_duplicates():
#     # Arrange

#     data = """"
#         @article{test1,
#         title={Test 1},
#         author={Test Author 1},
#         journal={Test Journal},
#         pages={1--2},
#         year={2025},
#         publisher={Testing Team},
#                 doi={123}
#     }

#     @article{test1,
#         title={Test 1},
#         author={Test Author 1},
#         journal={Test Journal},
#         pages={1--2},
#         year={2025},
#         publisher={Testing Team}
#     }
#     """

#     item1 = article()

#     parse_return_data = []

#     # Act & Assert
#     with patch('src.util.detector.parse', return_value=parse_return_data, autospec=True):
#         res = detect_duplicates(data)

#         assert res == parse_return_data


# @pytest.mark.unit
# def test_detect_duplicates():
#     assert True




# @pytest.mark.unit
# @pytest.mark.parametrize(
#     "test_input_data",
#     [
#     ("name@.com"),
#     (""),
#     (1337),
#     ]
# )
# def test_invalid_email_raises_valueerror(usercontroller, test_input_email):