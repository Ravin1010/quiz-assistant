# Quiz Assistant Architecture

## Overview

The Quiz Assistant converts screenshots into structured multiple-choice questions that can later be analyzed by an LLM.

Pipeline:

```text
Screenshot
    │
    ▼
Capture Module
    │
    ▼
OCR Engine (Strategy Pattern)
    │
    ▼
Text Cleaner
    │
    ▼
Question Parser
    │
    ▼
MCQ Model
    │
    ▼
Prompt Builder
    │
    ▼
OpenAI GPT
    │
    ▼
Answer Formatter
```

---

## Design Principles

- Single Responsibility Principle
- Strategy Pattern for OCR engines
- Modular pipeline
- Test-driven development
- Backend-independent OCR
- Platform-independent core logic

---

## Current OCR Backend

Current implementation:

- EasyOCR

Future backends:

- Tesseract
- PaddleOCR
- Google Vision
- Azure Document Intelligence
- OpenAI Vision