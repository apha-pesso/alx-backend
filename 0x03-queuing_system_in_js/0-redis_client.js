// Import createCLient from redis
import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Output on success
client.on('connect', () => {
	console.log('Redis client connected to the server');
});

// Output for error
client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err}`);
});


// Close the Redis connection
client.quit();

