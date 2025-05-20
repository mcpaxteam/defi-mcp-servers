# MCP Lending Rates Server

This MCP server provides lending rates based on input parameters such as collateral type, loan duration, and loan amount.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way to calculate lending rates in a DeFi environment. This can be used by lenders and borrowers to make more informed decisions.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_lending_rates:app --host 0.0.0.0 --port 8003
    ```

4.  Send a GET request to the `/mcp/defi/lending_rate` endpoint with the following query parameters:

    *   `collateral_type`: The type of collateral being used (e.g., ETH, BTC).
    *   `loan_duration`: The duration of the loan in days.
    *   `loan_amount`: The amount of the loan.
    *   `market_conditions` (optional): The current market conditions (e.g., bullish, bearish).

    Example:

    ```
    http://localhost:8003/mcp/defi/lending_rate?collateral_type=ETH&loan_duration=30&loan_amount=10000&market_conditions=bullish
    ```

5.  The server will return a JSON response containing the lending rate and the input parameters.

## Example Response

```json
{
    "lending_rate": 0.06,
    "collateral_type": "ETH",
    "loan_duration": 30,
    "loan_amount": 10000,
    "market_conditions": "bullish"
}
