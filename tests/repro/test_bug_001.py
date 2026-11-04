import re
import pytest
from fastapi.testclient import TestClient

from demo_app import app
from shop.pricing import tax_for_items


def test_receipt_and_checkout_tax_agree_for_dime_items():
    # Receipt rounds each line item: round(0.10*0.0825,2)=0.01 x3 = 0.03
    assert tax_for_items([0.10, 0.10, 0.10], 0.0825) == pytest.approx(0.03)
    client = TestClient(app)
    response = client.get("/checkout-preview")
    assert response.status_code == 200
    assert "Receipt tax:</strong> $0.03" in response.text
    assert "Checkout tax:</strong> $0.03" in response.text
    amounts = re.findall(r"\$(\d+\.\d{2})", response.text)
    assert amounts[:2] == ["0.03", "0.03"]
