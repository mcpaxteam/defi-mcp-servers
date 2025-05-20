from fastapi import FastAPI, Query
from typing import Dict
import random

app = FastAPI(
    title="MCP DAO Voting",
    description="A simple MCP server that simulates a DAO voting process.",
    version="0.1.0",
)

@app.get("/mcp/dao/vote")
async def get_vote_result(
    proposal_id: int = Query(..., description="The ID of the proposal being voted on."),
    voter_weights: Dict[str, float] = Query(
        ..., description="A dictionary of voter addresses and their corresponding voting weights."
    )
):
    """
    Simulates a DAO voting process and returns the result.
    """

    # Simulate the voting process
    total_votes_for = 0
    total_votes_against = 0

    for voter, weight in voter_weights.items():
        if random.random() > 0.5:  # Simulate a vote for or against
            total_votes_for += weight
        else:
            total_votes_against += weight

    # Determine the result
    if total_votes_for > total_votes_against:
        result = "Passed"
    else:
        result = "Failed"

    return {
        "proposal_id": proposal_id,
        "total_votes_for": total_votes_for,
        "total_votes_against": total_votes_against,
        "result": result,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
