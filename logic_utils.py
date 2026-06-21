def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Moved parse_guess from app.py into logic_utils.py with Claude (agent mode);
# collapsed the None/"" checks into `if not raw` and narrowed the bare except.
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    return True, value, None


# FIX: Moved check_guess from app.py into logic_utils.py with Claude (agent mode);
# fixed the str/int comparison glitch by coercing both to int, and returns just
# the outcome string (matching the existing tests) instead of an (outcome, message) tuple.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    Both values are coerced to int so a string/int mix compares numerically.

    Returns one of: "Win", "Too High", "Too Low"
    """
    guess, secret = int(guess), int(secret)

    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


# FIX: Moved update_score from app.py into logic_utils.py with Claude (agent mode);
# removed the glitch where "Too High" added +5 on even attempts so a wrong guess
# always loses 5 points (covered by the new regression tests).
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    A correct guess ("Win") awards points that decrease with each attempt
    (floored at 10). Any wrong guess ("Too High" / "Too Low") loses 5 points.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
