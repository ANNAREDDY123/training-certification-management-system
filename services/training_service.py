def valid_training_status(status):

    return status in [
        "Upcoming",
        "Ongoing",
        "Completed"
    ]


def valid_completion_status(status):

    return status in [
        "Enrolled",
        "In Progress",
        "Completed",
        "Failed"
    ]


def valid_training_dates(start_date, end_date):

    return end_date > start_date


def valid_certificate_dates(issued_date, expiry_date):

    return expiry_date > issued_date
