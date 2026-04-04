## Platform-Specific Implementations

```
PLATFORM DATA LAYER IMPLEMENTATIONS
=====================================

SHOPIFY
───────
Use Shopify's native Analytics integration + app:

Liquid template approach:
```liquid
<script>
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({
    'pageType': '{{ template.name }}',
    {% if customer %}
    'userLoggedIn': true,
    'userId': '{{ customer.id }}',
    {% endif %}
    {% if product %}
    'productId': '{{ product.id }}',
    'productName': '{{ product.title | escape }}',
    'productPrice': {{ product.price | money_without_currency | remove: ',' }}
    {% endif %}
  });
</script>
```


WORDPRESS / WOOCOMMERCE
────────────────────────
Plugins:
├── GTM4WP (Google Tag Manager for WordPress)
├── Pixel Manager for WooCommerce
└── Monster Insights

Or custom functions.php:
```php
add_action('wp_head', function() {
  global $post;
  echo "<script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      'pageType': '" . get_post_type() . "',
      'pageId': " . get_the_ID() . "
    });
  </script>";
}, 1);
```


MAGENTO
───────
Modules:
├── GTM Pro by Mageworx
├── Google Tag Manager by Amasty
└── Custom module development

Native events via Magento layout XML + knockout.js


NEXT.JS / REACT
────────────────

```javascript
// _app.js or layout component
import { useEffect } from 'react';
import { useRouter } from 'next/router';

function MyApp({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    const handleRouteChange = (url) => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'page_view',
        'page_path': url
      });
    };

    router.events.on('routeChangeComplete', handleRouteChange);
    return () => {
      router.events.off('routeChangeComplete', handleRouteChange);
    };
  }, [router.events]);

  return <Component {...pageProps} />;
}
```
```

## Data Layer Structure

### Page-Level Data (all pages)
```javascript
dataLayer.push({
  'pageType': '[home|category|product|cart|checkout|thank-you|blog|landing]',
  'pageCategory': '[category name]',
  'userLoggedIn': [true|false],
  'userId': '[hashed user id]',
  'userType': '[visitor|lead|customer]'
});
```

### E-commerce Events

#### view_item
- **Trigger:** Product page load
- **Required fields:** item_id, item_name, price, currency

#### add_to_cart
- **Trigger:** Add to cart button click
- **Required fields:** item_id, item_name, price, quantity, currency

#### begin_checkout
- **Trigger:** Checkout page load
- **Required fields:** items array, value, currency

#### purchase
- **Trigger:** Order confirmation page
- **Required fields:** transaction_id, value, currency, items array

### Custom Events

| Event Name | Trigger | Data Fields |
|------------|---------|-------------|
| form_submit | Form completion | form.name, form.location |
| cta_click | CTA button click | cta.text, cta.location |
| video_play | Video start | video.title, video.provider |