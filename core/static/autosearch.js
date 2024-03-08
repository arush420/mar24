function search() {
    // Declare variables
    var input, filter, table, tr, td, i, textValue;
    input = document.getElementById("myInput");

    /* To search case-insensitive */
    filter = input.value.toUpperCase();

    table = document.getElementById("myTable");

    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those that don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1]; // Assuming you want to search the first column
        if (td) {
            textValue = td.textContent || td.innerText;

            if (textValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function confirmDelete(event) {
    // Prompt for password
    var password = prompt("Please enter the password:");

    // You can replace 'YOUR_PASSWORD' with the actual password you want to check against
    if (password !== '1234') {
      alert("Incorrect password!");
      event.preventDefault(); // Prevent the default action (deleting)
    }
  }

  function enlargeImage(url) {
    var overlay = document.getElementById('overlay');
    var overlayImg = document.getElementById('overlay-img');
    overlay.style.display = 'flex';
    overlayImg.src = url;
  }

  function hideOverlay() {
    var overlay = document.getElementById('overlay');
    overlay.style.display = 'none';
  }


function moveToApproved(row) {
    const feature = row.cells[0].textContent;
    const dogViewUrl = row.cells[1].querySelector('img').src;
    const billViewUrl = row.cells[2].querySelector('img').src;

    // Create a new row for the approved table
    const newRow = approvedTable.insertRow();

    // Insert cells for feature, dog view, and bill view
    newRow.insertCell(0).textContent = feature;

    const dogViewCell = newRow.insertCell(1);
    const dogViewImage = document.createElement('img');
    dogViewImage.src = dogViewUrl;
    dogViewImage.alt = 'Dog View';
    dogViewImage.width = 75;
    dogViewCell.appendChild(dogViewImage);

    const billViewCell = newRow.insertCell(2);
    const billViewImage = document.createElement('img');
    billViewImage.src = billViewUrl;
    billViewImage.alt = 'Bill View';
    billViewImage.width = 75;
    billViewCell.appendChild(billViewImage);

    // Send AJAX request to save the accepted item
    fetch('/save-accepted-item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
            feature: feature,
            dog_view_url: dogViewUrl,
            bill_view_url: billViewUrl
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to save accepted item');
        }
        // Handle success
    })
    .catch(error => {
        console.error('Error:', error);
    });
}