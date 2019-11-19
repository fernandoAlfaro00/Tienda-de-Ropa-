$("#id_region").change(function() {
  var url = $("#personForm").attr("data-comunas-url");
  var regionId = $(this).val();
  $.ajax({
    url: url,
    data: {
      region: regionId
    },
    success: function(data) {
      $("#id_comuna").html(data);
    }
  });
});
