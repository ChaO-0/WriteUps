const { Box } = require("../models");

const create = async (body) => {
    const { name, content, secret } = body;
    const boxs = await Box.findOne({
        name: name,
    });

    if (boxs) {
        return {
            error: "Box name not available !!",
        };
    }

    return await Box.create({
        name: name,
        content: content,
        secret: secret,
    });
};

const fetch = async (body) => {
    const { name, secret } = body;
    const boxs = await Box.aggregate([
        {
            $match: {
                name: {
                    $regex: `^[${name}]{4}`,
                    $options: "gm",
                },
            },
        },
    ]);

    if (!boxs) {
        return {
            error: "Box name not found !!",
        };
    }

    for (box of boxs) {
        if (box.secret == secret) {
            return boxs.shift();
        }
    }
};

module.exports = {
    create,
    fetch,
};
