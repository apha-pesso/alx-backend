// Import createCLient from redis
import redis from "redis";
import { createClient } from "redis";
import { promisify } from "util";

// Create a Redis client
const client = createClient();

// Promisify Redis client methods
const getAsync = promisify(client.get).bind(client);

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
async function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print);
  await getAsync(schoolName);
  // return new Promise((resolve, reject) => {
  //   client.get(schoolName, (err, value) => {
  //     if (err) reject(err);
  //     resolve(value);
  //   });
  // });
}

// Call functions

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

//displaySchoolValue("HolbertonSanFrancisco");

// Close the Redis connection
client.quit();
