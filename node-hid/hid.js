var HID = require('node-hid');

var device = new HID.HID(2131,256); // HHKB Professional. 管理者権限で実行
// var device = new HID.HID(1149,8257); // Kensington Slimblade Trackball

setTimeout(function() {
  console.log('5sec has passed. hid device is closed.')
  device.close();
}, 5000);


device.on("data", function(data) {
  console.log(data);
});

device.on("error", function(data) {
  console.log(data);
});
