import http from 'k6/http';
import { check } from 'k6';

let users = JSON.parse(open('./user.json', 'utf-8'));

// Function to generate random user IDs in the format 'u00000'
function generateRandomUserID() {
  let randomNum = Math.floor(Math.random() * 99999); // Generate a random number between 0 and 99999
  let paddedNum = randomNum.toString().padStart(5, '0'); // Pad the number with leading zeros
  return `u${paddedNum}`;
}

export let options = {
  vus: 5,
  stages: [
    { duration: '10s', target: 5 }, // Ramp-up to reach the maximum request rate
  ],
  thresholds: {
    http_req_duration: ['p(90)<100']
  },
};

export default function () {  
  let generatedUserID = generateRandomUserID();

  // Measure GET request
  let getResponse = http.get(`http://knn_model:5005/recommend/${generatedUserID}`);

  check(getResponse, {
    'GET status is 200': (r) => r.status === 200,
  });
}