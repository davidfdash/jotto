var str = new String("Demo Text");
         document.write(str.strike());
         alert(str.strike());


<div id="container">
    <span>0</span><span>0</span><span>0</span><span>0</span> <span>0</span><span>0</span><span>0</span><span>0</span> <span>0</span><span>0</span><span>0</span><span>0</span>
</div>

var container = document.getElementById("container");
if (container.addEventListener) {
    container.addEventListener('click', clickHandler, false);
}
else if (container.attachEvent) {
    container.attachEvent('onclick', function(e) {
        return clickHandler.call(container, e || window.event);
    });
}