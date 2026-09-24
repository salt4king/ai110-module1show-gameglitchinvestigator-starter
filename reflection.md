# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
Looked like a simple numeber guessing app.
- List at least two concrete bugs you noticed at the start  
  -The hint would say the wrong thing where no matter what it would say "Go Higher" even if the number was lower.
  -When trying to create a new game no new guesses can be made.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  33.  |. Go Lower.            Go Higher.            none
|new game| New game starts |New game doesnt start| none
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude as an assistant
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested that the ranges for numbers for the different difficulties was not updating when the difficulty was changed. I asked it to explain the code and then pushed the update into my file.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
When fixing the New Game bug, the ai first pass also rewrote parse_guess for extra edge cases. I said that was overkill for this project and kept the simple try/except int(float()) version, then re-tested it with "33", "33.5", and a blank input to confirm it still worked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried the same steps that broke it before (like guessing 33 and clicking New Game) and checked if it worked right this time.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest with a test for guess 60 vs secret 50, and it showed the hint was fixed because it now said "go lower" instead of "go higher."
- Did AI help you design or understand any tests? How?
Yes, it pointed out my old tests were checking the wrong thing and helped me fix them so they actually worked.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click something, Streamlit reruns the whole app from the top, so you have to use session state to remember stuff like your score between clicks.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Writing down the bugs I find before asking AI to fix them so I know what "fixed" is supposed to look like.
- What is one thing you would do differently next time you work with AI on a coding task?
I'd run the tests first before changing anything so I know what was already broken.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I learned AI code can run with no errors and still be wrong, so I can't just trust it without checking.
