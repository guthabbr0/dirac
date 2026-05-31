from dirac.context.filters import contains_dirac_fenced_block, strip_dirac_fenced_blocks


def test_strips_exact_dirac_fence() -> None:
    text = "before\n```dirac\ninternal runtime output\n```\nafter"
    assert strip_dirac_fenced_blocks(text) == "before\nafter"
    assert contains_dirac_fenced_block(text)


def test_preserves_non_exact_fence_language() -> None:
    text = "```bash dirac eats it\necho keep\n```"
    assert strip_dirac_fenced_blocks(text) == text
