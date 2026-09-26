from author_model import predict_author_signal

print(
    "Strong scholarly article:",
    predict_author_signal(
        10,
        True,
        True,
        False,
    )
)

print(
    "Average article:",
    predict_author_signal(
        1,
        True,
        False,
        False,
    )
)

print(
    "Weak source:",
    predict_author_signal(
        0,
        False,
        False,
        False,
    )
)