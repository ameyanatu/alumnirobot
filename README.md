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
- **Comprehensive Diagnostics**: Automatic screenshots and HTML capture on test failures
- **AI-Powered Error Analysis**: Get intelligent explanations and fix suggestions for test failures
- **Extensible Framework**: Easily register custom Python functions as keywords

## Installation

```bash
pip install alumnium selenium playwright faker robotframework alumnirobotlibrary
playwright install