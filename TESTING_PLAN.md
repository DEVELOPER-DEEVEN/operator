# Testing Plan

## 1. Unit Tests
- **Server Logic**: Verify `process_step` handles inputs correctly.
- **Guardrails**: Test `GuardrailService` with safe and unsafe prompts.
- **Vector Store**: Test `VectorStore` fallback when Firestore is missing.
- **Spanner**: Test `SpannerClient` connection handling.

## 2. Integration Tests
- **End-to-End Flow**: Mock Gemini response and verify the full pipeline from `process` endpoint to action response.
- **Database Integration**: Verify data is actually written to Firestore/Spanner (using emulators or test projects).

## 3. Manual Verification
- **Accessibility**: Manually trigger switch mappings.
- **Security**: Try to inject "rm -rf" commands and verify blocking.

## 4. Performance Testing
- **Latency**: Measure `X-Process-Time` header under load.
