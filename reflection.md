# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  On the left side of the game it showed the diffculty level and the amount of guesses. In the bottom of the game it showed new game and hints. In the middle you are able to type your guess. The top it shows the title "Game Glitch Investigator."

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. normal and hard are switched
  2. secret number is visible in the Developer Debug Info section
  3. when starting a new game it ignores the diffculty that is selected


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Select Hard Range:1-100      Range 1-50        No error

Guess a    "Go LOWER"        "Go HIGHER"       No error
number too 
high(101)

Guess a    "Go HIGHER"       "Go LOWER"        No error
number too 
lower(-1)

Open Developer Game data     data should be hidden No error
Debug Info     should be hidden
               and also the 
               number



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

The AI tools that I used is ChatGPT and Claude. I used a mix of both to cross reference if both of the AI bots are right. Therefore this is what I used in this project. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One suggestion that AI gave is check_guess() function where by correcting the high/low hint logic. If the guess was higher than the secret number the game returns as "Too High" and tell the player to go lower. I vertified this my pythin3 -m pytest which passed the test.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One suggest that AI suggested is when I was entering pytest it gave me an error. I told AI bot that it was able to clear the situation. I verified this by running the terminal.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided whether a bug was fixed is to run the game again and also verify it with another AI bot(chatgpt). For the game I was able to know that the code that claude gave me worked. For AI bot i was able to cross reference if the bug in the code was fixed directly.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Pytest is a tsting tool for pythong that  runs test cases and checks whether the vode is behaved. I used the pytest and it showed that 5 test cases passed. I used python3-m pytest.

Terminal output from running the tests:

```
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
```


- Did AI help you design or understand any tests? How?

AI helped me with understanding how to design tests by saying how the update_score should be moved from app.py to logic_utils.py before it can be tested. It helped me understand that the logic before this, so that the tests can happen. Therefore, AI help me to understand the tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

The way that Streamlit works is by rerunning a script, when a user has an interactions with the app such as clicking an icon or entering info. This also means that regular features are reset as well.  In additon, Streamlit uses session state where it keeps information between reuns. It allows the ap to remember multiple voices such as scores settings and inputs. 



---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit or strategy that I learned from this project is usuing pip. Before this project I didn't learn how to do pip install or even add libararies. I learned how important it is to add them.



- What is one thing you would do differently next time you work with AI on a coding task?

The one thing that I would do differently next time I work with AI on a coding task is separate  AI chats. I feel like this would make it more organized. Otherwise I would need to scroll up to find the chat I am looking for. 



- In one or two sentences, describe how this project changed the way you think about AI generated code.

This projects help me to learn how AI can help with debugs and how to use it.
