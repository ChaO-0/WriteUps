const Joi = require("@hapi/joi");

const create = Joi.object({
    name: Joi.string().required(),
    content: Joi.string().required(),
    secret: Joi.string().required(),
});

const show = Joi.object({
    name: Joi.string().required(),
    secret: Joi.string().required(),
});

module.exports = {
    create,
    show,
};
