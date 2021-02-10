$(document).ready(function () {
    $("#list-items").html(localStorage.getItem("key"));

    $(".add-items").submit(function (event) {
        event.preventDefault();
        var item = $("#todo-list-item").val();
        if (item.trim() != "") {
            console.log($(this));
            $("#list-items").fadeIn("default", function () {
                $(this).append("<li class='listItem'><input type='checkbox' class='checkbox'>" + item + "<a class='remove'>x</a><hr></li>")
                localStorage.setItem("key", $("#list-items").html());
                $("#todo-list-item").val("");
            });

        }
    });
    //static way
    // $(".checkbox").change(function() {
    // console.log("Checkbox checked!");
    // })


    //dynamic way
    $(document).on("change", ".checkbox", function () {
        if ($(this).attr("checked")) {
            $(this).removeAttr("checked");
        } else {
            $(this).attr("checked", "checked");
        }

        $(this).parent().toggleClass("completed");
        localStorage.setItem("key", $("#list-items").html());

    });

    $(document).on("click", ".remove", function () {
        //console.log($(this).parent())
        $(this).parent().fadeOut("slow", function () {
            $(this).remove();
            localStorage.setItem("key", $("#list-items").html());
        });
    });
});