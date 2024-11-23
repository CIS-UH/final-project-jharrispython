const express = require('express');
const app = express();
const axios = require('axios');
const path = require('path');


console.log('Views directory:', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.get('/', (req, res) => {
    res.render('index', { message: 'Welcome to the Stock Brokerage System' });
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Frontend server running on port ${PORT}`);
});

app.get('/investors', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/investor');
        const investors = response.data;
        res.render('investors', { investors });
    } catch (error) {
        res.status(500).send('Error fetching investors');
    }
});
