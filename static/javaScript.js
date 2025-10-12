// Seleciona todos os botões de edição
const editButtons = document.querySelectorAll(".edit-btn");
const editForm = document.querySelector(".edit_user_form");
const form = document.getElementById("editForm");

editButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const userId = btn.getAttribute("data-id");
    const userName = btn.getAttribute("data-name");
    const userEmail = btn.getAttribute("data-email");

    // Preenche o formulário
    document.getElementById("edit_id").value = userId;
    document.getElementById("edit_name").value = userName;
    document.getElementById("edit_email").value = userEmail;

    // Define a rota correta de atualização
    form.action = `/update/${userId}`;

    // Mostra o formulário
    editForm.style.display = "block";

    // Rola até o formulário para boa UX
    editForm.scrollIntoView({ behavior: "smooth" });
  });
});
