<script type="text/javascript">
    $(document).ready(function () {

        $(".{{ object }}-run").each(function () {
            $(this).modalForm({
                formURL: $(this).data('url'),
                modalID: "#{{ object }}-modal"
            });
        });
    });
</script>
