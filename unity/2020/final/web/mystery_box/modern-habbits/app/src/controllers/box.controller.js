const { boxServices } = require("../services");

const addMisteryBox = async (req, res) => {
    const datas = await boxServices.create(req.body);
    res.send({ datas });
};

const showMisteryBox = async (req, res) => {
    const datas = await boxServices.fetch(req.body);
    res.send({ datas });
};

module.exports = {
    addMisteryBox,
    showMisteryBox,
};
