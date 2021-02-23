var str = new String("Demo Text");
         document.write(str.strike());
         alert(str.strike());


var container = document.getElementById("container");
if (container.addEventListener) {
    container.addEventListener('click', clickHandler, false);
}
else if (container.attachEvent) {
    container.attachEvent('onclick', function(e) {
        return clickHandler.call(container, e || window.event);
    });
}

function clickHandler(event) {
    var span = event.target;
    // Do something with the span, such as look at its `innerHTML` and
    // see if it's "0" -- if so, make it "1"; if not, make it "0"
}