require("dotenv").config();
const seeder = require("mongoose-seed");

const lengthFlag = 39; // mod 13 == 0
const secret = Array.from(Array(lengthFlag / 13).keys())
    .map(() => Math.random().toString(16).substring(2))
    .join("");

seeder.connect(process.env.DB_CONNECTION, { useNewUrlParser: true, useUnifiedTopology: true }, () => {
    seeder.loadModels(["src/models/Box.model.js"]);
    seeder.clearModels(["Box"], () => {
        seeder.populateModels(
            [
                {
                    model: "Box",
                    documents: [
                        {
                            name: "flag",
                            content: `FLAG{${secret}}`,
                            secret: secret,
                        },
                    ],
                },
            ],
            () => seeder.disconnect(),
        );
    });
});
