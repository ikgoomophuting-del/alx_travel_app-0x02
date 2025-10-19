# alx_travel_app-0x02
cp -r alx_travel_app_0x01 alx_travel_app_0x02

## Chapa Payment Integration 

- Integrated Chapa API for secure payments
- Created Payment model to store transaction info
- Added `/payments/initiate/` and `/payments/verify/` endpoints
- Uses `CHAPA_SECRET_KEY` from environment
- Tested with Chapa sandbox API — verified successful initiation and completion

### Example Payload:
```json
{
  "amount": "100.00",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "booking_reference": "BOOK12345"
}
```
---

## Testing (in Sandbox)

Use cURL or Postman to test:

### Initiate:
```bash
curl -X POST http://127.0.0.1:8000/api/payments/initiate/ \
  -H "Content-Type: application/json" \
  -d '{"amount":"100","email":"test@example.com","booking_reference":"BOOK123"}'
```
