$(document).ready(function() {
    $('#chatForm').on('submit', function(event) {
        event.preventDefault();
        var query = $('#query').val();
        $.ajax({
            url: '/chat',
            type: 'POST',
            data: { query: query },
            success: function(response) {
                $('#response').html('<pre>' + JSON.stringify(response, null, 2) + '</pre>');
            }
        });
    });
});
