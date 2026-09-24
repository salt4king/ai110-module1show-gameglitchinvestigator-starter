# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  This is a simple number guessing game built with Streamlit. You pick a difficulty, guess a number, and get hints until you win or run out of attempts.
- [x] Detail which bugs you found.
  - The hint was backwards: guessing too high told you to "Go Higher" instead of "Go Lower" (and the same for too low).
  - Clicking "New Game" after winning or losing didn't actually let you play again — it froze the game.
  - The starter pytest tests were checking the wrong thing, so they failed even when the code worked.
- [x] Explain what fixes you applied.
  - Fixed `check_guess` so the hint text matches the actual outcome ("Too High" now says go lower, "Too Low" now says go higher).
  - Fixed "New Game" to also reset the game status, the guessed number range, and the guess history, so a fresh game actually starts.
  - Refactored the game logic (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) out of `app.py` and into `logic_utils.py`.
  - Fixed the starter tests and added new tests that specifically check the hint bug is fixed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run the app and pick a difficulty (Easy, Normal, or Hard) from the sidebar.
2. Type a guess and click "Submit Guess."
3. Read the hint — it now correctly tells you to go higher or lower.
4. Keep guessing until you hit the secret number and see the win message.
5. Click "New Game" to reset and play again as many times as you want.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
pytest tests/ -v

tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high PASSED
tests/test_game_logic.py::test_guess_too_low PASSED
tests/test_game_logic.py::test_too_high_hint_tells_player_to_go_lower PASSED
tests/test_game_logic.py::test_too_low_hint_tells_player_to_go_higher PASSED

========================= 5 passed in 0.02s =========================
```

## 🚀 Stretch Features

- [ ] Did not attempt Challenge 4 (Enhanced UI) for this submission.
