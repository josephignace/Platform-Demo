from cohortextractor import StudyDefinition, patients # NOQA

# set index date
index_date = "2020-01-01"

# Study population
study = StudyDefinition(
    default_expectations={
        "date": {
            "earliest": index_date,
            "latest": "today",
            },  # data range for simulated dates
        "rate": "uniform",
        "incidence": 1,
    },
    # Define study population
    population=patients.registered_as_of(index_date),
    # define the stp variable we want to extract
    stp=patients.registered_practice_as_of(
        index_date,
        returning="stp_code",
        return_expectations={
            "category": {"ratios": {"STP1": 0.3, "STP2": 0.2, "STP3": 0.5}},
        },
    ),
)
