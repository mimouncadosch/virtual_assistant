function play(url) {
    console.log('calling play with url', url);
    $("#jquery_jplayer_1").jPlayer({
        ready: function () {           
            $(this).jPlayer("setMedia", {
                title: "File",
                // mp3: url
                m4a: url
            }).jPlayer("play");
        },
        ended: function() {
            $("#jquery_jplayer_1").jPlayer("destroy");
        },
        cssSelectorAncestor: "#jp_container_1",
        swfPath: "/js",
        supplied: "m4a, oga",
        useStateClassSkin: true,
        autoBlur: false,
        smoothPlayBar: true,
        keyEnabled: true,
        remainingDuration: true,
        toggleDuration: true
    });
}

$(document).ready(function() {
    $(".file_id").click(function(i) {
        var file_id = $(this).attr('file_id');
        var url = '/uploads/' + file_id;
        play(url);
    });
});

$(document).ready(function() {
    $(".markread").click(function () {
        var file_id = $(this).attr('file_id');
        var url = $(this).attr('url');
        var full_url = url + 'markread/' + file_id;
        data = {read : true}
         $.ajax({
            type : "POST",
            url : full_url,
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                console.log(result);
            }
        });
    });
});

$(document).ready(function() {
    $(".markunread").click(function () {
        var file_id = $(this).attr('file_id');
        var url = $(this).attr('url');
        var full_url = url + 'markunread/' + file_id;
        data = {read : true}
         $.ajax({
            type : "POST",
            url : full_url,
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                console.log(result);
            }
        });
    });
});