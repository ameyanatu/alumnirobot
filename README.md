# AlumniRobotLibrary

[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Robot Framework](https://img.shields.io/badge/Robot%20Framework-Latest-green.svg)](https://robotframework.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/alumnium-hq/alumnirobotlibrary/pulls)

**AI-Powered Robot Framework Library for Alumnium**

Bridge the gap between natural language and test automation

## Overview

AlumniRobotLibrary is an AI-powered Robot Framework library that seamlessly integrates [Alumnium](https://github.com/alumnium-hq/alumnium) into your test automation workflow. Write test steps in plain English and let AI handle the complexities of web automation.

## Key Features

- **Multiple Automation Backends**: Full support for both **Selenium** and **Playwright**
- **Cross-Browser Testing**: Run tests on Chrome, Firefox, WebKit, or Chromium
- **Flexible AI Integration**: 
  - OpenAI (GPT-4o, etc.)
  - Anthropic (Claude models)
  - Google (Gemini)
  - DeepSeek
  - Ollama & Self-hosted LLMs
- **Natural Language Commands**: Write test steps as you would explain them to a human
- **Self-Healing Actions**: Robust against UI changes and selector modifications
- **Dynamic Test Data Generation**: Create realistic user profiles, accounts, addresses, and more
- **Comprehensive Diagnostics**: Automatic screenshots and HTML capture on test failures
- **AI-Powered Error Analysis**: Get intelligent explanations and fix suggestions for test failures
- **Extensible Framework**: Easily register custom Python functions as keywords

## Installation

```bash
pip install alumnium selenium playwright faker robotframework alumnirobotlibrary
playwright install
```

## Quick Start

```robotframework
*** Settings ***
Library    alumnirobot.alumni_robot_library.AlumniRobotLibrary     backend=playwright    browser=chromium    headless=True    ai_provider=openai    ai_model=gpt-4o    api_key=YOUR_OPENAI_API_KEY

*** Variables ***
${LOGIN_URL}    https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Login With Dynamic User Profile
    [Documentation]    Generate a full user profile and attempt login using AI-powered keywords.
    ${user}=    Generate Test Data    user
    Open Browser And Init Alumni    ${LOGIN_URL}
    Alumni Do    enter ${user['username']} into username field
    Alumni Do    enter ${user['password']} into password field
    Alumni Do    click the login button
    Alumni Check    page contains error message
    Alumni Quit


```

## Usage Guide

### Configuration Options

| Parameter       | Description                           | Default       | Example Values                         |
|-----------------|---------------------------------------|---------------|----------------------------------------|
| `backend`       | Automation backend to use             | `selenium`    | `selenium`, `playwright`               |
| `browser`       | Target browser                        | `chrome`      | `chrome`, `firefox`, `webkit`, `edge`  |
| `headless`      | Run in headless mode                  | `False`       | `True`, `False`                        |
| `ai_provider`   | LLM provider for AI capabilities      | `openai`      | `openai`, `anthropic`, `google`, `ollama` |
| `ai_model`      | Specific model to use (optional)      | *provider default* | `gpt-4o`, `claude-3-haiku`, `gemini-pro` |
| `api_key`       | API key for chosen provider           | `None`        | `YOUR_API_KEY`                         |
| `api_base`      | Custom API endpoint (for self-hosted) | *provider default* | `http://localhost:11434`              |
| `screenshot_dir`| Directory for diagnostics files       | `alumni_failures` | `test_artifacts`, `screenshots`        |

### Core Keywords

| Keyword                         | Description                                        | Example |
|---------------------------------|----------------------------------------------------|---------|
| `Open Browser And Init Alumni`  | Start browser and initialize Alumnium with URL     | `Open Browser And Init Alumni    https://example.com` |
| `Alumni Do`                     | Execute an action using natural language           | `Alumni Do    click the submit button` |
| `Alumni Check`                  | Verify a condition using natural language          | `Alumni Check    page title is "Welcome"` |
| `Alumni Get`                    | Retrieve a value using natural language            | `${text}=    Alumni Get    text of welcome message` |
| `Generate Test Data`            | Create realistic test data of specified type       | `${user}=    Generate Test Data    user` |
| `Register Custom Keyword`       | Add your own Python function as a keyword          | `Register Custom Keyword    my_keyword    ${my_function}` |
| `Alumni Quit`                   | Close browser and clean up                         | `Alumni Quit` |

## Advanced Features

### AI-Powered Error Diagnosis

When a test fails, AlumniRobotLibrary can automatically:
1. Capture a screenshot and HTML of the page
2. Analyze the failure using AI
3. Provide detailed explanations and potential fixes

```
[AlumniRobotLibrary] Failure in alumni_do('click the login button'):
ElementNotFoundException: Could not find element matching criteria

📸 Screenshot: alumni_failures/alumni_do_20240515_123456.png
📄 HTML: alumni_failures/alumni_do_20240515_123456.html

🤖 AI Analysis:
   The login button was not found on the page. Possible reasons:
   - The page may not have finished loading
   - The button might have a different text or appearance than expected
   - A modal dialog might be blocking access to the button
   
   Suggested fixes:
   - Add a wait step before trying to click: "Alumni Do wait for page to load completely"
   - Try using a more specific selector: "Alumni Do click button with id 'login-btn'"
   - Check if you need to dismiss a dialog first
```

### Custom Keyword Registration

Extend AlumniRobotLibrary with your own Python functions:

```python
def custom_validation(element_id, expected_value):
    # Your custom validation logic here
    return result

# In your Robot Framework test:
Register Custom Keyword    validate_custom_element    ${custom_validation}
Alumni Do    click on the settings icon
validate_custom_element    user-preference    enabled
```

### Dynamic Test Data Types

The `Generate Test Data` keyword supports multiple data types:

- `user`: Complete user profile with name, username, email, password
- `address`: Physical address with street, city, state, zip
- `custom`: Specify your own schema

## System Requirements

- Python 3.7 or newer
- Robot Framework
- Selenium or Playwright
- Faker for test data generation
- Appropriate LLM provider SDK based on your chosen AI provider

## Contributing

We welcome contributions of all kinds! Here's how you can help:

- **Report Bugs**: Open an issue describing the bug and steps to reproduce
- **Suggest Features**: Have an idea? We'd love to hear it!
- **Submit PRs**: Implement new features or fix existing issues
- **Improve Documentation**: Help us make these docs even better

Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

## License

AlumniRobotLibrary is released under the [MIT License](LICENSE).

## Resources

- [AlumniRobotLibrary Documentation](https://alumnium.ai/docs/robot-framework/)
- [Alumnium Core Documentation](https://alumnium.ai/docs/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Playwright Python Documentation](https://playwright.dev/python/)

---

<div align="center">
  <strong>Supercharge your Robot Framework tests with AI-powered automation!</strong>
  <br>
  <br>
  <a href="https://github.com/alumnium-hq/alumnirobotlibrary/stargazers">
    <img src="https://img.shields.io/github/stars/alumnium-hq/alumnirobotlibrary?style=social" alt="Stars">
  </a>
</div>
