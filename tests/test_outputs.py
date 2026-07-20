import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json():
    """Success criterion 1: a single JSON object is written to /app/report.json."""
    assert REPORT.exists(), "no /app/report.json found"
    data = _load()
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_total_requests():
    """Success criterion 2: total_requests equals the number of log lines (6)."""
    assert _load()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips equals the distinct client IP count (3)."""
    assert _load()["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most-requested path (/index.html)."""
    assert _load()["top_path"] == "/index.html"
