function update() {
    $(document).ready(function () {
        $("#btn").click(function () {
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
                    $( "#memory" ).prepend(x + "%");
                },
                error: function () {
                    alert("error!");
                }
            });
        });
    });
}