# 🧮Queueing System In JavaScript

This project contains tasks for learning to create a queueing system in JavaScript using Redis.

## 🧮Tasks To Complete

+ [x] 0. **Install a Redis instance**
  + This task involves downloading, extracting, and compiling the latest stable Redis version (higher than 5.0.7) from the official website (https://redis.io/download). It provides step-by-step instructions for installing Redis on Linux and macOS systems.
  + After installing Redis, the task requires starting the Redis server in the background, ensuring it's working correctly, setting a key-value pair in the Redis database, and finally, killing the Redis server process.
  + The `dump.rdb` file from the Redis installation directory is copied to the project's root directory.
  + The requirement is that running `get Holberton` in the Redis client should return `School`.

+ [x] 1. **Node Redis Client**
  + This task involves installing the `node_redis` library using either yarn or npm.
  + A script named `0-redis_client.js` is created using Babel and ES6 syntax.
  + The script connects to the Redis server running on the local machine and logs a message to the console indicating whether the connection was successful or not.
  + The requirement is to use the `import` keyword to import the `node_redis` library.

+ [x] 2. **Node Redis client and basic operations**
  + In the file `1-redis_op.js`, the code from the previous task (`0-redis_client.js`) is copied.
  + Two functions are added:
    1. `setNewSchool`: Accepts two arguments (`schoolName` and `value`), sets the value for the given `schoolName` key in Redis, and displays a confirmation message.
    2. `displaySchoolValue`: Accepts one argument (`schoolName`), and logs the value associated with the given `schoolName` key to the console.
  + At the end of the file, the following functions are called:
    - `displaySchoolValue('Holberton')`
    - `setNewSchool('HolbertonSanFrancisco', '100')`
    - `displaySchoolValue('HolbertonSanFrancisco')`
  + The requirement is to use callbacks for any Redis operation.

+ [x] 3. **Node Redis client and async operations**
  + In the file `2-redis_op_async.js`, the code from the previous exercise (`1-redis_op.js`) is copied.
  + The `displaySchoolValue` function is modified to use ES6's `async/await` syntax with `promisify`.
  + The expected result is the same as `1-redis_op.js`.

+ [x] 4. **Node Redis client and advanced operations**
  + In the file `4-redis_advanced_op.js`, the Redis client is used to store a hash value.
  + A hash with the key `HolbertonSchools` is created using `hset`, and the following key-value pairs are stored:
    - `Portland=50`
    - `Seattle=80`
    - `New York=20`
    - `Bogota=20`
    - `Cali=40`
    - `Paris=2`
  + The `redis.print` function is used for each `hset` operation.
  + The stored hash object is displayed using `hgetall`, which should return the following output:
    ```
    Portland=50
    Seattle=80
    New York=20
    Bogota=20
    Cali=40
    Paris=2
    ```

The comments provide a clear explanation of each task, including the requirements, expected outputs, and any specific instructions or details to be followed. The code is well-structured and easy to understand, making it a valuable resource for learning about queueing systems in JavaScript using Redis.

##🧮 explanation for the tasks:

+ [x] 0. **Install a Redis instance**
  + Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. This task ensures that you have a Redis instance installed and running on your local machine, which is a prerequisite for the subsequent tasks.
  + The `dump.rdb` file is a Redis database snapshot that contains the initial data for the project. By copying this file to the project's root directory, you'll have a pre-populated Redis database to work with.

+ [x] 1. **Node Redis Client**
  + The `node_redis` library is a popular Node.js client for Redis that provides a convenient way to interact with Redis from within your Node.js applications.
  + This task sets up the basic connection to the Redis server using the `node_redis` client and logs the connection status to the console.
  + Establishing a connection to Redis is a fundamental step before performing any operations on the Redis database.

+ [x] 2. **Node Redis client and basic operations**
  + This task introduces two basic Redis operations: setting a key-value pair and retrieving the value associated with a key.
  + The `setNewSchool` function demonstrates how to store a value in Redis using the `SET` command, while the `displaySchoolValue` function retrieves the value associated with a given key using the `GET` command.
  + By calling these functions with different keys and values, you can practice storing and retrieving data from Redis using the `node_redis` client.
  + The use of callbacks in this task is a common pattern in Node.js for handling asynchronous operations, as Redis commands are non-blocking.

+ [x] 3. **Node Redis client and async operations**
  + This task builds upon the previous one by introducing the use of `async/await` syntax and the `promisify` utility from the Node.js `util` module.
  + `promisify` is a helper function that converts a function that uses a callback-based API to a function that returns a Promise.
  + By modifying the `displaySchoolValue` function to use `async/await` and `promisify`, you can write more concise and readable code for handling asynchronous Redis operations.
  + This task demonstrates how to leverage modern JavaScript features like `async/await` for working with Redis in a more synchronous-looking style.

+ [x] 4. **Node Redis client and advanced operations**
  + In this task, you'll work with Redis hashes, which are a data structure that allows you to store multiple key-value pairs under a single key.
  + The `hset` command is used to set multiple fields (key-value pairs) within a Redis hash, and the `hgetall` command retrieves all the fields and values associated with the hash.
  + By storing and retrieving data using Redis hashes, you can organize related data into a single data structure, which can be useful for various use cases like caching objects or storing user sessions.
  + This task also introduces the `redis.print` function, which is a convenient way to log messages or data to the console in a Redis context.

Overall, these tasks provide a solid foundation for working with Redis using the `node_redis` client in a Node.js environment. They cover essential concepts like connecting to Redis, performing basic operations (setting and retrieving values), working with different data structures (hashes), using callbacks and `async/await`, and handling advanced Redis operations.
