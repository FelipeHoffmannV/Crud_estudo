function remove(id) {
    fetch(`/remove/${id}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })

        .catch(err => console.error(err));
}