/**
 * Mobile App Backend - Matar's Iced Americano
 * Powering the mobile experience (Beta)
 */

const fastify = require('fastify')({ logger: true });

fastify.get('/health', async () => {
  return { status: 'healthy', service: 'mobile-app-backend', version: '0.9.0-beta' };
});

fastify.get('/api/v1/stores', async () => {
  return {
    stores: [
      { id: 'store-1', name: 'Downtown', address: '123 Main St', distance: '0.3 mi' },
      { id: 'store-2', name: 'Midtown', address: '456 Oak Ave', distance: '0.8 mi' },
      { id: 'store-3', name: 'Airport', address: 'Terminal B', distance: '5.2 mi' },
    ]
  };
});

fastify.post('/api/v1/orders/ahead', async (request) => {
  return {
    message: 'Order placed for pickup',
    order_id: 'ORD-MOBILE-001',
    pickup_time: '10 minutes',
    store: 'Downtown'
  };
});

fastify.get('/api/v1/user/rewards', async () => {
  return {
    points: 342,
    tier: 'Silver',
    next_reward: 'Free Iced Americano at 400 points'
  };
});

const start = async () => {
  try {
    await fastify.listen({ port: 8080, host: '0.0.0.0' });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
