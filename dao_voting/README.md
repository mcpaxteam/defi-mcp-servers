# MCP DAO Voting Server

This MCP server simulates a DAO voting process and returns the result based on voter weights.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way to simulate DAO voting. This can be used for testing voting mechanisms or for educational purposes.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_dao_voting:app --host 0.0.0.0 --port 8001
    ```

4.  Send a GET request to the `/mcp/dao/vote` endpoint with the following query parameters:

    *   `proposal_id`: The ID of the proposal being voted on.
    *   `voter_weights`: A dictionary of voter addresses and their corresponding voting weights.  This should be a JSON string.

    Example:

    ```
    http://localhost:8001/mcp/dao/vote?proposal_id=123&voter_weights={"0x123":0.6,"0x456":0.4}
    ```

5.  The server will return a JSON response containing the proposal ID, total votes for, total votes against, and the result.

## Example Response

```json
{
    "proposal_id": 123,
    "total_votes_for": 0.6,
    "total_votes_against": 0.4,
    "result": "Passed"
}
