# AlumniRobotLibrary

**AI-Powered Robot Framework Library for Alumnium**  
Seamlessly integrate [Alumnium](https://github.com/alumnium-hq/alumnium) into your Robot Framework tests with support for Selenium, Playwright, multiple browsers, dynamic test data, error diagnostics, and AI-driven error summaries.

---

## Features

- **Supports Selenium & Playwright**: Choose your backend and browser (Chrome, Firefox, WebKit, Chromium).
- **AI Model Flexibility**: Use OpenAI, Anthropic, Gemini, DeepSeek, Ollama, or self-hosted LLMs.
- **Natural Language Automation**: Write test steps in plain English using Alumnium’s AI.
- **Self-Healing Actions**: Robust against UI changes.
- **Dynamic Test Data**: Instantly generate realistic user/account/address data.
- **Failure Diagnostics**: Automatic screenshot & HTML capture on failure.
- **AI Error Summaries**: (Optional) Get LLM-powered explanations and suggestions for test failures.
- **Custom Keyword Registration**: Extend with your own Python functions as keywords.

---

## Installation

pip install alumnium selenium playwright faker robotframework alumnirobotlibrary
playwright install


---

## Quick Start


*** Settings ***
Library AlumniRobotLibrary.py backend=playwright browser=webkit ai_provider=openai api_key=YOUR_OPENAI_KEY

*** Test Cases ***
AI Login Test With Dynamic Data
${user}= Generate Test Data user
Open Browser And Init Alumni https://practicetestautomation.com/practice-test-login/
Alumni Do enter ${user['username']} into username field
Alumni Do enter ${user['password']} into password field
Alumni Do click the login button
Alumni Check page contains error message
Alumni Quit



---

## Usage

### Supported Arguments

| Argument      | Description                                    | Example Values                  |
|---------------|------------------------------------------------|---------------------------------|
| backend       | Automation backend                             | selenium, playwright            |
| browser       | Browser to use                                 | chrome, firefox, webkit         |
| headless      | Run browser headless                           | True, False                     |
| ai_provider   | LLM provider for Alumnium                      | openai, anthropic, google, ...  |
| ai_model      | Model name (optional)                          | gpt-4o, claude-3-haiku, etc.    |
| api_key       | API key for your LLM provider                  | YOUR_API_KEY                    |
| api_base      | Custom API base (for self-hosted/Ollama)       | http://localhost:11434          |
| screenshot_dir| Directory for failure screenshots & HTML       | alumni_failures                 |

### Keywords

- `Open Browser And Init Alumni    <url>`
- `Alumni Do    <natural language command>`
- `Alumni Check    <check command>`
- `Alumni Get    <get command>`
- `Generate Test Data    <data_type>`
- `Register Custom Keyword    <name>    <python_func>`
- `Alumni Quit`

---

## Advanced Features

- **AI Error Summaries**: Enable AI-powered explanations for failures (requires relevant API key and provider).
- **Extensible**: Register your own Python functions as Robot Framework keywords at runtime.
- **Rich Diagnostics**: Screenshots and HTML are saved on every failure for easy debugging.

---

## Example: AI Error Summary

On failure, the library can call your configured LLM to provide a summary and suggestion:

[AlumniRobotLibrary] Failure in alumni_do('click the login button'):
ElementNotFoundException: ...
Screenshot: alumni_failures/alumni_do_20240515_123456.png
HTML: alumni_failures/alumni_do_20240515_123456.html
Traceback:
...
AI Summary: The login button was not found. This may be due to a UI change...



---

## Requirements

- Python 3.7+
- [Alumnium](https://github.com/alumnium-hq/alumnium)
- [Robot Framework](https://robotframework.org/)
- [Selenium](https://selenium.dev/) or [Playwright](https://playwright.dev/python/)
- [Faker](https://faker.readthedocs.io/)
- LLM provider SDKs as needed (`openai`, `anthropic`, etc.)

---

## Contributing

Pull requests and feature requests are welcome!  
Please open an issue to discuss your ideas or report bugs.

---

## License

MIT License

---

## Links

- [Alumnium Documentation](https://alumnium.ai/docs/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Playwright Python](https://playwright.dev/python/)

---

**Supercharge your Robot Framework tests with AI-powered automation and diagnostics!**
