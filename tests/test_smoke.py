"""Phase 0 smoke test: the package and all subpackages import."""

import aiagentready
import aiagentready.analyzer
import aiagentready.generators
import aiagentready.grounding
import aiagentready.validation


def test_version():
    assert aiagentready.__version__ == "0.0.1"


def test_subpackages_importable():
    assert aiagentready.analyzer is not None
    assert aiagentready.generators is not None
    assert aiagentready.grounding is not None
    assert aiagentready.validation is not None
