Test strategy

# Unit testing
Most of logic should be covered by cheap, fast and realiable unit testing. The start of things can be checked on **test_logic.py**, but it could be expanded if we find it needed.

# Integration / App testing
Some basic testing should target the entire app. Can we start the app? Can we do a happy path? Can the app handle exceptions and error messages? These are more expensive and time consuming, so it shouldn't cover all the permutations from the unit testing; but there are some things that need to be checked at an app level. You can find this on **test_app.py**

# UI / EndToEnd testing
Some smoke tests and things that could only cover by the UI should be checked at this level. This will start the app and use a browser to click and go through it. Only a smoke test verifying a happy path, as well as things that are only UI based (copying too much text, maybe strange characters, etc.). You can find this on **test_browser.py**

# Non-functional / Extra funky / We are scared of this
This is all the extra. If it's critical, we can add performance tests creating a huge load (something like Vegetta). Security measures checking strings that inject anything. Fuzzy testing needed? It's about finding what is relevant, and what is worth doing (as waiting for results takes time, and maintaining the tooling and tests takes effort).