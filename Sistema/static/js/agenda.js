


document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
    events: '/all_events',
    selectable: true,
    timeZone: moment.tz('America/Argentina/Buenos_Aires'),
      customButtons: {
        adicionarEvento: {
          text: 'Adicionar Evento',
          click: function() {
            alert('clicked the custom button!');
          }
        }
      },
        headerToolbar: {
          left: 'prev,next',
          center: 'title',
          right: 'today adicionarEvento',
        },
        buttonText: {
          today:'Hoje',
          month:'Mês',
          week:'Semana',
          day:'Dia',
          list:'Lista'
        },
        locale: 'pt-br',
        initialView: 'dayGridMonth',

      });
    calendar.render();
   } 
  );

  