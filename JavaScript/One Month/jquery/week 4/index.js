$(document).ready(function () {
    $.ajax({
        url: "https://api.jsonbin.io/b/5e99f36b5fa47104cea282ff/4",
        dataType: "json",
        success: function (response) {
            $.each(response.apartments, function (index, apartment) {
                var listing = '<a href = "#" class = "list-group-item"><h4 class="list-group-item-heading">' + apartment.description + ' / ' + apartment.bedrooms + ' / ' + apartment.price + '</h4><p class="list-group-item-text">' + apartment.neighborhood + '</p></a>';
                $(".apartments").append(listing);
            })
        },
        error: function (error) {
            console.log(error);
        }
    });
});