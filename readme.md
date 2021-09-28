# Consumer Affairs Test Automation Challenge

> This is a automated test script for Consumer Affairs QA Engineer position challenge. 
> using selenium and pytest.

## ✅ Challenge Requirements.
URL to test: https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html

Required tests:
- [x] Verify Disclaimer
- [x] Verify Footer Text
- [x] Assert Social Links work
- [x] Assert "Find my match" redirects correctly
- [x] Verify first and last links on "related news links"

## ✨ Assumptions

There were no requirements or expected behaviours shared with me, so I assumed the correct
behaviour is the current website behaviour.

>### Classes and Fixtures:
>>####TestData:
>>* SimpleNamespace containing the test data, could be easily replaced for a factory to implement multiple scenarios.
>>#### Browser:
>>* This class encapsulates the common methods for browser interaction.
>>#### RecallArticlePage:
>>* Class for higher level test interactions with the article page. 
>>* The locators are inside the methods to simplify maintenance since there's no repetition on locators.
>### Tests:
>>#### Testing social links and "How it works":
>>* Tested just the button hrefs assuming the used API's are consolidated.
>>#### Testing related news:
>>* The provided article didn't have any related news, in this case the test skips.
>>* I assumed an article may have no related news, but left a skip message because if a lot of articles skip this test, it could be a bug related to the news not loading.
>>* In case the article has related news, it tests the first and last article the same way it tests the first one, excluding the related news step.
>>#### Testing Disclaimer and Footer text:
>>* I assumed the texts on the provided page were the correct.



## 💻 Get Started

Before starting you need the following dependencies:
* Install `Python 3` latest version 

## 🚀 Setup

Windows:

```
git clone https://github.com/metheuspsc/ca-test-automation.git
cd <project path>
python -m venv venv
./venv/scripts/activate
pip install -r requirements.txt
pytest
```
