import express from "express";
import { Sequelize } from "sequelize";

const port = 5000

const app = express()
app.use(express.json())

export const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'path/to/database.sqlite'
  });

try {
    await sequelize.authenticate();
    console.log('Connection has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }

app.get('/', (req, res) => {
    res.send('Hello World!')
  })


app.post('/square', (req, res)=>{
    const number = req.query.number
    const number2 =  req.body.number

    const result2 = number2*number2
    const result = number*number
    console.log("🚀 ~ app.get ~ result:", result)

    res.json({squ : result, sq2: result2 })
})

app.listen(port , ()=> console.log(`server started on port http://localhost:${port}`))