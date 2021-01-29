window.onload = function () {
    console.log('DOM loaded');
    $('.blog-pagination').on('click', '.btn btn-outline-primary', function (event) {
    //$('.blog-pagination').on('change', 'input[type=number]', function (event) {
        console.log(event.target);
        //$.ajax({
            //url: '/basket/change/' + event.target.name + '/quantity/' + event.target.value + '/',
            //success: function (data) {
                //console.log(data)
                //$('.basket').html(data.result);
            //}
        //});
    })
};