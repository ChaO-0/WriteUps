const express = require("express");
const validate = require("express-joi-validation").createValidator({
    passError: true,
});
const helmet = require("helmet");

const { boxControllers } = require("./controllers");
const { boxValidations } = require("./validations");

const app = express();

app.use(helmet());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(__dirname + "/assets"));
app.set("view engine", "pug");
app.set("views", __dirname + "/views");

app.post("/add", validate.body(boxValidations.create), boxControllers.addMisteryBox);
app.post("/show", validate.body(boxValidations.show), boxControllers.showMisteryBox);

app.get("/", (_, res) => {
    res.render("main");
});

app.use((err, _, res, next) => {
    if (err && err.error && err.error.isJoi) {
        res.status(400).json({
            type: err.type,
            message: err.error.toString(),
        });
    } else next(err);
});

module.exports = {
    app,
};
