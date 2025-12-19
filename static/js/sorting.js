const modal = document.getElementById("sortingModal");
const closeBtn = document.querySelector(".close");
const editButtons = document.querySelectorAll(".edit-btn");

editButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const deviceId = btn.dataset.deviceId;
    const serial = btn.dataset.serial;

    document.getElementById("modalDeviceID").value = deviceId;
    document.getElementById("modalSerialNumber").value = serial;

    modal.style.display = "flex";
  });
});

closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target == modal) {
    modal.style.display = "none";
  }
});
