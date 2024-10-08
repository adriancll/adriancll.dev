const express = require('express');
const app = express();
const port = 3000;

const adjectives = [
    'sweet', 'adorable', 'lovely', 'charming', 'cute', 
    'playful', 'friendly', 'gentle', 'loyal', 'affectionate', 
    'happy', 'energetic', 'cuddly', 'cheerful', 'brave', 
    'curious', 'intelligent', 'obedient', 'protective', 'faithful',
    'graceful', 'jovial', 'merry', 'spirited', 'vivacious',
    'radiant', 'delightful', 'endearing', 'heartwarming', 'joyful',
    'magnificent', 'majestic', 'noble', 'splendid', 'stunning',
    'vibrant', 'whimsical', 'witty', 'zesty', 'zealous'
];

app.get('/dog', (req, res) => {
    const randomAdjective = adjectives[Math.floor(Math.random() * adjectives.length)];
    res.json({ adjective: randomAdjective });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
