var page = require('webpage').create();
page.open('https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=phantom+open', function() {
  page.render('baidu.png');
  phantom.exit();
});


// var webPage = require('webpage');
// var page = webPage.create();
// var postBody = 'user=username&password=password';
//
// page.open('https://mail.163.com/', 'POST', postBody, function(status) {
//
//   console.log('Status: ' + status);
//   page.render('baidu.png');
//   phantom.exit();
// });
