function get_json(){
    $.get('/todolist/json', function(data){
        var cardTask = ""
        for(var i = 0; i < data.length; i++){
          cardTask = `
          <div class="card">
            <div class="card-header">
              ${data.is_finished ? `Selesai` : `Belum Selesai`}
            </div>
            <div class="card-body">
              <h5 class="card-title">${data.title}</h5>
              <p class="card-text"><b>${data.date}</b></p>
              <p class="card-text">${data.description}</p>
              <a class="btn btn-primary" href="{% url 'todolist:update-task' task.id %}">Update</a>
              <a class="btn btn-primary" href="{% url 'todolist:delete-task' task.id %}">Hapus</a>
              <a class="btn btn-primary" href="{% url 'todolist:update-task' task.id %}">Update</a>
              <a class="btn btn-primary" href="{% url 'todolist:delete-task' task.id %}">Hapus</a>
            </div>
          </div>
          `
        }
        $('#card-task').append(cardTask);
    })
}

$(document).ready(function(){
  get_json()
});

