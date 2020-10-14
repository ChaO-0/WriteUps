const mongoose = require("mongoose");

const BoxSchema = mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
        },
        content: {
            type: String,
            requried: true,
        },
        secret: {
            type: String,
            required: true,
        },
    },
    { timestamps: true },
);

module.exports = mongoose.model("Box", BoxSchema);
