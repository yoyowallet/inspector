<script type="text/javascript">
  $(document).ready(function () {

    $(".{{ object }}-delete").each(function () {
      $(this).modalForm({
        formURL: $(this).data('url'),
        modalID: "#{{ object }}-modal"
      });
    });
  });
</script>
