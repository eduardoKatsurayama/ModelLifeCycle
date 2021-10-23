def temporal_series_train_test_split(
    dataset, last_only=False, validation=False
):
    statements = dataset.statement_due_date.sort_values().unique()

    if validation:
        yield (
            dataset[dataset.statement_due_date < statements[-1]].reset_index(drop=True),
            dataset[dataset.statement_due_date == statements[-1]].reset_index(drop=True)
        )

    statements = statements[-7:-1]

    for test_statement in statements:
        if last_only:
            if test_statement == statements[-1]:
                yield (
                    dataset[dataset.statement_due_date < test_statement].reset_index(drop=True),
                    dataset[dataset.statement_due_date == test_statement].reset_index(drop=True)
                )
        else:
            yield (
                dataset[dataset.statement_due_date < test_statement].reset_index(drop=True),
                dataset[dataset.statement_due_date == test_statement].reset_index(drop=True)
            )
