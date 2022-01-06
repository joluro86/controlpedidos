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
        fecha_cierre(url);
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
    id_url.classList.add("bg-primary", "text-light");

    bgpendi = document.getElementById("pendi_index");
    bgpendi.classList.add("bg-primary");
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

function cierre_masivo() {
  Swal.fire({
    title: "Ingrese fecha y hora de cierre",
    html: `<input type="date" id="fecha_cierre" class="form-control input swal2-input" placeholder="Fecha de cierre">
    <input type="time" id="hora_cierre" class="form-control input swal2-input" placeholder="Hora de cierre">`,
    confirmButtonText: "Guardar",
    focusConfirm: false,
    preConfirm: () => {
      const fecha = Swal.getPopup().querySelector("#fecha_cierre").value;
      const hora = Swal.getPopup().querySelector("#hora_cierre").value;
      if (!fecha || !hora) {
        Swal.showValidationMessage(`Por favor ingrese fecha y hora`);
      }
      return { fecha: fecha, hora: hora };
    },
  }).then((result) => {
    if (result.value) {
      window.location.href =
        "/cierre_masivo/" + result.value.fecha + "/" + result.value.hora;
    }
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


