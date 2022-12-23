function cerrar_pedido(id) {
  url = "/cerrar/" + id;
  swal
    .fire({
      title: "¿Esta seguro de cerrar el pedido?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, cerrar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url 
      }
    });
}

function fecha_cierre(url) {
  Swal.fire({
    title: "Ingrese fecha y hora",
    html: `<input type="date" id="fecha" class="form-control input swal2-input" placeholder="Fecha de cierre">
    <input type="time" id="hora" class="form-control input swal2-input" placeholder="Hora de cierre">`,
    confirmButtonText: "Sign in",
    focusConfirm: false,
    preConfirm: () => {
      const fecha = Swal.getPopup().querySelector("#fecha").value;
      const hora = Swal.getPopup().querySelector("#hora").value;
      if (!fecha || !hora) {
        Swal.showValidationMessage(`Por favor ingrese fecha y hora`);
      }
      return { fecha: fecha, hora: hora };
    },
  }).then((result) => {
    if (result.value) {
      window.location.href =
        url + "/" + result.value.fecha + "/" + result.value.hora;
    }
  });
}

document.addEventListener(
  "DOMContentLoaded",
  function () {
    pintar_dia_semana();
  },
  false
);

function pintar_dia_semana() {
  id_dia = document.getElementById("id-oculto").value;

  if (id_dia > 0 || id_dia <= 50) {
    id_url = document.getElementById("id_url_" + id_dia);
    id_url.classList.add("bg-secondary", "text-light");

    bgpendi = document.getElementById("pendi_index");
    bgpendi.classList.add("bg-secondary");
    a = document.getElementById("pendi_a");
    a.classList.add("text-light");
  }
}

function otros_pedidos() {
  Swal.fire({
    title: "Elija los estados a buscar",
    html: `<div class="form-check">
                <input class="form-check-input" type="checkbox" value="1" id="cliente">
                <label class="form-check-label" for="cliente">Cliente</label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="2" id="apla">
                <label class="form-check-label" for="apla">Aplazados</label>
            </div>
            <div class="form-check">
            <input class="form-check-input" type="checkbox" value="3" id="pendi">
            <label class="form-check-label" for="pendi">Pendi</label>
          </div>`,
    confirmButtonText: "Buscar",
    focusConfirm: false,
    preConfirm: () => {
      cliente = document.getElementById("cliente");
      apla = document.getElementById("apla");
      pendi = document.getElementById("pendi");
      if (!cliente.checked && !apla.checked && !pendi.checked) {
        Swal.showValidationMessage(`Por favor elija al menos un campo`);
      } else {
        if (cliente.checked && !apla.checked && !pendi.checked) {
          apla = 0;
          pendi = 0;
          window.location.href =
            "/otros/" + cliente.value + "/" + apla + "/" + pendi;
        }
        if (!cliente.checked && apla.checked && !pendi.checked) {
          cli = 0;
          pendi = 0;
          window.location.href =
            "/otros/" + cli + "/" + apla.value + "/" + pendi;
        }
        if (!cliente.checked && !apla.checked && pendi.checked) {
          cli = 0;
          apla = 0;
          window.location.href =
            "/otros/" + cli + "/" + apla + "/" + pendi.value;
        }
        if (cliente.checked && apla.checked && !pendi.checked) {
          pendi = 0;
          window.location.href =
            "/otros/" + cliente.value + "/" + apla.value + "/" + pendi;
        }
        if (!cliente.checked && apla.checked && pendi.checked) {
          cli = 0;
          window.location.href =
            "/otros/" + cli + "/" + apla.value + "/" + pendi.value;
        }
        if (cliente.checked && !apla.checked && pendi.checked) {
          apla = 0;
          window.location.href =
            "/otros/" + cliente.value + "/" + apla + "/" + pendi.value;
        }
        if (cliente.checked && apla.checked && pendi.checked) {
          window.location.href =
            "/otros/" + cliente.value + "/" + apla.value + "/" + pendi.value;
        }
      }
    },
  });
}



function gestion_bd() {
  url = "/limpiar/";
  swal
    .fire({
      title: "¿Esta seguro de Gestionar la base de datos?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, gestionar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

function reiniciar_bd() {
  url = "/eliminar/";
  swal
    .fire({
      title: "¿Esta seguro de eliminar la información de la base de datos?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, eliminar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

function fechas_busqueda_epm() {
  swal
    .fire({
      title: "Fechas a buscar",
      type: "warning",
      html: '<div style="width:350px;margin:auto;"><label>Inicio</label><br><input id="inicio" type="date" class="form-control"><label>Final</label><br><input id="final" type="date" class="form-control"></div>',
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "Buscar",
      focusConfirm: false,
      preConfirm: () => {
        const inicio = Swal.getPopup().querySelector("#inicio").value;
        const final = Swal.getPopup().querySelector("#final").value;
        if (!inicio || !final) {
          Swal.showValidationMessage(`Por favor seleccione fechas a buscar`);
        }
        return { inicio: inicio, final: final };
      },
    })
    .then(function (result) {
      if (result.value) {
        inicio=result.value.inicio
        final=result.value.final
        window.location.href = "/epm/"+inicio+"/"+final+"/";
        
        alert(i) 
      }
    });
}

function descartar(id) {
  url = "/descartar/";
  swal
    .fire({
      title: "¿Esta seguro de descartar la base de datos?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, descartar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url+id+"/";
      }
    });
}

function gestion_fenix() {
  url = "/comparativo/calculo_novedades_perseo_vs_fenix/";
  swal
    .fire({
      title: "¿Esta seguro de realizar esta gestión?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, realizar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

function reiniciar_bd_perseo_vs_fenix() {
  url = "/comparativo/reiniciar/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar las extracciones?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

function reiniciar_novedades_bd_perseo_vs_fenix() {
  url = "/comparativo/reiniciar-novedades-perseo-fenix/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar las novedades?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

function analisis_fechas_perseo() {
  url = "/limpiar/";
  swal
    .fire({
      title: "¿Esta seguro de Gestionar la base de datos?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, gestionar!",
    })
    .then(function (result) {
      if (result.value) {
        window.location.href = url;
      }
    });
}

// CODIGO MENU BONIFICACIONES

function gestionar_bd_bonificacion() {
  url = "/ped-bonficiaciones/gestion_fenix/";
  swal
    .fire({
      title: "¿Esta seguro de gestionar la BBDD?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, gestionar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Gestionando la base de datos...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        })
        window.location.href = url;
      }
    });
}

function reiniciar_bd_bonificacion() {
  url = "/ped-bonficiaciones/reiniciar_actas_bonificaciones/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar la BBDD?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Reiniciando la base de datos...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        })
        window.location.href = url;
      }
    });
}

function reiniciar_bonificaciones() {
  url = "/ped-bonficiaciones/reiniciar_bonificaciones/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar el dato de las bonificaciones?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Reiniciando...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        })
        window.location.href = url;
      }
    });
}

function calculo_novedades() {
  url = "/analisis/calculo_novedades/";
  swal
    .fire({
      title: "¿Esta seguro de Analizar la base de datos del Acta?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, gestionar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Calculando novedades...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading()
          }
        });
        window.location.href = url;
      }
    });
}

function limpiar_novedades_acta() {
  url = "/analisis/limpiar_novedades/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar las novedades del Acta?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Limpiando novedades...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        })
        window.location.href = url;
      }
    });
}

function limpiar_acta_analisis() {
  url = "/analisis/limpiar_acta/";
  swal
    .fire({
      title: "¿Esta seguro de reiniciar la bases de datos del Acta?",
      type: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      cancelButtonText: "Cancelar",
      confirmButtonText: "¡Si, reiniciar!",
    })
    .then(function (result) {
      if (result.value) {
        Swal.fire({
          title: 'Reiniciando...',
          html: 'Por favor, espere...',
          allowEscapeKey: false,
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading()
          }
        });
        window.location.href = url;
      }
    });
}

// consulta con ajax
$('#search-button').click(function () {
  console.log("llegue a js")
  $.ajax({
    url: '/nuevo_analisis/busqueda-pedidos-acta-analisis/',  // URL de la vista de Django
    type: 'POST',
    data: {
      'nombre': 'jorge'
    },
    success: function (response) {  // función a ejecutar si la solicitud es exitosa
      console.log(response);  // imprime la respuesta del servidor en la consola
    }
  });
});
// fin consulta con ajax