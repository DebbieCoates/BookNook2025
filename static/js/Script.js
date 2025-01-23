
    $(document).ready(function () {
        toastr.options = {
            "positionClass": "toast-top-custom",
            "timeOut": "2000", // 2 seconds
        };

        {% if messages %}
            {% for message in messages %}
                toastr["{{ message.tags }}"]("{{ message }}");
            {% endfor %}
        {% endif %}
    });
