function remove(id) {
    fetch(`/remove/${id}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })

        .catch(err => console.error(err));
}

// Seleciona botões de edição
document.addEventListener("DOMContentLoaded", function () {
  const editButtons = document.querySelectorAll(".edit-btn");
  const editContainer = document.getElementById("editContainer");
  const editForm = document.getElementById("editForm");

  editButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.id;
      const name = btn.dataset.name;
      const email = btn.dataset.email;

      // Preenche o formulário
      document.getElementById("edit_id").value = id;
      document.getElementById("edit_name").value = name;
      document.getElementById("edit_email").value = email;

      // Exibe o formulário
      editContainer.style.display = "block";
      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
      })
    });
  });

  // Envia atualização via fetch
  editForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(editForm);

    const response = await fetch("/update", {
      method: "POST",
      body: formData
    });

    if (response.ok) {
      alert("Usuário atualizado!");
      editContainer.style.display = "none"; // Esconde o formulário
      location.reload(); // Recarrega a lista
    } else {
      alert("Erro ao atualizar usuário.");
    }
  });
});
