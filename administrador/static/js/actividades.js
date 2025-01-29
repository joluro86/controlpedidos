// Confirmación para eliminar actividad contrato
function eliminarActividad(element) {
    let actividadId = element.getAttribute("data-id");    
    let url = `/administrador/eliminar-actividad/${actividadId}/`;
    console.log(url)
    swal
      .fire({
        title: "¿Desea eliminar esta actividad? Esta acción no es revertible",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        cancelButtonText: "Cancelar",
        confirmButtonText: "¡Sí, continuar!",
      })
      .then(function (result) {
        if (result.value) {
          Swal.fire({
            title: 'Procesando...',
            html: 'Por favor, espere...',
            allowEscapeKey: false,
            allowOutsideClick: false,
            didOpen: () => {
              Swal.showLoading();
            }
          });
          window.location.href = url;
        }
      });
  }

  // Confirmación para eliminar actividad epm
function eliminarActividadEpm(element) {
  let actividadId = element.getAttribute("data-id");    
  let url = `/administrador/eliminar-actividad-epm/${actividadId}/`;
  console.log(url)
  swal
    .fire({
      title: "¿Desea eliminar esta actividad Epm? Esta acción no es revertible",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Sí, continuar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Procesando...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        });
        window.location.href = url;
      }
    });
}
  

// Confirmación para eliminar encargado
function eliminarEncargado(element) {
  let encargadoId = element.getAttribute("data-id");    
  let url = `/administrador/eliminar-encargado/${encargadoId}/`;
  console.log(url)
  swal
    .fire({
      title: "¿Desea eliminar esta encargado? Esta acción no es revertible",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Sí, continuar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Procesando...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        });
        window.location.href = url;
      }
    });
}


// Confirmación para eliminar material contrato
function eliminarMaterialContrato(element) {
  let materialId = element.getAttribute("data-id");    
  let url = `/administrador/eliminar-material-contrato/${materialId}/`;
  console.log(element.getAttribute("idd"))
  swal
    .fire({
      title: "¿Desea eliminar esta material? Esta acción no es revertible",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Sí, continuar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Procesando...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        });
        window.location.href = url;
      }
    });
}