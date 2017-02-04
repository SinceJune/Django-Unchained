var moment = require("moment");

window.timer = function () {
    moment().local();
    return moment().format('l');
}