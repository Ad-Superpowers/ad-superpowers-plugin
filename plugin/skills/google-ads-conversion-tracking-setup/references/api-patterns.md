### Automated Import via API

```python
# PYTHON SCRIPT FOR OFFLINE CONVERSION UPLOAD
# Uses the Google Ads API

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def upload_offline_conversions(customer_id, conversions):
    """
    Upload offline conversions to Google Ads.

    Args:
        customer_id: Google Ads customer ID
        conversions: List of conversion dicts
    """
    client = GoogleAdsClient.load_from_storage()
    conversion_upload_service = client.get_service("ConversionUploadService")
    conversion_action_service = client.get_service("ConversionActionService")

    # Build conversion operations
    operations = []
    for conv in conversions:
        click_conversion = client.get_type("ClickConversion")
        click_conversion.gclid = conv['gclid']
        click_conversion.conversion_action = f"customers/{customer_id}/conversionActions/{conv['conversion_action_id']}"
        click_conversion.conversion_date_time = conv['conversion_time']
        click_conversion.conversion_value = conv['value']
        click_conversion.currency_code = conv['currency']

        operations.append(click_conversion)

    # Upload
    request = client.get_type("UploadClickConversionsRequest")
    request.customer_id = customer_id
    request.conversions = operations
    request.partial_failure = True

    response = conversion_upload_service.upload_click_conversions(request=request)

    print(f"Uploaded {len(response.results)} conversions")
    return response

# Example usage
conversions = [
    {
        'gclid': 'EAIaIQobChMI...',
        'conversion_action_id': '123456789',
        'conversion_time': '2025-01-28 14:30:00+01:00',
        'value': 50.00,
        'currency': 'EUR'
    }
]

upload_offline_conversions('123-456-7890', conversions)
```