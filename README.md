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

- [ ] Describe the game's purpose.
<<<<<<< HEAD
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.
=======
The game purpose is to guess a number. It has a different ranges, diffculty and also amount of guess. It would day if it goes higher or lower.


- [ ] Detail which bugs you found.
  1. The higher/lower hints were wrong because the guess and the secret were
     compared as different types (number vs. text), so the game could not be won.
  2. A wrong "Too High" guess added points on even attempts instead of losing them.
  3. The secret number was being turned into text on even attempts, which caused
     the broken hint comparison.
  4. "New Game" did not fully reset the game, and changing the difficulty did not
     pick a new secret number for the new range.


- [ ] Explain what fixes you applied.
  1. Moved `parse_guess`, `check_guess`, and `update_score` out of `app.py` into
     `logic_utils.py` so the game logic can be imported and tested on its own.
  2. Fixed `check_guess` to convert both the guess and the secret to numbers
     before comparing, so the higher/lower hints are now correct (it returns
     "Win", "Too High", or "Too Low").
  3. Fixed `update_score` so a wrong "Too High" guess always loses 5 points
     instead of adding points on even attempts.
  4. Removed the code in `app.py` that turned the secret into text on even
     attempts, so it stays a number.
  5. Added pytest tests for the score fix and confirmed all 5 tests pass
     (see Test Results below).

  Still open (found but not fixed yet): "New Game" doesn't fully reset the
  game, changing difficulty doesn't pick a new secret, and Hard has an easier
  range than Normal.

>>>>>>> 8110ff4 (Initial commit)

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

<<<<<<< HEAD
1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->
=======
1. User's enters "50" as guess
2. Game returns "Too Low"
3. User's enters "75" as guess
4. Game returns "Too High"
5. Game end when user enter correct guess or runs out of attempts
6. User can play again or pick different range.
>>>>>>> 8110ff4 (Initial commit)

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
<<<<<<< HEAD
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
=======
$ python3 -m pytest tests/ -v
============================= test session starts ==============================
platform darwin -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
cachedir: .pytest_cache
rootdir: /Users/shy25/Downloads/ai110-module1show-gameglitchinvestigator-starter-main
plugins: anyio-4.13.0
collecting ... collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_too_high_loses_points_on_even_attempt PASSED [ 80%]
tests/test_game_logic.py::test_too_high_loses_points_on_odd_attempt PASSED [100%]

============================== 5 passed in 0.01s ===============================
>>>>>>> 8110ff4 (Initial commit)
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
