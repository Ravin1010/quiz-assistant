# ADR-0001

## Title

Use the Strategy Pattern for OCR engines.

## Status

Accepted

## Context

The application may support multiple OCR providers.

## Decision

Introduce BaseOCREngine and separate implementations.

## Consequences

Advantages:

- Easy to test
- Easy to extend
- Cleaner architecture

Disadvantages:

- Slightly more abstraction