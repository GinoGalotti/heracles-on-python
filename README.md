<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Twelve_Labours_Altemps_Inv8642.jpg" height="300px"/>

## The challenge: Money Formatting

Given an amount of money as a number, format it as a string. Add associated tests for the functionality and for the user interface. 

```js
formatMoney(2310000.159897); // '2 310 000.16'
formatMoney(1600); // '1 600.00'
```

This needs to be a "fully working application" (you choose the format: web, cli, backend-frontend, mobile app, ...)

*eg: A simple HTML page with an input box*

## Requirements

I think it on Python 3.9, and requiring the libraries pytest, flask and selenium (they're on requirements.txt for CI jobs). Chromedriver needs to be on the PATH, but I've included the .exe file as I'm running it on PC. 

## How to run it

**run_test_venv.sh** and **run_tests.sh** should contain everything needed to run the tests. Before that, you need to start the application running *python app.py*, and then you could run all the test just running *pytest*

## Testing strategy

# Unit testing
Most of logic should be covered by cheap, fast and realiable unit testing. The start of things can be checked on **test_logic.py**, but it could be expanded if we find it needed.

# Integration / App testing
Some basic testing should target the entire app. Can we start the app? Can we do a happy path? Can the app handle exceptions and error messages? These are more expensive and time consuming, so it shouldn't cover all the permutations from the unit testing; but there are some things that need to be checked at an app level. You can find this on **test_app.py**

# UI / EndToEnd testing
Some smoke tests and things that could only cover by the UI should be checked at this level. This will start the app and use a browser to click and go through it. Only a smoke test verifying a happy path, as well as things that are only UI based (copying too much text, maybe strange characters, etc.). You can find this on **test_browser.py**

# Non-functional / Extra funky / We are scared of this
This is all the extra. If it's critical, we can add performance tests creating a huge load (something like Vegetta). Security measures checking strings that inject anything. Fuzzy testing needed? It's about finding what is relevant, and what is worth doing (as waiting for results takes time, and maintaining the tooling and tests takes effort).

## Improvements

Obviosuly this is only the barebones. But regarding to testing, we could improve

* Unit test could cover extra cases, and many regression errors we've found. We could also include some mocking to test the integration between systems in isolation
* On the app testing, we could test plenty of things regarding running out of memory and operational things that an app should be prepare and fail gracefully.
* UI testing is very expensive, so we should limit it to the minimum degree that still serve us value. We can offset it using fake browsers (like phantomJS) to get speed for the bulk of the tests, while still keeping some on real browsers.
* With non-functional the sky is the limit, but the value is on finding which are the areas we are worried about, what is the cost of running it and how can we make a solution general enough to be used on other systems.
