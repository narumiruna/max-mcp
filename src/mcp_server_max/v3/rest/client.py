import base64
import hashlib
import hmac
import json
import os
import time
from typing import Any
from urllib.parse import urljoin

import httpx
from loguru import logger


class MAXRestClient:
    def __init__(
        self,
        api_key: str | None = None,
        api_secret: str | None = None,
        base_url: str = "https://max-api.maicoin.com",
    ) -> None:
        self.api_key = api_key or os.getenv("MAX_API_KEY", "")
        self.api_secret = api_secret or os.getenv("MAX_API_SECRET", "")
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
        }

    def auth(self, path: str, params: dict[str, Any]) -> None:
        logger.info("Authenticating request")
        params_to_sign = {**params, "path": path}
        json_str = json.dumps(params_to_sign)

        payload = base64.b64encode(json_str.encode()).decode()

        signature = hmac.new(
            self.api_secret.encode(),
            payload.encode(),
            hashlib.sha256,
        ).hexdigest()

        self.headers.update(
            {
                "X-MAX-ACCESSKEY": self.api_key,
                "X-MAX-PAYLOAD": payload,
                "X-MAX-SIGNATURE": signature,
            }
        )

    async def make_request(self, path, method="GET", params: dict[str, Any] | None = None):
        params = params or {}
        params["nonce"] = int(time.time() * 1000)

        if self.api_key and self.api_secret:
            self.auth(path, params=params)

        url = urljoin(self.base_url, path)
        async with httpx.AsyncClient() as client:
            if method == "GET":
                resp = await client.get(url, headers=self.headers, params=params)
                resp.raise_for_status()
            else:
                resp = await client.post(url=url, headers=self.headers, data=json.dumps(params))
                resp.raise_for_status()

        return resp.json()
