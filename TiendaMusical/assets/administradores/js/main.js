

function setTodayDate() {
    var today = new Date();
    var year = today.getFullYear();
    var month = ('0' + (today.getMonth() + 1)).slice(-2);
    var day = ('0' + today.getDate()).slice(-2);
    var formattedDate = year + '-' + month + '-' + day;
    document.getElementById('id_annopublicacion').value = formattedDate;
}


var form = document.getElementById('disco_form');
form.addEventListener('submit', function(event) {
  var fields = [
    { inputId: 'id_nombre', errorId: 'nombreError', maxLength: 50, errorMessage: 'El nombre debe tener máximo 50 caracteres.' },
    { inputId: 'id_nombreAlbum', errorId: 'albumError', maxLength: 50, errorMessage: 'El nombre del album debe tener máximo 50 caracteres.' },
    { inputId: 'id_artista', errorId: 'artistaError', maxLength: 50, errorMessage: 'El nombre del artista debe tener máximo 50 caracteres.' },
    { inputId: 'id_precio', errorId: 'precioError', maxLength: 10, errorMessage: 'Ingrese un número válido para el precio.', numeric: true },
    { inputId: 'id_vendidos', errorId: 'vendidosError', maxLength: 10, errorMessage: 'Ingrese un número válido para los vendidos.', numeric: true },
    { inputId: 'id_stock', errorId: 'stockError', maxLength: 10, errorMessage: 'Ingrese un número válido para el stock.', numeric: true }
  ];

  var formIsValid = true;

  fields.forEach(function(field) {
    var input = document.getElementById(field.inputId);
    var error = document.getElementById(field.errorId);

    if (field.maxLength && input.value.length > field.maxLength) {
      input.setCustomValidity(field.errorMessage);
      error.textContent = field.errorMessage;
      formIsValid = false;
    } else if (field.numeric && isNaN(input.value)) {
      input.setCustomValidity(field.errorMessage);
      error.textContent = field.errorMessage;
      formIsValid = false;
    } else {
      input.setCustomValidity('');
      error.textContent = '';
    }
  });

  var inputFormato = document.getElementById('id_formatos');
  var formatoError = document.getElementById('formatoError');

  if (inputFormato.value === "0") {
    inputFormato.setCustomValidity('Elige un tipo de formato.');
    formatoError.textContent = 'Elige un tipo de formato.';
    formIsValid = false;
  } else {
    inputFormato.setCustomValidity('');
    formatoError.textContent = '';
  }

  if (!formIsValid) {
    event.preventDefault();
  }
});
    