// Import createCLient from redis
import redis from "redis";
import { createClient } from "redis";

// Create a Redis client
const client = createClient();

// Output on success
client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// Output for error
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// SetSchool function
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// DisplaySchool function
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) console.log(err);
    console.log(value);
  });
}

// Call functions
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

// Close the Redis connection
client.quit();
