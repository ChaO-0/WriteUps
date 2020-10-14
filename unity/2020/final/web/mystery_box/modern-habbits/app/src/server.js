require("dotenv").config();

const mongoose = require("mongoose");
const { app } = require("./app");

mongoose.connect(
    process.env.DB_CONNECTION,
    {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    },
    () => app.listen(process.env.PORT),
);
