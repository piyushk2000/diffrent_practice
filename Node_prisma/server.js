
import express from 'express';
import dotenv from 'dotenv';
import { notFound, errorHandler } from './middleware/errorMiddleware.js';

dotenv.config();


const port = process.env.PORT || 5000;

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use(notFound);
app.use(errorHandler);

app.get('/', (req, res) => {
    res.send('API is running....');
});

app.listen(port, () => console.log(`Server started on  http://localhost:${port}`));
