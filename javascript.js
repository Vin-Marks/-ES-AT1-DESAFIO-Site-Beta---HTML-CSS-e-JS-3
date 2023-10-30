// JavaScript para interações na página de compras
function addToCart(productId, productName) {
    shoppingList.push({ id: productId, name: productName });
    updateList();
}

function deleteFromCart(index) {
    shoppingList.splice(index, 1);
    updateList();
}

function updateList() {
    var listElement = document.getElementById("shoppingList");
    listElement.innerHTML = "";
    shoppingList.forEach(function (item, index) {
        var listItem = document.createElement("li");
        listItem.appendChild(document.createTextNode(item.name));
        var deleteButton = document.createElement("button");
        deleteButton.appendChild(document.createTextNode("Excluir"));
        deleteButton.onclick = function () {
            deleteFromCart(index);
        };
        listItem.appendChild(deleteButton);
        listElement.appendChild(listItem);
    });
}

function confirmPurchase() {
    var confirmation = confirm("Deseja confirmar a compra?");
    if (confirmation) {
        alert("Compra confirmada! Obrigado por comprar conosco.");
    }
}

// Adicione mais funcionalidades conforme necessário
