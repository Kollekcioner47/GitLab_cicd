import os
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

API_URL = os.getenv("API_URL", "http://backend:8000")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_URL}/api/deals")
        deals = resp.json()
    
    rows = "".join(
        f"<tr><td>{d['id']}</td><td>{d['client_name']}</td>"
        f"<td>{d['amount']}</td><td style='color:green;'>{d['status']}</td></tr>"
        for d in deals
    )
    
    return f"""
    <html><head><title>Mini CRM</title></head><body>
    <h1>CRM Deals</h1>
    <table border="1" cellpadding="5">
    <tr><th>ID</th><th>Client</th><th>Amount</th><th>Status</th></tr>
    {rows}
    </table></body></html>
    """
