const fetch = require('node-fetch');

  async function getCurrentTime() {
      const response = await fetch('http://worldtimeapi.org/api/ip');
      const data = await response.json();
      return data.datetime; // Returns the current time in ISO format
  }
