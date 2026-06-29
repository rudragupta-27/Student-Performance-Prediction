import pandas as pd


def prepare_input(
    gender,
    race,
    parent_education,
    lunch,
    test_preparation,
    reading_score,
    writing_score
):
    """
    Convert user input into a DataFrame for prediction.
    """

    input_df = pd.DataFrame(
        {
            "gender": [gender],
            "race/ethnicity": [race],
            "parental level of education": [parent_education],
            "lunch": [lunch],
            "test preparation course": [test_preparation],
            "reading score": [reading_score],
            "writing score": [writing_score],
        }
    )

    return input_df