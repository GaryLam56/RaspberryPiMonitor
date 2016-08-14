function update() {
    $(document).ready(function () {
        $("#update-btn").click(function () {
            $.ajax({
                type: "GET",
                url: "/test/",
                dataType: "json",
                data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
                success: function (json) {
                    var x = ((json.mem_used / json.mem_total) * 100);
                    console.log(x);
                    $("#memory").attr({
                        "style": ("width:" + x + "%"),
                        "aria-valuemax": (json.mem_total),
                        "aria-valuenow": (json.mem_used)
                    });
                    $("#pi-uptime").html(json.up_day + "d" + json.up_hour + "h" + json.up_minute + "m");
                    $("#buffer-percentage").html(json.mem_buffer + "MB");
                    $("#cache-percentage").html(json.mem_cache + "MB");
                    $("#used-percentage-bar").html(((json.mem_used/json.mem_total) * 100) + "%");
                    $("#used-percentage").html(json.mem_used + "MB");
                    $("#free-percentage").html(json.mem_avail + "MB");
                    $("#cpu-temperature").html(json.temp + "°C");
                    $("#processor0").html(json.cpu0 + "%");
                    $("#processor1").html(json.cpu1 + "%");
                    $("#processor2").html(json.cpu2 + "%");
                    $("#processor3").html(json.cpu3 + "%");
                },
                error: function () {
                    alert("error!");
                }
            });
        });
    });
}