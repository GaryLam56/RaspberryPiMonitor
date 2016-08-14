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
                    $("#pi-uptime").html(x + "%");
                    $("#buffer-percentage").html(json.mem_buffer/json.mem_total + "%");
                    $("#cache-percentage").html(json.mem_cache/json.mem_total + "%");
                    $("#used-percentage").html(json.mem_used/json.mem_total + "%");
                    $("#free-percentage").html((json.mem_total - json.mem_buffer + json.mem_cache - json.mem_used)/json.mem_total + "%");
                    $("#cpu-temperature").html(json.temp + "°C");
                    $("#processor0").html(json.cpu0);
                    $("#processor1").html(json.cpu1);
                    $("#processor2").html(json.cpu2);
                    $("#processor3").html(json.cpu3);
                },
                error: function () {
                    alert("error!");
                }
            });
        });
    });
}