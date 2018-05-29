$("#refresh").click(function() {
    getStatus();
})

$("#lightOn").click(function() {
    $.get("/action/lighton", function(rst) {
        alert("开灯成功，当前灯光：" + rst.state);
        $("#lightStat").html(rst.state);
    });
})

$("#lightOff").click(function() {
    $.get("/action/lightoff", function(rst) {
        alert("关灯成功，当前灯光：" + rst.state);
        $("#lightStat").html(rst.state);
    });
})

$("#feed").click(function() {
    $.get("/action/feed", function(rst) {
        alert("投喂结果：" + rst.state);
    });
})

$(document).ready(function() {
    getStatus();
});

function getStatus() {
    $.get("/read/temp", function(rst) {
        $("#waterTemp").html(rst.temp);
        $("#waterStat").html(rst.state);
    });
    $.get("/read/light", function(rst) {
        $("#lightStat").html(rst.state);
    });
}