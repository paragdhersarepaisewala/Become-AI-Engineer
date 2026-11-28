# Project (Chapter 11): API Data Fetcher, Pydantic Validator & JSON Archiver

Fetch JSON records from an HTTP endpoint using `requests`, validate them with Pydantic, and save cleaned results to disk.

## Architecture Steps

1. Write `fetch_json(url, timeout)` handling `RequestException` and non-200 statuses.
2. Validate payloads with a Pydantic `BaseModel`.
3. Save validated records to a JSON file and test against a local mock HTTP server.

## Milestones

- [ ] Implement timeout-safe requests fetcher
- [ ] Validate API JSON responses with Pydantic
- [ ] Save results to JSON file & pass pytest
