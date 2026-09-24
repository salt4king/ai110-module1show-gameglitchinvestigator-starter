from logic_utils import check_guess

# FIX: these three starter tests compared the raw check_guess() return value
# (a (outcome, message) tuple) directly to a string, e.g.
# assert check_guess(60, 50) == "Too High", so they failed on collection
# before any of my bug fixes. AI caught the mismatch while running pytest
# for the first time; I unpacked the tuple to match check_guess's actual
# contract and reran pytest to confirm all tests pass.
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# FIX: new tests targeting the swapped-hint bug in check_guess (see
# logic_utils.py). AI drafted these after I described the bug; I picked the
# guess/secret values (60/50 and 40/50) and ran pytest to confirm they fail
# against the old backwards messages and pass against the fix.
def test_too_high_hint_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()

def test_too_low_hint_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()
