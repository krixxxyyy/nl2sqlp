"""
lm_adapter.py

AUTO-SAFE LM ADAPTER

This adapter:
- Tries to detect a usable inference entry point
- Uses the LM ONLY if it can be called safely
- Falls back to conservative intent hints otherwise
- NEVER generates SQL
- NEVER crashes
"""

import os
import sys


# -------------------------------------------------
# Attempt to add universal_nl2sql_lm to PYTHONPATH
# -------------------------------------------------
LM_DIR = os.path.join(os.path.dirname(__file__), "..", "universal_nl2sql_lm")

if os.path.isdir(LM_DIR) and LM_DIR not in sys.path:
    sys.path.append(LM_DIR)


# -------------------------------------------------
# Try to detect a callable inference function
# -------------------------------------------------
LM_AVAILABLE = False
LM_INFER = None

try:
    # Try common inference naming patterns
    from universal_nl2sql_lm import infer  # type: ignore
    LM_INFER = infer
    LM_AVAILABLE = True
except Exception:
    try:
        from universal_nl2sql_lm import predict  # type: ignore
        LM_INFER = predict
        LM_AVAILABLE = True
    except Exception:
        LM_AVAILABLE = False


def lm_suggest_intent(nl_query):
    """
    Suggest intent hints in a STRUCTURED, SAFE way.

    Output contract (MANDATORY):
    {
        "aggregation": "AVG" | "MAX" | "SUM" | "MIN" | None,
        "group_by": "department" | None,
        "confidence": float (0.0 – 1.0)
    }
    """

    # -------------------------------------------------
    # CASE 1: LM IS AVAILABLE (SAFE USE)
    # -------------------------------------------------
    if LM_AVAILABLE and callable(LM_INFER):
        try:
            result = LM_INFER(nl_query)

            # Accept ONLY structured outputs
            if isinstance(result, dict):
                return {
                    "aggregation": result.get("aggregation"),
                    "group_by": result.get("group_by"),
                    "confidence": float(result.get("confidence", 0.0))
                }

        except Exception:
            # Any LM failure → safe fallback
            pass

    # -------------------------------------------------
    # CASE 2: SAFE FALLBACK (RULE-ONLY)
    # -------------------------------------------------
    q = nl_query.lower()

    if "highest" in q and "department" in q:
        return {
            "aggregation": "MAX",
            "group_by": "department",
            "confidence": 0.55   # below auto-accept threshold
        }

    if ("average" in q or "avg" in q) and "department" in q:
        return {
            "aggregation": "AVG",
            "group_by": "department",
            "confidence": 0.65
        }

    if ("total" in q or "sum" in q) and "department" in q:
        return {
            "aggregation": "SUM",
            "group_by": "department",
            "confidence": 0.65
        }

    # -------------------------------------------------
    # DEFAULT: NO SUGGESTION
    # -------------------------------------------------
    return {
        "aggregation": None,
        "group_by": None,
        "confidence": 0.0
    }
