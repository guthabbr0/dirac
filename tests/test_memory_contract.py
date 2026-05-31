from dirac.memory.contracts import is_discord_id, normalize_discord_id, parse_confidence, parse_tags


def test_normalizes_mentions_to_snowflake() -> None:
    assert normalize_discord_id("<@!123456789012345678>") == "123456789012345678"
    assert is_discord_id("123456789012345678")


def test_parse_tags_from_csv() -> None:
    tags, error = parse_tags("alpha, beta")
    assert error is None
    assert tags == ("alpha", "beta")


def test_confidence_bounds_are_explained() -> None:
    value, error = parse_confidence("2")
    assert value == 0.7
    assert error is not None
