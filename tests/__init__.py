# PopulationSim
# See full license in LICENSE.txt.

import sys
from pathlib import Path

EXPECTED_DIR = Path(__file__).parent / "expected"


def expected_path(name: str) -> Path:
    """Return the platform-specific expected parquet file.

    Returns ``expected/<platform>/<name>.parquet`` (e.g.
    ``expected/linux/expanded.parquet``).
    """
    return EXPECTED_DIR / sys.platform / f"{name}.parquet"
