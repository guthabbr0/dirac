from dirac.provider.parameters import split_supported_params


def test_parameter_split_records_ignored_common_keys() -> None:
    result = split_supported_params({"temperature": 0.2, "reasoning": "high"}, {"temperature"})
    assert result.sent == {"temperature": 0.2}
    assert result.ignored == {"reasoning": "high"}
