# MCP Stablecoin APY Server

This MCP server provides a stablecoin APY based on input parameters such as stablecoin name, deposit amount, and lockup period.

## Purpose

The purpose of this MCP server is to provide a simple and easily accessible way to calculate the APY for depositing stablecoins in a DeFi environment. This can be used by stablecoin holders to make more informed decisions about where to deposit their funds.

## Usage

To use this MCP server, you will need to:

1.  Install Python 3.7+
2.  Install FastAPI and Uvicorn:

    ```bash
    pip install fastapi uvicorn
    ```
3.  Run the server using Uvicorn:

    ```bash
    uvicorn mcp_stablecoin_apy:app --host 0.0.0.0 --port 8004
    ```

4.  Send a GET request to the `/mcp/defi/stablecoin_apy` endpoint with the following query parameters:

    *   `stablecoin_name`: The name of the stablecoin (e.g., USDT, USDC).
    *   `deposit_amount`: The amount of stablecoin being deposited.
    *   `lockup_period`: The lockup period in days.
    *   `platform_risk` (optional): The risk score of the platform offering the APY.

    Example:

    ```
    http://localhost:8004/mcp/defi/stablecoin_apy?stablecoin_name=USDT&deposit_amount=1000&lockup_period=30&platform_risk=0.1
    ```

5.  The server will return a JSON response containing the stablecoin APY and the input parameters.

## Example Response

```json
{
    "stablecoin_apy": 0.025,
    "stablecoin_name": "USDT",
    "deposit_amount": 1000,
    "lockup_period": 30,
    "platform_risk": 0.1
}
