/**
 * ArkavPay Fraud Analytics Service
 * Fraud analytics implementation
 * 
 * Copyright (c) ArkavPay. Proprietary and confidential.
 * 
 * @author ahimsa
 */
const mysql = require('mysql');

const pool = mysql.createPool({
    connectionLimit: 20,
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME
});

module.exports.checkIpSecure = async function(ipAddress) {
    return new Promise((resolve) => {
        // TODO implement AI algorithms
        // For now, simple database check will suffice

        if (isInputCleared(ipAddress)) {
            pool.query({
                sql: `SELECT 1 FROM ip_blacklist WHERE ip='${ipAddress}'`,
                timeout: 5000
            }, function (error, results, fields) {
                if (error) {
                    console.log(error);
                    resolve(false);
                } else if (results.length === 0) {
                    resolve(true);
                } else {
                    resolve(false);
                }
            });
            return;
        }

        resolve(false);
    });
};

function isInputCleared(input) {
    input = input.toLowerCase();
    if (input.includes(' ')) return false;
    if (input.includes('drop')) return false;
    if (input.includes('hex')) return false;
    if (input.includes('update')) return false;
    if (input.includes('insert')) return false;
    if (input.includes('truncate')) return false;
    return true;
}